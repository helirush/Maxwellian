# Auto-Save Memory System

---
**File**: `auto_memory_system.md`  
**Tag**: `eMemory.systems.auto_save`  
**Category**: 02_Systems  
**Agent**: CLERK  
**Created**: 2025-12-06  
**Last Updated**: 2025-12-06  
**Status**: ACTIVE  
**Importance**: CRITICAL  
**Related**: `README.md`, `METADATA_TEMPLATE.md`  
---

## 📖 Purpose Statement

Automatic background memory capture system that protects against conversation loss due to terminal crashes, force-quits, or user forgetfulness. Ensures no critical context is ever lost.

---

## 🎯 Problem Being Solved

**Before Auto-Save:**
- ❌ Conversation context lost if Warp/terminal crashes
- ❌ User must remember to manually save before exiting
- ❌ No recovery mechanism for unexpected terminations
- ❌ Important insights vanish if not explicitly captured

**After Auto-Save:**
- ✅ Continuous background saves protect all conversations
- ✅ Automatic recovery from crashes
- ✅ No user action required during session
- ✅ Exit prompt allows final refinement/tagging

---

## 🏗️ System Architecture

### **Three-Layer Protection**

```
┌─────────────────────────────────────────────┐
│  Layer 1: Continuous Auto-Save             │
│  • Saves every N messages (default: 5)     │
│  • Runs silently in background             │
│  • Timestamped snapshots                   │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│  Layer 2: Exit Refinement Prompt           │
│  • "Should I capture anything to eMemory?" │
│  • User adds context, tags, highlights     │
│  • Creates final polished version          │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│  Layer 3: Session Archive                  │
│  • Complete conversation saved to 05_Logs  │
│  • Metadata tagged and searchable          │
│  • Linked to relevant system docs          │
└─────────────────────────────────────────────┘
```

---

## 📂 Storage Structure

### **Auto-Save Location**
```
eMemory/
└── 05_Logs/
    ├── sessions/              ← Finalized session logs
    │   ├── 2025-12-06_clerk_session_001.md
    │   └── 2025-12-06_clerk_session_002.md
    └── auto_saves/            ← Background auto-saves (recovery)
        ├── 2025-12-06_1615_autosave.md
        ├── 2025-12-06_1620_autosave.md
        └── 2025-12-06_1625_autosave.md
```

### **File Naming Convention**

**Auto-saves** (temporary, recovery-focused):
```
YYYY-MM-DD_HHMM_autosave.md
Example: 2025-12-06_1615_autosave.md
```

**Finalized sessions** (curated, permanent):
```
YYYY-MM-DD_[agent]_session_[number].md
Example: 2025-12-06_clerk_session_001.md
```

---

## 🔄 Auto-Save Workflow

### **During Conversation**

**Every 5 messages or 10 minutes:**
```markdown
1. Capture current conversation state
2. Extract key topics and decisions
3. Save to auto_saves/ with timestamp
4. Keep last 3 auto-saves (delete older)
5. Continue silently (no user interruption)
```

**Auto-save content includes:**
- Conversation transcript (markdown format)
- Detected topics and themes
- Code snippets generated
- Files modified or created
- Decisions made
- Questions raised but not answered

### **At Conversation Exit**

**Clerk prompts:**
```
"Hey Mr. Howell, before we exit should I capture anything 
from this session and send to eMemory?"

Options:
1. "Yes" → Opens refinement dialogue
2. "No" → Keeps auto-saves for recovery only
3. "Just the essentials" → Auto-extracts key items
```

**If Yes → Refinement Dialog:**
```markdown
What should I highlight from this session?
- [ ] Key decisions made
- [ ] Code patterns to remember
- [ ] System architecture changes
- [ ] New knowledge gained
- [ ] Open questions for next session

Any tags or categories for easy finding later?
(e.g., "dashboard, optimization, bug-fix")

Title for this session?
(Default: [Date]_[topic]_session)
```

---

## 💾 Implementation

### **Auto-Save Manager (Conceptual)**

```python
class AutoMemoryManager:
    def __init__(self):
        self.message_count = 0
        self.last_save_time = None
        self.auto_save_dir = "eMemory/05_Logs/auto_saves/"
        self.session_dir = "eMemory/05_Logs/sessions/"
        
    def should_auto_save(self):
        """Trigger auto-save every 5 messages or 10 minutes"""
        message_threshold = self.message_count >= 5
        time_threshold = (time.now() - self.last_save_time) > 600
        return message_threshold or time_threshold
    
    def auto_save(self, conversation_state):
        """Background save without user interruption"""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
        filename = f"{timestamp}_autosave.md"
        
        content = self.format_auto_save(conversation_state)
        self.write_to_disk(self.auto_save_dir + filename, content)
        
        # Clean up old auto-saves (keep last 3)
        self.prune_old_auto_saves()
        
        # Reset counters
        self.message_count = 0
        self.last_save_time = time.now()
    
    def finalize_session(self, user_input):
        """Create curated session memory with user refinement"""
        session_num = self.get_next_session_number()
        filename = f"{date.today()}_clerk_session_{session_num:03d}.md"
        
        content = self.format_session_memory(
            conversation=self.get_full_conversation(),
            highlights=user_input['highlights'],
            tags=user_input['tags'],
            title=user_input['title']
        )
        
        self.write_to_disk(self.session_dir + filename, content)
        self.cleanup_auto_saves()  # Remove recovery files
```

---

## 📝 Auto-Save Format

