#!/usr/bin/env python3
"""
Session State Tracker for Maxwellian Agent Awareness

This module tracks terminal session state to enable agents to have
contextual awareness of:
- Normal startup vs crash recovery
- Time elapsed since last session
- What work was in progress

Used by Warp Agent initialization to provide intelligent greetings.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path


class SessionStateTracker:
    """Tracks terminal session state for agent awareness."""
    
    def __init__(self, memory_path=None):
        """Initialize tracker with path to Maxwellian Memory."""
        if memory_path is None:
            memory_path = os.path.expanduser("~/Maxwellian/Unity/Memory")
        
        self.memory_path = Path(memory_path)
        self.session_dir = self.memory_path / "05_Logs" / "sessions"
        self.state_file = self.session_dir / ".current_session_state.json"
        
        # Ensure directories exist
        self.session_dir.mkdir(parents=True, exist_ok=True)
    
    def start_session(self, agent_name="CLERK"):
        """
        Mark session start and detect if this is a crash recovery.
        
        Returns:
            dict: Session state with keys:
                - session_type: "normal", "crash_recovery", "long_absence"
                - time_away_seconds: seconds since last session
                - time_away_human: human-readable time away
                - last_session_end: ISO timestamp of last session end (if any)
                - recent_work: list of recent work items from activeContext
        """
        now = datetime.now()
        session_state = {
            "session_type": "normal",
            "time_away_seconds": 0,
            "time_away_human": "first session",
            "last_session_end": None,
            "recent_work": []
        }
        
        # Check for existing session state
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r') as f:
                    last_state = json.load(f)
                
                last_start = datetime.fromisoformat(last_state.get("start_time", ""))
                last_end = last_state.get("end_time")
                
                # Calculate time away
                if last_end:
                    # Clean exit - calculate time away
                    last_end_dt = datetime.fromisoformat(last_end)
                    time_away = now - last_end_dt
                else:
                    # No clean exit = crash
                    time_away = now - last_start
                    session_state["session_type"] = "crash_recovery"
                
                session_state["time_away_seconds"] = time_away.total_seconds()
                session_state["time_away_human"] = self._format_time_away(time_away)
                session_state["last_session_end"] = last_end
                
                # Determine if long absence
                if session_state["session_type"] != "crash_recovery":
                    if time_away > timedelta(hours=24):
                        session_state["session_type"] = "long_absence"
                    elif time_away > timedelta(hours=4):
                        session_state["session_type"] = "normal"
                
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                # Corrupted state file - treat as normal boot
                print(f"Warning: Could not read session state: {e}")
        
        # Get recent work from activeContext
        session_state["recent_work"] = self._get_recent_work()
        
        # Write new session start state
        new_state = {
            "agent_name": agent_name,
            "start_time": now.isoformat(),
            "end_time": None  # Will be set on clean exit
        }
        
        with open(self.state_file, 'w') as f:
            json.dump(new_state, f, indent=2)
        
        return session_state
    
    def end_session(self):
        """Mark session end cleanly."""
        if not self.state_file.exists():
            return
        
        try:
            with open(self.state_file, 'r') as f:
                state = json.load(f)
            
            state["end_time"] = datetime.now().isoformat()
            
            with open(self.state_file, 'w') as f:
                json.dump(state, f, indent=2)
        
        except Exception as e:
            print(f"Warning: Could not mark session end: {e}")
    
    def _format_time_away(self, time_delta):
        """Format time delta into human-readable string."""
        seconds = int(time_delta.total_seconds())
        
        if seconds < 60:
            return f"{seconds} seconds"
        elif seconds < 3600:
            minutes = seconds // 60
            return f"{minutes} minute{'s' if minutes != 1 else ''}"
        elif seconds < 86400:
            hours = seconds // 3600
            return f"{hours} hour{'s' if hours != 1 else ''}"
        else:
            days = seconds // 86400
            return f"{days} day{'s' if days != 1 else ''}"
    
    def _get_recent_work(self):
        """Extract recent work items from activeContext.md."""
        active_context_path = self.memory_path / "01_Context" / "activeContext.md"
        
        if not active_context_path.exists():
            return []
        
        try:
            with open(active_context_path, 'r') as f:
                content = f.read()
            
            # Extract recent sessions/work items
            # Look for "Current Work Focus" section
            recent_work = []
            
            if "## Current Work Focus" in content:
                # Extract first few lines after Current Work Focus
                lines = content.split("\n")
                in_section = False
                line_count = 0
                
                for line in lines:
                    if "## Current Work Focus" in line:
                        in_section = True
                        continue
                    
                    if in_section:
                        if line.startswith("##") and line_count > 0:
                            break
                        
                        if line.strip() and not line.startswith("#"):
                            if line.startswith("-") or line.startswith("*"):
                                recent_work.append(line.strip())
                                line_count += 1
                            elif line.startswith("**") and ":" in line:
                                recent_work.append(line.strip())
                                line_count += 1
                        
                        if line_count >= 5:
                            break
            
            return recent_work[:5]  # Return max 5 items
        
        except Exception as e:
            print(f"Warning: Could not read activeContext: {e}")
            return []
    
    def generate_greeting(self, session_state, agent_name="Clerk", human_name="Mr. Howell"):
        """
        Generate contextual greeting based on session state.
        
        Args:
            session_state: dict from start_session()
            agent_name: Name of the agent (Clerk, Cisco, etc.)
            human_name: Name of the human user
        
        Returns:
            str: Multi-line greeting message
        """
        session_type = session_state["session_type"]
        time_away = session_state["time_away_human"]
        recent_work = session_state["recent_work"]
        
        greeting_lines = []
        
        if session_type == "crash_recovery":
            greeting_lines.append(f"Welcome back, {human_name}! Glad to be back online.")
            greeting_lines.append(f"I detected we crashed {time_away} ago - but I've recovered everything.")
            greeting_lines.append("All context preserved. What were we working on?")
        
        elif session_type == "long_absence":
            greeting_lines.append(f"Good morning, {human_name}! It's been {time_away} since we last spoke.")
            if recent_work:
                greeting_lines.append("\nRecent work from our last sessions:")
                for work in recent_work[:3]:
                    greeting_lines.append(f"  • {work}")
            greeting_lines.append("\nWhat would you like to work on today?")
        
        else:  # normal
            if time_away == "first session":
                greeting_lines.append(f"Good morning, {human_name}! I'm {agent_name}, ready to help.")
            else:
                greeting_lines.append(f"Welcome back, {human_name}! (been {time_away})")
            
            if recent_work and len(recent_work) > 0:
                greeting_lines.append("\nWe were recently working on:")
                for work in recent_work[:2]:
                    greeting_lines.append(f"  • {work}")
            
            greeting_lines.append("\nWhat can I help you with?")
        
        return "\n".join(greeting_lines)


def main():
    """CLI interface for testing session tracking."""
    import sys
    
    tracker = SessionStateTracker()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "start":
            agent_name = sys.argv[2] if len(sys.argv) > 2 else "CLERK"
            human_name = sys.argv[3] if len(sys.argv) > 3 else "Mr. Howell"
            
            state = tracker.start_session(agent_name)
            greeting = tracker.generate_greeting(state, agent_name, human_name)
            
            print("\n" + "="*60)
            print(greeting)
            print("="*60 + "\n")
        
        elif command == "end":
            tracker.end_session()
            print("Session ended cleanly.")
        
        else:
            print(f"Unknown command: {command}")
            print("Usage: session_state_tracker.py [start|end] [agent_name] [human_name]")
    else:
        print("Usage: session_state_tracker.py [start|end] [agent_name] [human_name]")


if __name__ == "__main__":
    main()
