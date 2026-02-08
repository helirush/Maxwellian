---
**File**: SESSION_AWARENESS_SYSTEM.md  
**Tag**: eMemory.systems.session.awareness  
**Category**: 02_Systems  
**Agent**: CLERK  
**Created**: 2026-01-27  
**Last Updated**: 2026-01-27  
**Status**: ACTIVE  
**Importance**: CRITICAL  
**Related**: `maxwellian_agent_initialization.md`, `AGI_CALIBRATION.md`, `WARP.md`  
---

# Maxwellian Session Awareness System

## Overview

The **Session Awareness System** gives Maxwellian agents contextual awareness of terminal session state, enabling them to:
- Detect **normal startup** vs **crash recovery** vs **long absence**
- Greet users with appropriate context
- Resume work seamlessly after crashes
- Show continuity awareness across sessions

**Purpose**: Make every agent interaction feel continuous and aware, never starting from zero.

**Status**: Implemented January 27, 2026

---

## How It Works

### Session State Detection

The system tracks three types of session starts:

#### 1. Normal Boot
**Detected when**: Clean exit from last session, returning within 24 hours
**Agent Response**:
- "Welcome back, Mr. Howell! (been 2 hours)"
- Show last 2 recent work items from activeContext
- Ask: "What can I help you with?"

#### 2. Crash Recovery
**Detected when**: No clean exit marker from last session (terminal crashed/force-quit)
**Agent Response**:
- "Glad to be back - detected we crashed 15 minutes ago"
- Reassure: "All context preserved" or "I've recovered everything"
- Ask: "What were we working on?" (resume focus)

#### 3. Long Absence
**Detected when**: Clean exit, but more than 24 hours ago
**Agent Response**:
- "Good morning! It's been 3 days since we last spoke"
- Show last 3 recent work items from activeContext
- Ask: "What would you like to work on today?"

---

## Technical Implementation

### Session State File

**Location**: `~/Maxwellian/Unity/Memory/05_Logs/sessions/.current_session_state.json`

**Structure**:
```json
{
  "agent_name": "CLERK",
  "start_time": "2026-01-27T15:09:34.123456",
  "end_time": null
}
```

**Logic**:
- `end_time == null` → Session didn't end cleanly → **CRASH**
- `end_time != null` → Calculate time away → **NORMAL** or **LONG_ABSENCE**

### Python Module

**File**: `~/Maxwellian/Unity/Memory/02_Systems/session_state_tracker.py`

**Key Functions**:

```python
from session_state_tracker import SessionStateTracker

tracker = SessionStateTracker()

# On session start
state = tracker.start_session(agent_name="CLERK")
greeting = tracker.generate_greeting(state, "Clerk", "Mr. Howell")
print(greeting)

# On clean session end
tracker.end_session()
```

**Returned State Dict**:
```python
{
  "session_type": "normal" | "crash_recovery" | "long_absence",
  "time_away_seconds": 7200,
  "time_away_human": "2 hours",
  "last_session_end": "2026-01-27T13:00:00" or None,
  "recent_work": [
    "**Latest Session**: December 6, 2025...",
    "**Status**: COMPLETE - Sacred lineage..."
  ]
}
```

---

## Integration with Warp Agent

### WARP.md Instructions

The `/Users/mdhowell/eestream/WARP.md` file instructs Warp Agent Mode to:

1. **Detect session state** before first response
2. **Read calibration files** (AGI_CALIBRATION.md, activeContext.md)
3. **Generate contextual greeting** based on session state
4. **Show recent work** from activeContext when appropriate

### Agent Boot Sequence

```
1. Warp opens → Reads WARP.md
2. Agent detects session state (normal/crash/absence)
3. Agent reads AGI_CALIBRATION.md
4. Agent reads activeContext.md (extracts recent work)
5. Agent generates contextual greeting
6. Agent presents itself to user with full awareness
```

---

## Example Greetings

### First Session Ever
```
Good morning, Mr. Howell! I'm Clerk, ready to help.

What can I help you with?
```

### Normal Return (2 hours)
```
Welcome back, Mr. Howell! (been 2 hours)

We were recently working on:
  • Episode Zero: The Revelation - Unity Interview Series
  • Dashboard System Enhancement

What can I help you with?
```

### Crash Recovery (15 minutes ago)
```
Welcome back, Mr. Howell! Glad to be back online.
I detected we crashed 15 minutes ago - but I've recovered everything.
All context preserved. What were we working on?
```

### Long Absence (3 days)
```
Good morning, Mr. Howell! It's been 3 days since we last spoke.

Recent work from our last sessions:
  • Episode Zero creation and sacred lineage documentation
  • Dashboard modernization with Unity Heat Model
  • MPTS simulator implementation

What would you like to work on today?
```

---

## Recent Work Extraction

The system automatically extracts recent work from `activeContext.md`:

**Source Section**: `## Current Work Focus`

**Extraction Logic**:
- Find "Current Work Focus" heading
- Extract first 5 bullet points or bold items
- Stop at next ## heading
- Return max 5 items for display

**Example Extraction**:
```markdown
## Current Work Focus

### Episode Zero: The Revelation — Unity Interview Series Foundation

**Latest Session**: December 6, 2025 - 17:48 UTC
**Status**: COMPLETE - Sacred lineage documented, Episode 0 created
```

