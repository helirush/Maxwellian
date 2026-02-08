# Maxwell Library - Installation & Distribution Guide

**Library Name:** Maxwellian Unity Memory (Maxwell Library)  
**Version:** 1.0  
**Distribution Date:** 2026-01-16  
**Size:** 204 KB  
**Files:** 21 documents  

---

## Installation Instructions

### For New Team Members (Riley, Beck, etc.)

**Step 1: Extract the Archive**
```bash
# You will receive: maxwellian-unity-memory.zip
unzip maxwellian-unity-memory.zip
```

**Step 2: Place in Home Directory**
```bash
# The extraction should create this structure:
/Users/[yourname]/maxwellian/unity/memory/

# Verify:
ls -la ~/maxwellian/unity/memory/
```

**Step 3: Symlink for Easy Access (Optional but Recommended)**
```bash
# Create a shortcut in home directory for quick access:
ln -s ~/maxwellian/unity/memory ~/eMemory

# Now you can access with: ~/eMemory/
```

**Step 4: Environment Variable (Optional)**
```bash
# Add to ~/.zshrc or ~/.bash_profile:
export MAXWELL_MEMORY="$HOME/maxwellian/unity/memory"

# Then use: $MAXWELL_MEMORY/T10_VOLTAGE_PATTERN_RECOGNITION_LIBRARY.md
```

---

## Directory Structure

```
maxwellian/unity/memory/
├── 06_Architecture/              # System architecture documents
├── ANTHROPIC_API_KEY_LOCATION.md # API key storage reference
├── COVES_VOLTAGE_FORENSICS_IMPLEMENTATION.md
├── T10_VOLTAGE_PATTERN_RECOGNITION_LIBRARY.md  # <-- NEW
├── MAXWELLIAN_FOUNDATIONS.md     # Historical & philosophical context
├── PATTERN_RECOGNITION_SYSTEM.md
├── PRODUCTION_CORRELATION_MODEL.md
├── VOLTAGE_ALGORITHM_QUICK_REFERENCE.md
├── README.md                     # Master index
└── [Other documents...]
```

---

## Quick Start

### For Voltage Analysis
1. Read: `COVES_VOLTAGE_FORENSICS_IMPLEMENTATION.md`
2. Reference: `VOLTAGE_ALGORITHM_QUICK_REFERENCE.md`
3. For T10 specific: `T10_VOLTAGE_PATTERN_RECOGNITION_LIBRARY.md`

### For Pattern Recognition
1. Read: `PATTERN_RECOGNITION_SYSTEM.md`
2. Study: `PRODUCTION_CORRELATION_MODEL.md`

### For Historical Context
1. Read: `MAXWELLIAN_FOUNDATIONS.md`

---

## Contents Manifest

### Core Technical Documents (7)
- `COVES_VOLTAGE_FORENSICS_IMPLEMENTATION.md` - Motor detection and voltage forensics
- `VOLTAGE_HEALTH_ALGORITHM_TECHNICAL_REVIEW.md` - Technical deep dive
- `VOLTAGE_ALGORITHM_QUICK_REFERENCE.md` - Quick tuning parameters
- `T10_VOLTAGE_PATTERN_RECOGNITION_LIBRARY.md` - **NEW - T10 specific patterns**
- `PATTERN_RECOGNITION_SYSTEM.md` - Visual field analysis
- `PRODUCTION_CORRELATION_MODEL.md` - Energy-to-production mapping
- `customerHierarchySystem.md` - Customer naming conventions

### Design & Historical Documents (5)
- `MAXWELLIAN_FOUNDATIONS.md` - 200-year journey and philosophy
- `RESPONSE_TO_COVE.md` - Design decision rationale
- `IDEAS_FOR_COVE.md` - Future enhancements
- `THERMAL_BURDEN_CALCULATION_FIX_DEC2024.md` - Historical fix
- `VOLTAGE_NOMINAL_AUTO_DETECTION_FIX.md` - Historical fix

### Session Logs & References (8)
- SESSION_2025-12-31_AI_PATTERN_ANALYZER_FIX.md
- SESSION_2025-12-29_DASHBOARD_FIXES_R0.md
- SESSION_2025-12-21_PATTERN_ANALYSIS_TRAINING.md
- SESSION_2025-12-14_PRODUCTION_ALLOCATION.md
- DAILY_CHART_PATTERN_AND_POWER_FACTOR_FIXES.md
- ELECOPS_CALCULATION_ISSUE.md
- ANTHROPIC_API_KEY_LOCATION.md
- 06_Architecture/ (directory)

### Master Index
- `README.md` - Complete documentation index

---

## Updating the Library

### If You're the Maintainer

**When new documentation is ready:**
1. Add document to `/Users/mdhowell/maxwellian/unity/memory/`
2. Update `README.md` with new entry
3. Create distribution package

**To create distribution package:**
```bash
cd /Users/mdhowell
zip -r maxwellian-unity-memory.zip maxwellian/unity/memory/
# File: maxwellian-unity-memory.zip
```

**To distribute:**
1. Email `maxwellian-unity-memory.zip` to team member
2. They extract to home directory
3. They get `/Users/[theirname]/maxwellian/unity/memory/`

---

## Support

**Questions about:**
- **Voltage analysis:** See `COVES_VOLTAGE_FORENSICS_IMPLEMENTATION.md`
- **T10 patterns:** See `T10_VOLTAGE_PATTERN_RECOGNITION_LIBRARY.md`
- **Motor detection:** See `VOLTAGE_HEALTH_ALGORITHM_TECHNICAL_REVIEW.md`
- **Naming conventions:** See `customerHierarchySystem.md`
- **Philosophy & context:** See `MAXWELLIAN_FOUNDATIONS.md`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-16 | Initial distribution package. Added T10 Voltage Pattern Recognition Library. Consolidated all eMemory documents into maxwellian/unity/memory structure. |

---

## Maintenance Contact

**Maintainer:** MD Howell, Unity Energy LLC  
**Repository:** `/Users/mdhowell/maxwellian/unity/memory/`  
**Distribution:** See instructions above for creating and sharing `maxwellian-unity-memory.zip`

---

**Last Updated:** 2026-01-16  
**Next Review:** 2026-02-16
