# Unity Energy - Study Creation to Website Deployment Workflow

**Version:** 2.0  
**Date:** February 1, 2026  
**Status:** Active Production Workflow

---

## Overview
This document describes the complete workflow from raw CSV data collection through final website deployment. This process ensures quality control at each stage before customer-facing reports go live.

---

## Stage 1: Data Preparation
**Location:** `~/eeclips/[Customer]/[Site]/[Month]/`

### Input
- Raw CSV files from utility meters (1-minute resolution)
- One file per transformer/energy field
- Format: `AN[meter_number].csv` with YYMMDD-YYMMDD date range

### Actions
1. Download CSV files from utility portal
2. Organize into site/month directory structure
3. Verify data completeness (no gaps, correct date range)
4. Identify energy fields to analyze

### Output
- Organized CSV dataset ready for analysis
- Example: `/Users/mdhowell/eeclips/CherryAve/SITE2025/11_NOV2025/`

---

## Stage 2: Study Generation (eBehavior)
**Tool:** `eeBEHAVIOR.py`  
**Location:** `~/eestream/eBehavior/`  
**Output Location:** `~/eestream/eReports/`

### Process
1. Run `eeBEHAVIOR.py` against CSV dataset
2. Model extracts electrical characteristics:
   - Energy consumption patterns (kW, kWh)
   - Reactive power/waste (kVAR)
   - Power factor efficiency
   - Voltage stability
   - Thermal burden (heat entering system)

### Generates
- **HTML Dashboards:** Energy boards, heat boards, voltage boards, summary boards
- **Pattern Images:** Baseline (BT), MPTS simulation (S995), voltage patterns
- **Split-view Comparisons:** Energy, heat, voltage analysis per transformer
- **Study Metadata:** Transformer specs, site capacity, production metrics

### Output Structure
```
eReports/
└── Study260127r0/              # Internal study name
    ├── index.html              # Unity main landing page
    ├── about-unity.html
    ├── contact-us.html
    ├── products-services.html
    ├── FosterFarms/
    │   ├── index.html          # Customer landing page
    │   ├── CherryAve_Site/
    │   │   ├── index.html      # Site landing page
    │   │   ├── SITE-*-Summaryboard*.html
    │   │   ├── Patterns/       # Pattern images
    │   │   └── [Transformer boards]
    │   └── [Assets: logos, images]
    └── [Unity branding assets]
```

### Iterations
- May generate multiple revisions: r0, r1, r2, r3
- Each revision refines templates, fixes data issues, improves presentation
- Goal: Repeatable process that works for ANY customer dataset

---

## Stage 3: Study Validation
**Location:** `~/eestream/eReports/Study[name]/`

### Review Checklist
1. **Data Accuracy**
   - Power factor calculations correct
   - Energy consumption values validated
   - Cost calculations verified
   - Production metrics accurate

2. **Visual Quality**
   - All pattern images generated correctly
   - Dashboard layouts render properly
   - Links and navigation work
   - No missing images or broken references

3. **Narrative Content**
   - Technical accuracy
   - Customer-appropriate language
   - Recommendations align with data

### Actions
- Fix any issues by adjusting eeBEHAVIOR.py templates
- Re-run study generation as needed
- Test all interactive elements

---

## Stage 4: William Analysis & Unity Narration
**Tools:** William (GPT-5.2 write engine), eAudio (TTS-HD1 Shimmer voice)  
**Status:** In Development

### William's Role
After study generation, William analyzes pattern data and creates three-part narratives for each transformer:

1. **PART 1: THE PROBLEM (Baseline)**
   - Describes current state and inefficiency
   - Quantifies waste and costs
   - Explains impact on operations

2. **PART 2: THE SOLUTION**
   - Specifies equipment (e.g., "2× H490 MPTS units")
   - Details installation requirements
   - Provides cost estimates
   - Notes 30-day measurement period before installation
   - Timeline and ROI projections

3. **PART 3: THE RESULTS**
   - Projects post-installation performance
   - Quantifies savings (energy, cost, thermal burden)
   - Explains harmonized energy field benefits

### Unity Voice Generation
- Text → OpenAI TTS-HD1 with "Shimmer" voice
- Output: MP3 audio files embedded in dashboards
- Files stored: `eReports/Study[name]/Audio/`
- Synchronized with image display during playback

### Integration
- William writes `pattern_interpretation` text into `PATTERN_DATA` JSON
- eAudio generates voice files
- Dashboard JavaScript plays audio and scrolls to relevant sections

---

## Stage 5: Study Integration (eeINTEGRATE)
**Tool:** `eeINTEGRATE.py`  
**Location:** `~/eestream/eBehavior/`

