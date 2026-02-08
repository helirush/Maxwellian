# eStream Knowledge Base - Maxwellian Memory System (MMS)

**Date:** 2026-01-30  
**Location:** `/Users/mdhowell/Maxwellian/Unity/eStream/`  
**Purpose:** Consolidated eStream software development knowledge

---

## Migration from Old eMemory Locations

**Previous locations (DEPRECATED):**
- `/Users/mdhowell/eestream/eMemory/` — Old general memory location
- `/Users/mdhowell/eestream/eBehavior/eMemory/` — Old eBehavior-specific memory

**New unified location:**
- `/Users/mdhowell/Maxwellian/Unity/eStream/` — Maxwellian Memory System (MMS)

⚠️ **DO NOT add new content to old eMemory directories. Use this location instead.**

---

## Directory Structure

```
eStream/
├── README.md                    ← This file
├── Memory/                      ← Long-term architectural knowledge
│   ├── Core/                    (eStream core concepts)
│   ├── Architecture/            (system design patterns)
│   └── APIs/                    (integration patterns)
│
├── eBehavior/                   ← eBehavior module documentation
│   ├── Features/                (feature documentation)
│   ├── Sessions/                (development sessions)
│   └── Patterns/                (analysis patterns)
│
├── eVision/                     ← eVision module documentation
│   └── ...
│
└── Sessions/                    ← Short-term work sessions
    └── 2026/                    (organized by year/month)
```

---

## Content Categories

### Memory/ (Long-term Knowledge)
**What belongs here:**
- System architecture and design patterns
- Core algorithms and methodologies
- Technical specifications and standards
- Integration patterns and APIs
- Best practices and conventions

**Examples:**
- Maxwellian field theory implementations
- Pattern recognition algorithms
- Voltage analysis methodologies
- Dashboard generation systems
- File processing workflows

### eBehavior/ (Module-Specific)
**What belongs here:**
- eBehavior feature documentation
- Analysis techniques and methods
- Development sessions for eBehavior work
- Bug fixes and enhancements specific to eBehavior
- Pattern libraries and examples

### Sessions/ (Short-term Context)
**What belongs here:**
- Recent development work logs
- Bug investigation notes
- Feature implementation sessions
- Troubleshooting and debugging
- Temporary notes and working drafts

**Retention:** Sessions older than 6 months should be reviewed and either:
1. Promoted to Memory/ (if containing lasting knowledge)
2. Moved to Private/Archives/ (if customer-specific)
3. Deleted (if no longer relevant)

---

## Migration Plan

### Phase 1: Consolidation (Current)
✅ Create new MMS structure under Unity/eStream/  
⏳ Review old eMemory content  
⏳ Categorize into Memory/, eBehavior/, eVision/, or Sessions/  
⏳ Migrate valuable content to new location  
⏳ Create deprecation notice in old locations  

### Phase 2: Integration
- Update Warp MCP Memory to read from Unity/ location
- Update environment variables if needed
- Create symlinks if backward compatibility required
- Test with AI Scribes to ensure proper context loading

### Phase 3: Cleanup
- Archive old eMemory directories
- Remove deprecated content
- Update all documentation references
- Verify team has access to new structure

---

## Usage Guidelines

### Adding New Knowledge
```bash
# Navigate to appropriate location
cd ~/Maxwellian/Unity/eStream/

# Create or edit documentation
vim Memory/NEW_CONCEPT.md

# Commit with clear message
git add Memory/NEW_CONCEPT.md
git commit -m "Add [topic] - [brief description]

Co-Authored-By: Warp <agent@warp.dev>"

# Share with team
git push origin main
```

### Session Documentation
```bash
# Create session log
DATE=$(date +%Y-%m-%d)
vim Sessions/2026/SESSION_${DATE}_TOPIC.md

# Include:
# - Date and context
# - Problem/feature being addressed
# - Key decisions and reasoning
# - Code changes and locations
# - Follow-up items
```

### Finding Information
```bash
# Search across all eStream knowledge
cd ~/Maxwellian/Unity/eStream/
grep -r "voltage analysis" .

# Search in MCP Memory (via Warp)
# Just ask: "What do we know about voltage analysis?"
# MCP will search the knowledge graph
```

---

## What NOT to Store Here

❌ **Customer-specific data** → Goes in `/Users/mdhowell/Maxwellian/Private/`
- Customer names, sites, contacts
- Specific utility data and bills
- Proprietary customer implementations
- Financial details and pricing

❌ **Personal notes** → Goes in `/Users/mdhowell/Maxwellian/Personal/`
- Your private working notes
- Experimental ideas not ready to share
- Draft materials under development

✅ **Generalized patterns OK** → Can be anonymized and shared
- "Large poultry facility analysis pattern" (not "Foster Farms")
- "Multi-building campus approach" (not specific customer name)
- "480V system with 8 transformers" (anonymized example)

---

## MCP Integration

### Current MCP Memory Configuration
The Warp Memory MCP should read from:
```
/Users/mdhowell/Maxwellian/Unity/Memory/
/Users/mdhowell/Maxwellian/Unity/eStream/Memory/
```

### Thread Initialization
When starting a new Warp session:
1. AI Scribe reads MCP Memory knowledge graph
2. Establishes baseline from Unity + eStream knowledge
3. Applies context throughout conversation
4. Before closing, asks: "Should I capture anything to memory?"

---

## Contact & Questions

**Maintained by:** Clerk (Chief Scribe)  
**For:** Unity Energy technical team  
**Questions:** Reference this README and MCP Memory

---

> *"Make the invisible visible through systematic knowledge capture."*  
> — Maxwellian Memory System (MMS)
