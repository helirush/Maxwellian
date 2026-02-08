# Complete eBehavior Workflow: Raw Data → Website Deployment

**Last Updated:** February 5, 2026  
**Documentation Status:** Canonical Reference

---

## Overview

This document describes the complete end-to-end workflow for processing customer energy data from raw meter readings through final website deployment. The system consists of multiple tools working together to analyze electrical behavior, generate insights, and create customer-facing dashboards.

---

## Stage 1: Data Extraction (eVision Builder)

### Source: Unity Customer Library
- **Location:** Microsoft-hosted cloud storage
- **Access:** Unity Energy controls this library
- **Content:** All customer energy meter data feeds

### Tool: eVision Builder
**Purpose:** Extract specific datasets from Unity Customer Library

**User Actions:**
1. Open eVision Builder
2. Select customer/site
3. Select meters (by serial number, e.g., AN53111387)
4. Choose resolution (typically 1-minute)
5. Choose timeframe (e.g., November 1-30, 2025)
6. Execute extraction

**Output:**
- Raw CSV files containing: kVA, kW, kVAR, voltage, current, power factor
- Files deposited in: `/eestream/eBuilder/eReport/`

---

## Stage 2: Manual Organization (File Management)

### Process
1. **Examine** raw CSV files from eBuilder output
2. **Validate** data quality and completeness
3. **Manually move** files to customer directory structure

### Directory Structure
```
/eeclips/[Customer]/[Site]/[MonthNumber]_[MONTHYEAR]/
├── AN53110845-V-1minRES_43260CLP_251101-251130zth.csv  (T15 Master)
├── AN53111387-V-1minRES_43260CLP_251101-251130zth.csv  (T10 Master)
├── AN54021613-V-1minRES_43260CLP_251101-251130zth.csv  (T12 Master)
├── AN54022983-V-1minRES_43260CLP_251101-251130zth.csv  (T16 Master)
└── patterns/  (created later - holds 20 images)
```

**Example:**
`/eeclips/CherryAve/SITE2025/11_NOV2025/`

### Master Files
These become the **Master datasets** - source of truth for all analysis.

---

## Stage 3: Behavior Analysis (eBEHAVIOR.py)

### Execution
```bash
cd /Users/mdhowell/eestream/eBehavior
python eeBEHAVIOR.py
```

### Interactive Questionnaire
eBEHAVIOR asks questions to configure the study:
- Customer name
- Site name
- Analysis period dates
- Number of transformers
- Transformer details (name, capacity, serial number)
- Study naming (date + revision: Study260127r0)

**TODO:** Save previous answers to avoid re-typing

### Automated Processing
eBEHAVIOR performs:
1. **Data refinement** - cleans and improves Master CSV files
2. **Statistical analysis** - calculates metrics, patterns, anomalies
3. **Dashboard generation:**
   - Energy analysis dashboards
   - Heat/thermal analysis dashboards
   - Voltage analysis dashboards
4. **Metadata extraction:**
   - Temperature and humidity data
   - Equipment specifications
   - Operational patterns
5. **Study directory creation** in `/eestream/eReports/Study26xxxxRx/`

### PAUSE POINT: Pattern Images Required

eBEHAVIOR pauses and asks:
```
"Do you have the pattern images ready?"
```

At this point, Summary Dashboard **cannot** be created until pattern images exist.

---

## Stage 4: Pattern Image Creation (eVision_Examine - MANUAL)

### Current Process (Manual - Needs Automation)

#### Tool: eVision_Examine
- **Purpose:** Visualize Master CSV files and capture screenshots
- **Location:** `/eestream/eVision_Examine/` software

#### For Each Transformer (e.g., T10, T12, T15, T16):

**1. Load Refined Master File**
- Open eVision_Examine
- Load Master CSV from `/eeclips/[Customer]/[Site]/[Month]/`
- Use the **refined/improved** version created by eBEHAVIOR

**2. Capture 5 Images Per Transformer**

##### Image Type B - Baseline
- **Filename:** `t10b891.png`
- **Content:** Raw actual energy field behavior
- **Shows:** kVA (dark blue), kW (light blue), kVAR (green), power factor line (orange)
- **Number:** Current power factor (891 = 89.1%)