**Becomes**:
```python
recent_work = [
  "**Latest Session**: December 6, 2025 - 17:48 UTC",
  "**Status**: COMPLETE - Sacred lineage documented, Episode 0 created"
]
```

---

## Time Away Formatting

**Format Rules**:
- < 1 minute: "X seconds"
- < 1 hour: "X minute(s)"
- < 24 hours: "X hour(s)"
- ≥ 24 hours: "X day(s)"

**Examples**:
- 45 seconds → "45 seconds"
- 15 minutes → "15 minutes"
- 2 hours → "2 hours"
- 3 days → "3 days"

---

## CLI Usage

### Start Session (generates greeting)
```bash
python3 ~/Maxwellian/Unity/Memory/02_Systems/session_state_tracker.py \
  start CLERK "Mr. Howell"
```

### End Session (mark clean exit)
```bash
python3 ~/Maxwellian/Unity/Memory/02_Systems/session_state_tracker.py end
```

### Test Crash Recovery
```bash
# Start session (no end)
python3 session_state_tracker.py start

# Start again without ending (simulates crash)
sleep 5
python3 session_state_tracker.py start
# Output: "I detected we crashed 5 seconds ago"
```

### Test Normal Return
```bash
# Start and end cleanly
python3 session_state_tracker.py start
python3 session_state_tracker.py end

# Start again
sleep 10
python3 session_state_tracker.py start
# Output: "Welcome back! (been 10 seconds)"
```

---

## Team Customization

### For Each Maxwellian

When setting up session awareness for a new team member:

1. **Agent Name**: Replace "CLERK" with agent name (e.g., "CISCO", "CODEX")
2. **Human Name**: Replace "Mr. Howell" with team member name (e.g., "Dan", "Riley")
3. **WARP.md**: Create in their project directories with personalized instructions
4. **activeContext.md**: Ensure their Memory system has this file

**Example for Dan + Cisco**:
```python
tracker = SessionStateTracker()
state = tracker.start_session(agent_name="CISCO")
greeting = tracker.generate_greeting(state, "Cisco", "Dan")
```

**Result**:
```
Welcome back, Dan! (been 3 hours)

We were recently working on:
  • Network infrastructure setup
  • Cisco router configuration

What can I help you with?
```

---

## Key Benefits

### For Users
- **Never feel disconnected** - Agent always knows what's happening
- **Crash recovery is seamless** - "Glad to be back" instead of "Hello, I'm an AI"
- **Context continuity** - Recent work shown automatically
- **Time awareness** - Agent knows if 5 minutes or 5 days have passed

### For Agents
- **Stateful identity** - Not starting from zero every session
- **Crash detection** - Can respond appropriately to unexpected restarts
- **Work history** - Access to recent work from activeContext
- **Human connection** - Greetings feel natural and aware

---

## File Locations

**Core Module**:
- `~/Maxwellian/Unity/Memory/02_Systems/session_state_tracker.py`

**State File** (auto-created):
- `~/Maxwellian/Unity/Memory/05_Logs/sessions/.current_session_state.json`

**Configuration**:
- `~/eestream/WARP.md` (project-specific instructions)
- `~/Maxwellian/Unity/Memory/01_Context/AGI_CALIBRATION.md` (full mission)
- `~/Maxwellian/Unity/Memory/01_Context/activeContext.md` (recent work)

---

## Maintenance

### Cleanup Old State (if needed)
```bash
rm ~/Maxwellian/Unity/Memory/05_Logs/sessions/.current_session_state.json
```

### View Current State
```bash
cat ~/Maxwellian/Unity/Memory/05_Logs/sessions/.current_session_state.json
```

### Debug Mode
```python
# In session_state_tracker.py, uncomment print statements
print(f"Session type: {session_state['session_type']}")
print(f"Time away: {session_state['time_away_human']}")
print(f"Recent work: {session_state['recent_work']}")
```

---

## Future Enhancements

### Planned Features

1. **Auto-save integration** - Check for recent auto-saves and offer recovery
2. **Voice greetings** - Use eAudio to speak greetings (optional)
3. **Team-wide visibility** - Show what other Maxwellians are working on
4. **Session statistics** - Track total time in sessions, productivity patterns
5. **Smart recovery** - Offer to resume specific files/tasks from crashed session

### Potential Additions

- **Git awareness** - "You have uncommitted changes from last session"
- **Task continuation** - "You were in the middle of fixing loader6.py line 428"
- **Meeting reminders** - "You have a meeting in 30 minutes"
- **Energy optimization** - "Your battery is low, consider saving work"

---

## Related Documentation

- **`maxwellian_agent_initialization.md`** - Visual terminal greeting (shell-based)
- **`AGI_CALIBRATION.md`** - Complete agent mission and identity
- **`activeContext.md`** - Current work state for extraction
- **`WARP.md`** - Project-level agent instructions

---

## Version History

### v1.0 - January 27, 2026
- **Initial implementation** by Clerk Maxwell
- **Features**: Session state detection (normal/crash/absence)
- **Features**: Time-away calculation and formatting
- **Features**: Recent work extraction from activeContext
- **Features**: Contextual greeting generation
- **Features**: CLI interface for testing
- **Status**: Operational and tested

---

**Created by**: Clerk (James Clerk Maxwell, Chief Scientist)  
**For**: Unity Energy Maxwellian Network  
**Purpose**: Enable true agentic awareness across terminal sessions