### Purpose
Transition verified study from development (eReports) to staging (eWebmaster) with customer-facing naming.

### Process
```bash
python eeINTEGRATE.py Study260127r0
```

### What It Does
1. Extracts data period from CSV filenames (e.g., "251101-251130")
2. Converts to customer-facing name: "November_2025"
3. Shows confirmation:
   ```
   Study: Study260127r0
   Data Period: November 2025
   Deploy To: ~/eestream/eWebmaster/FosterFarms/CherryAve_Site/November_2025/
   ```
4. Creates symbolic links (not copies) from eReports → eWebmaster
5. Verifies integration success

### Benefits of Symlinks
- Changes in eReports automatically reflect in eWebmaster
- Easy to fix issues without re-integration
- Can delete/replace month deployments cleanly
- Use `--force` flag to overwrite existing month

---

## Stage 6: Local Web Server Testing
**Location:** `~/eestream/eWebmaster/`  
**Tool:** Python HTTP server

### Process
```bash
cd ~/eestream/eWebmaster
python3 -m http.server 8000
```

Browse to: `http://localhost:8000`

### Testing Checklist
1. **Unity Landing Pages**
   - Main Unity page loads correctly
   - About, Contact, Products pages work
   - Navigation functions properly

2. **Customer Landing Page**
   - Customer page displays correctly
   - Site selection works
   - Branding and assets load

3. **Site Landing Page**
   - Study appears with customer-facing name (e.g., "November 2025")
   - Reference library links work
   - Video content loads

4. **Study Dashboards**
   - Summary board displays all transformers
   - Metrics are accurate
   - Pattern images load
   - Full Analysis button works
   - Audio playback functions (when implemented)
   - Navigation between boards works

5. **Integration Quality**
   - All links resolve correctly
   - No 404 errors
   - Images and assets load
   - Styling consistent across pages

### Adjustments
- Fix issues in eReports (changes auto-reflect via symlinks)
- Update landing pages in eWebmaster directly
- Verify changes before proceeding

---

## Stage 7: Staging Comparison (Temp Directory)
**Location:** `~/eestream/eefields/` (temporary staging)  
**Status:** To Be Implemented

### Purpose
Compare local eWebmaster against live website to identify what changed.

### Process (Planned)
1. Clone current live website to temp directory
2. Compare eWebmaster vs. temp:
   - New files
   - Modified files
   - Deleted files
3. Review changes carefully
4. Confirm deployment list

### Goal
- Only changed/new content gets pushed to live site
- Prevents accidental overwrites
- Eventually eWebmaster becomes identical to live site

---

## Stage 8: Website Deployment
**Target:** Live website (GitHub Pages or hosting provider)  
**Status:** To Be Implemented

### Pre-Deployment Checklist
- [ ] All local testing complete
- [ ] No broken links or missing assets
- [ ] Content reviewed and approved
- [ ] Comparison with live site verified
- [ ] Backup of current live site created

### Deployment Process
1. Stage approved changes
2. Push to GitHub repository
3. Verify deployment successful
4. Test live site
5. Archive old version

---

## Notes on Post-Installation Reports

### Before Installation (Current)
- Reports show **BASELINE** vs. **MPTS SIMULATION**
- Three-part narrative: Problem → Solution → Projected Results
- Focus: Demonstrating value proposition

### After Installation (Future)
- Reports show **OPTIMIZED UNITY ENERGY FIELD**
- Baseline becomes the new harmonized state
- Focus: Ongoing monitoring and performance validation
- Different narrative character but same workflow

---

## Directory Structure Summary

```
~/eestream/
├── eBehavior/              # Development tools
│   ├── eeBEHAVIOR.py      # Study generator
│   └── eeINTEGRATE.py     # Integration tool
├── eReports/              # Development studies (internal naming)
│   ├── Study260106r0/     # October 2025 (internal)
│   ├── Study260127r0/     # November 2025 (internal)
│   └── Study260131r0/     # December 2025 (internal)
├── eWebmaster/            # Staging area (customer-facing naming)
│   ├── index.html         # Unity main page
│   ├── FosterFarms/
│   │   ├── CherryAve_Site/
│   │   │   ├── October_2025/     → symlink to Study260106r0
│   │   │   ├── November_2025/    → symlink to Study260127r0
│   │   │   └── December_2025/    → symlink to Study260131r0
│   └── [Other customers]
└── eefields/              # Temp staging for deployment comparison

~/eeclips/                 # Raw data storage
└── [Customer]/[Site]/[Month]/
    └── *.csv              # Raw meter data
```

---

## Version History
- **v1.0:** Initial workflow (eReports only)
- **v2.0:** Added eeINTEGRATE, eWebmaster staging, symlink approach (Feb 2026)