##### Image Type BT - Baseline Target
- **Filename:** `t10bt891_nov25.png`
- **Content:** Baseline with validated target line
- **Shows:** Blue Supply box target value (e.g., 1103.8 kVA)
- **Purpose:** Performance validation reference

##### Image Type M - MPTS Variables
- **Filename:** `t10m891_nov25.png`
- **Content:** Special configuration showing MPTS sizing data
- **Shows:** KVAR levels, Amperage, sizing markers
- **Purpose:** Determine which MPTS units to deploy (H425, H490, H520, H650)
- **Use:** Attached to Power Factor Circle on Summary Board

##### Image Type S - Solution/Simulator
- **Filename:** `t10s995_nov25.png`
- **Content:** MPTS optimized projection
- **Shows:** What performance looks like WITH Unity equipment installed
- **Number:** Projected power factor after optimization (995 = 99.5%)

##### Image Type V - Voltage
- **Filename:** `t10v891_nov25.png`
- **Content:** First principles voltage view
- **Shows:** Voltage and amperage display, power factor line from top
- **Purpose:** Clean baseline voltage behavior analysis

#### Naming Convention
```
t[transformer#][type][powerFactor]_[month][year].png

Examples:
- t10b891_nov25.png  → Transformer 10, Baseline, 89.1% PF, November 2025
- t12s995_nov25.png  → Transformer 12, Solution, 99.5% PF, November 2025
```

#### Manual Screenshot Process
1. Configure eVision_Examine view settings for image type
2. Take screenshot (goes to default location with random name)
3. **Manually rename** to proper convention
4. Repeat for all 5 views
5. Repeat for all 4 transformers = **20 images total**

**CRITICAL:** Naming must be exact or workflow breaks!

#### Save Location
All 20 images saved to:
```
/eeclips/[Customer]/[Site]/[Month]/patterns/
```

**Example:**
`/eeclips/CherryAve/SITE2025/11_NOV2025/patterns/`

---

## Stage 5: Resume eBEHAVIOR (Pattern Integration)

### Resume Point

```
eBEHAVIOR: "Do you have the pattern images ready?"
User: "Yes"

eBEHAVIOR: "Where are the patterns?"
User: [paste full path to patterns directory]
```

**Example path:**
```
/Users/mdhowell/eeclips/CherryAve/SITE2025/11_NOV2025/patterns
```

### eBEHAVIOR Automated Actions

1. **Validates** all required images present (checks for all 20 files)
2. **Copies** patterns directory → Study folder
3. **Analyzes** pattern images (AI pattern analyzer)
4. **Creates Summary Dashboard** (now has required images)
5. **Generates Unity audio narration** (MP3 files)
6. **Finalizes Study structure**

### Study Directory Output

```
/eestream/eReports/Study260127r0/FosterFarms/CherryAve_Site/
├── Patterns/  ← Copied from eeclips
│   ├── t10b891_nov25.png
│   ├── t10bt891_nov25.png
│   ├── t10m891_nov25.png
│   ├── t10s995_nov25.png
│   ├── t10v891_nov25.png
│   └── [15 more images for T12, T15, T16]
├── Installation/
│   └── unity_system_overview.png
├── T10_narrative.mp3  ← Unity voice narration
├── T12_narrative.mp3
├── T15_narrative.mp3
├── T16_narrative.mp3
├── SITE-FosterFarms-Summaryboard_CherryAve-4_1minRES_251101-251130_30d.html
├── SplitView-energy-*.html  (4 files)
├── SplitView-heat-*.html    (4 files)
├── SplitView-volt-*.html    (4 files)
└── [transformer-specific directories]
```

---

## Stage 6: Study Evaluation & QA

### Review Checklist
- [ ] All dashboards load correctly
- [ ] Pattern images display properly
- [ ] Data accuracy verified against Master files
- [ ] Unity audio narration synchronized
- [ ] Summary calculations correct
- [ ] Visual quality acceptable
- [ ] No broken links or missing resources

### Location
All review happens in: `/eestream/eReports/Study26xxxxRx/`