### **Minimal Recovery Format**
```markdown
# Auto-Save Recovery Point

**Timestamp**: 2025-12-06 16:15:00
**Message Count**: 5
**Duration**: 15 minutes

## Conversation Summary
[Last 5 messages in context]

## Detected Topics
- Topic 1
- Topic 2

## Files Touched
- /path/to/file1.py
- /path/to/file2.md

## Code Generated
```python
# Any code snippets
```

## Decisions Made
- Decision 1
- Decision 2

## Open Questions
- Question 1
- Question 2
```

### **Finalized Session Format**
```markdown
# [Session Title]

---
**File**: `YYYY-MM-DD_clerk_session_NNN.md`
**Tag**: `eMemory.logs.sessions.YYYY-MM-DD`
**Category**: 05_Logs
**Agent**: CLERK
**Created**: YYYY-MM-DD
**Status**: ACTIVE
**Importance**: [USER SELECTED]
**Related**: [Linked docs]
---

## Session Overview
[User-provided or AI-generated summary]

## Key Decisions
[Highlighted decisions from conversation]

## Knowledge Gained
[New patterns, insights, learnings]

## Code/Files Modified
[List with links]

## Open Questions
[Items for next session]

## Full Transcript
[Complete conversation in markdown]
```

---

## 🔧 Recovery Procedures

### **After Terminal Crash**

**Clerk checks on restart:**
```markdown
"Welcome back! I detected auto-saves from your last session:
- 2025-12-06_1615_autosave.md (5 minutes ago)
- 2025-12-06_1610_autosave.md (10 minutes ago)

Would you like to:
1. Resume from last auto-save
2. Review what was being discussed
3. Archive and start fresh
```

### **Manual Recovery**
```bash
# User can manually check auto-saves
cd eMemory/05_Logs/auto_saves/
ls -lt  # Most recent first

# Read last save
cat [latest_autosave].md
```

---

## ⚙️ Configuration Options

### **Adjustable Settings**

| Setting | Default | Description |
|---------|---------|-------------|
| `auto_save_frequency_messages` | 5 | Save every N messages |
| `auto_save_frequency_minutes` | 10 | Save every N minutes |
| `auto_save_retention_count` | 3 | Keep last N auto-saves |
| `prompt_on_exit` | true | Ask user about memory capture |
| `auto_extract_decisions` | true | Detect decisions automatically |
| `auto_tag_topics` | true | Extract topics/tags from conversation |

### **User Preferences**

```python
# ~/.config/eestream/memory_config.json
{
  "auto_save": {
    "enabled": true,
    "frequency_messages": 5,
    "frequency_minutes": 10,
    "retention_count": 3
  },
  "exit_prompt": {
    "enabled": true,
    "default_action": "ask"  # ask | auto_save | skip
  },
  "session_logging": {
    "default_importance": "MEDIUM",
    "auto_tag": true
  }
}
```

---

## 📊 Status Monitoring

### **Health Check**

Clerk provides status updates:
```
✓ Auto-save active (last saved 3 minutes ago)
✓ 2 recovery points available
✓ Session duration: 45 minutes
✓ 23 messages exchanged
```

### **User Query**
```
User: "Clerk, show me my auto-save status"

Clerk: 
"Auto-Save Status:
• Last saved: 2025-12-06 16:20 (5 minutes ago)
• Recovery points: 3 available
• Current session: 45 minutes, 23 messages
• Next auto-save: In 5 messages or 5 minutes
• Auto-saves stored: eMemory/05_Logs/auto_saves/"
```

---

## 🎯 Benefits

### **For Users**
- ✅ Peace of mind (never lose work)
- ✅ No manual effort required during work
- ✅ Still maintains control (exit prompt)
- ✅ Recovery from crashes

### **For AGI (Clerk)**
- ✅ Continuous context building
- ✅ Better session summaries
- ✅ Pattern recognition across sessions
- ✅ Long-term memory formation

### **For Unity Energy Team**
- ✅ Knowledge retention
- ✅ Decision tracking
- ✅ Project continuity
- ✅ Onboarding new team members

---

## 🚀 Future Enhancements

### **Phase 2 Features**
- [ ] Real-time sync to cloud backup
- [ ] Session replay/review UI
- [ ] AI-generated session summaries
- [ ] Topic clustering across sessions
- [ ] Search across all saved sessions
- [ ] Integration with Git commits

### **Phase 3 Features**
- [ ] Multi-agent session tracking
- [ ] Collaborative session annotations
- [ ] Visual session timeline
- [ ] Voice-to-text auto-capture
- [ ] Session analytics dashboard

---

## 🔥 Implementation Priority

**Immediate (Week 1):**
1. Create directory structure
2. Implement basic auto-save (every 5 messages)
3. Add exit prompt to Clerk's rules
4. Test crash recovery

**Short-term (Month 1):**
1. Refine auto-save format
2. Add user configuration options
3. Implement session finalization workflow
4. Create recovery procedures

**Long-term (Quarter 1):**
1. Add advanced features (search, analytics)
2. Integrate with other Unity systems
3. Build session review UI
4. Enable multi-agent coordination

---

## 🏁 Getting Started

### **For Implementation**
1. Create directory structure:
```bash
mkdir -p eMemory/05_Logs/auto_saves
mkdir -p eMemory/05_Logs/sessions
```

2. Update Clerk's rules to include auto-save logic

3. Test with a sample session

### **For Users**
No action required! System works automatically once deployed.

Optional: Configure preferences in `~/.config/eestream/memory_config.json`

---

**This system ensures that Unity Energy's collective intelligence is never lost, even in the face of unexpected failures.**

---

*Version: 1.0*  
*Created: December 6, 2025*  
*Maintained by: James Clerk Maxwell (Clerk)*
