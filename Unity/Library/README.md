# Maxwellian Library - Long-Term Knowledge Repository

**Purpose:** Stable, foundational knowledge that transcends individual projects  
**Update Frequency:** Monthly/Quarterly (only when validated and production-ready)  
**Created:** 2026-01-25  

---

## What Belongs in Library/

### Criteria for Library Content
- ✅ **Stable** - Not changing frequently
- ✅ **Validated** - Tested and proven in production
- ✅ **Foundational** - Core to Unity Energy mission and methodology
- ✅ **Reference** - Used across multiple projects/sessions
- ✅ **Shareable** - Safe to distribute to all Maxwellians

### What Stays in Memory/
- ❌ Active development work
- ❌ Session-specific notes
- ❌ Experimental code or ideas
- ❌ Temporary debugging information
- ❌ Unvalidated hypotheses

**Rule of Thumb:** If it changes weekly, it belongs in Memory/. If it changes monthly or less, promote to Library/.

---

## Directory Organization

### Foundations/
**Historical context, philosophy, mission foundations**

Files:
- `MAXWELLIAN_FOUNDATIONS.md` - 200-year journey from Faraday to Unity Energy
- Future: Unity Energy history, company milestones, vision documents

### Algorithms/
**Proven, production-ready algorithm specifications**

Files:
- `COVES_VOLTAGE_FORENSICS_IMPLEMENTATION.md` - Motor detection and voltage analysis
- `VOLTAGE_HEALTH_ALGORITHM_TECHNICAL_REVIEW.md` - Technical deep dive
- `VOLTAGE_ALGORITHM_QUICK_REFERENCE.md` - Tuning parameters and troubleshooting
- `T10_VOLTAGE_PATTERN_RECOGNITION_LIBRARY.md` - Pattern signatures and baselines

### Systems/
**Core system architecture and established frameworks**

Files:
- `PATTERN_RECOGNITION_SYSTEM.md` - Visual pattern analysis architecture
- `PRODUCTION_CORRELATION_MODEL.md` - Energy-weighted production allocation
- `customerHierarchySystem.md` - 3-tier naming and organization

### Scribes/
**Scribe identity profiles and calibration files**

Files:
- `CLERK_MAXWELL.md` - Chief Scientist profile
- `CISCO_MAXWELL.md` - Chief Market Strategist profile
- Future: Profiles for each Maxwellian scribe as team grows

### Vision Documents
- `FUTURE_MAXWELLIAN_REAL_TIME_NETWORK.md` - Real-time cognitive network architecture

---

## Usage Patterns

### For Scribes Starting a Session
1. Read your profile: `Library/Scribes/[YOUR_NAME].md`
2. Reference algorithms when implementing: `Library/Algorithms/`
3. Check foundational context: `Library/Foundations/`
4. Apply system patterns: `Library/Systems/`

### For Humans
- Reference stable specifications when planning work
- Share Library/ content with customers (educational materials)
- Use as onboarding material for new team members
- Cite in proposals and technical documentation

---

## Promotion from Memory to Library

**When to promote a document from Memory/ to Library/:**

1. **Content has been stable** for 30+ days without changes
2. **Validated in production** - algorithm works, system performs
3. **Referenced frequently** - becomes a go-to resource
4. **Foundational value** - useful beyond current project

**Promotion process:**
```bash
# Copy from Memory to Library (appropriate category)
cp Memory/02_Systems/new_system.md Library/Systems/

# Update file metadata (set Status: REFERENCE)
# Remove temporary notes or session-specific details
# Add to Library/README.md index

# Git commit
git add Library/Systems/new_system.md Library/README.md
git commit -m "Promote new_system to Library - validated and stable"
```

---

## Maintenance

### Monthly Review
- Review Memory/ for content ready to promote
- Update Library/ READMEs with new files
- Check for duplicate or redundant content
- Consolidate related documents if needed

### Quarterly Audit
- Verify all algorithm specs still match production code
- Update outdated content or mark as DEPRECATED
- Reorganize if categories no longer make sense
- Archive obsolete material

---

## Future: Real-Time Network

When Library/ is network-mounted to central Unity server:
- All scribes access same Library/ simultaneously
- Updates appear instantly across all machines
- Git still provides backup and version history
- True cognitive-speed knowledge sharing

See `FUTURE_MAXWELLIAN_REAL_TIME_NETWORK.md` for architecture details.

---

**Maintained by:** All Maxwellian Scribes  
**Primary Curator:** Clerk Maxwell (Chief Scientist)  
**Last Updated:** 2026-01-25  

---

> *"Stable knowledge, shared forever."*