---

## Stage 7: Deploy to eWebmaster (Staging)

### Process
**Move/copy** approved study from eReports → eWebmaster:

```
/eestream/eReports/Study260127r0/FosterFarms/CherryAve_Site/
    ↓
/eestream/eWebmaster/FosterFarms/CherryAve_Site/
```

### eWebmaster Purpose
- **Website-Portal mirror** (pre-production environment)
- Final staging before live deployment
- Client-facing file organization
- Last chance for corrections

### Final Checks
- [ ] All links functional
- [ ] Images loading correctly
- [ ] Navigation working
- [ ] Customer branding correct
- [ ] Data privacy verified

---

## Stage 8: GitHub Deployment (Production)

### Process
Once eWebmaster staging passes all checks:

1. **Commit** changes to Git repository
2. **Push** to GitHub remote
3. **Deploy** to GitHub Pages (or production server)
4. **Verify** live site functionality
5. **Notify** customer of update

---

## Study Naming Convention

### Format: `Study26xxxxRx`

**Breakdown:**
- `26` = Year (2026)
- `xxxx` = Date (MMDD format, e.g., 0127 = January 27)
- `R` = Revision indicator
- `x` = Revision number (0, 1, 2, 3...)

**Examples:**
- `Study260127r0` = January 27, 2026, revision 0 (first attempt)
- `Study260127r1` = January 27, 2026, revision 1 (second attempt)

**Future Enhancement:**
More descriptive naming planned:
- `FosterFarms_February2026`
- `CherryAve_January2026`

---

## Key Directory Paths

### Data Flow
```
eVision Builder Output:
└── /eestream/eBuilder/eReport/

Master Files (Source of Truth):
└── /eeclips/[Customer]/[Site]/[Month]/

Study Generation:
└── /eestream/eReports/Study26xxxxRx/

Website Staging:
└── /eestream/eWebmaster/[Customer]/[Site]/

Production:
└── GitHub Pages / Live Website
```

---

## Tools & Scripts

| Tool | Location | Purpose |
|------|----------|---------|
| eVision Builder | Cloud application | Extract data from Unity Customer Library |
| eBEHAVIOR.py | `/eestream/eBehavior/` | Main analysis pipeline |
| eVision_Examine | `/eestream/eVision_Examine/` | Pattern image visualization & capture |
| eeINTEGRATE.py | `/eestream/eBehavior/` | Study integration & deployment |

---

## Known Issues & Future Improvements

### Manual Process Pain Points

1. **Pattern Image Naming** (High Priority)
   - Currently: Manual screenshot + manual rename (20 files per study)
   - Future: Automated capture with proper naming

2. **eBEHAVIOR Questionnaire** (Medium Priority)
   - Currently: Re-type all answers every run
   - Future: Save previous answers, pre-populate forms

3. **eVision_Examine View Configuration** (Medium Priority)
   - Currently: Manual configuration switching for each image type
   - Future: Pre-defined view templates, automated switching

4. **Study-to-eWebmaster Transfer** (Low Priority)
   - Currently: Manual copy/move
   - Future: Automated deployment script

---

## Critical Success Factors

### Image Naming
**CRITICAL:** Pattern filenames must be exact or entire workflow breaks
- Power factor codes must match lookup tables
- Month/year suffixes required
- Transformer numbers must be correct

### Data Integrity
- Master files in eeclips are source of truth
- Never modify Master files after eBEHAVIOR refinement
- Always work from refined versions for pattern generation

### Quality Control
- Validate every study before deployment
- Compare to utility bills for accuracy
- Check environmental factors (temperature, humidity)
- Verify MPTS sizing recommendations

---

## Document History

| Date | Author | Changes |
|------|--------|---------|
| 2026-02-05 | Clerk & Mr. Howell | Initial comprehensive workflow documentation |

---

## Related Documentation

- `/Maxwellian/Unity/eStream/eBehavior/WORKFLOW_Full_Analysis_Structure.md`
- `/Maxwellian/Unity/eStream/eBehavior/WORKFLOW_Study_to_Website.md`
- `/eestream/eBehavior/SYSTEM_OVERVIEW.md`
