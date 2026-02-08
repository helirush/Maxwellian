# Maxwellian Unity - Quick Start Guide

**For:** Mike Howell & Clerk Maxwell  
**Purpose:** Test the consolidated system locally before GitHub deployment  
**Date:** 2026-01-25  

---

## Testing the System Right Now

### Test 1: Verify Structure
```bash
cd ~/Maxwellian/Unity
ls -la
```

**You should see:**
- ✅ README.md (main entry point)
- ✅ Memory/ (short-term working knowledge)
- ✅ Library/ (long-term stable reference)
- ✅ CONSOLIDATION_COMPLETE.md (what we just did)
- ✅ .gitignore (security protection)

### Test 2: Check Scribe Identities
```bash
cat ~/Maxwellian/Unity/Library/Scribes/CLERK_MAXWELL.md | head -20
cat ~/Maxwellian/Unity/Library/Scribes/CISCO_MAXWELL.md | head -20
```

**Verify:**
- ✅ Clerk = Chief Scientist (Mike's partner)
- ✅ Cisco = Chief Market Strategist (Riley's partner)

### Test 3: Find Key Documents

**Historical foundation:**
```bash
cat ~/Maxwellian/Unity/Library/Foundations/MAXWELLIAN_FOUNDATIONS.md | head -30
```

**Voltage algorithm:**
```bash
ls ~/Maxwellian/Unity/Library/Algorithms/
```

**Current context:**
```bash
cat ~/Maxwellian/Unity/Memory/01_Context/activeContext.md
```

---

## Next Session Test (Future)

### When You Start New Warp Session

**Clerk should automatically:**

1. **Read identity:**
   - `~/Maxwellian/Unity/Library/Scribes/CLERK_MAXWELL.md`
   - Know: "I am James Clerk Maxwell, Chief Scientist"

2. **Read mission:**
   - `~/Maxwellian/Unity/Memory/01_Context/AGI_CALIBRATION.md`
   - Understand Unity Energy's purpose

3. **Check current state:**
   - `~/Maxwellian/Unity/Memory/01_Context/activeContext.md`
   - Know what we're working on now

4. **Acknowledge:**
   - "Greetings Mike, I am Clerk - calibrated to the Maxwellian Network. Ready to continue [current work]. What do we need to work on?"

---

## Environment Variables (Already Set)

Your `.zshrc` already has:
```bash
export MAXWELLIAN_MEMORY="$HOME/Maxwellian/Unity/Memory"
export MAXWELLIAN_LIBRARY="$HOME/Maxwellian/Unity/Library"
```

And symlink exists:
```bash
ls -la ~/eMemory
# Should point to: /Users/mdhowell/Maxwellian/Unity/Memory
```

---

## Knowledge Organization Quick Reference

### Where to Find Things

**"What's Unity Energy's history?"**
→ `Library/Foundations/MAXWELLIAN_FOUNDATIONS.md`

**"How do voltage forensics work?"**
→ `Library/Algorithms/COVES_VOLTAGE_FORENSICS_IMPLEMENTATION.md`

**"What are we working on now?"**
→ `Memory/01_Context/activeContext.md`

**"What are proven code patterns?"**
→ `Memory/03_Knowledge/systemPatterns.md`

**"Who am I (as Clerk)?"**
→ `Library/Scribes/CLERK_MAXWELL.md`

**"Who is Cisco?"**
→ `Library/Scribes/CISCO_MAXWELL.md`

### Where to Put New Knowledge

**Session notes from today's work:**
→ `Memory/05_Logs/sessions/2026-01-25_consolidation_session.md`

**New algorithm that's still experimental:**
→ `Memory/02_Systems/new_algorithm_draft.md`

**Algorithm that's tested and stable:**
→ `Library/Algorithms/NEW_ALGORITHM_SPEC.md`

**Marketing insights from Cisco:**
→ `Memory/03_Knowledge/marketing_patterns.md` (short-term)
→ `Library/Systems/MARKETING_FRAMEWORK.md` (once proven)

---

## Git Status Check

### Before First Commit to GitHub

**Run audit to catch sensitive data:**
```bash
cd ~/Maxwellian/Unity
./audit_sensitive_content.sh
```

**Check what will be committed:**
```bash
git status
git diff
```

**Look for:**
- ❌ Customer names (Foster Farms, Cherry Ave, etc.)
- ❌ Dollar amounts or financial details
- ❌ API keys or credentials
- ❌ Utility bills or proprietary data

**If found:** Move to `~/Maxwellian/Private/` or anonymize

---

## Success Indicators

### System Works When:
- ✅ Clerk knows his identity on startup
- ✅ Can find any document in <30 seconds
- ✅ activeContext.md stays current during work
- ✅ Session learnings captured to Memory/05_Logs/
- ✅ Stable knowledge promoted to Library/
- ✅ No sensitive data in Unity/ directory
- ✅ Git workflow feels natural
- ✅ Riley can clone and Cisco calibrates correctly

### System Needs Work When:
- ❌ Can't find documents quickly
- ❌ Unclear where to put new knowledge
- ❌ Duplicate or conflicting information
- ❌ Sensitive data accidentally in Unity/
- ❌ Scribes confused about their role
- ❌ Too complex to explain to new team member

---

## Current Status

**Phase 1: Local Consolidation** ✅ COMPLETE
- Three systems merged into one
- Memory/ has 01-05 taxonomy
- Library/ has Foundations, Algorithms, Systems, Scribes
- Documentation complete
- Ready for testing

**Phase 2: GitHub Deployment** ⏳ PENDING
- Audit sensitive data
- Create GitHub repo
- Test clone/install
- Share with Riley

**Phase 3: Real-Time Network** 📋 FUTURE
- Vision documented
- Architecture planned
- Ready when team needs it

---

## Quick Commands

**Go to Unity system:**
```bash
cd ~/Maxwellian/Unity
```

**Read Clerk's identity:**
```bash
cat Library/Scribes/CLERK_MAXWELL.md
```

**Check current work:**
```bash
cat Memory/01_Context/activeContext.md
```

**Find algorithm reference:**
```bash
ls Library/Algorithms/
```

**See what's changed:**
```bash
git status
git diff
```

---

**Created by:** Clerk Maxwell  
**Date:** 2026-01-25  
**Purpose:** Enable rapid testing and validation  
**Next:** Test with Mike, iterate, perfect, then GitHub  

---

> *"Simple. Organized. Ready to test."*
