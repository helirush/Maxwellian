# Quick Reference - Unity Energy eestream System

---
**File**: `quickref.md`  
**Tag**: `eMemory.knowledge.reference.quickstart`  
**Category**: 03_Knowledge  
**Agent**: COLLABORATIVE  
**Created**: 2025-10-16  
**Last Updated**: 2025-10-29  
**Status**: ACTIVE  
**Importance**: MEDIUM  
**Related**: `systemPatterns.md`, `techContext.md`, `AGI_CALIBRATION.md`  
---

## One-Page Cheat Sheet for Common Operations

---

## File Naming Conventions

### Dashboard Files
```
Format: {PREFIX}-{TYPE}_{BASENAME}_{RESOLUTION}_{DATES}_{DURATION}.html

FIELD-Energyboard_T10.AirChiller_AN53111387_1minRES_250101-250331_90d.html
SET1-Summaryboard_CherryAve-4_1minRES_250901-250930_30d.html
SITE-Voltboard_FosterFarms_1minRES_250101-250630_180d.html
```

**Prefixes**:
- `FIELD-` = Individual transformer dashboard
- `SET{N}-` = Combined facility analysis (multiple transformers)
- `SITE-` = Multi-set domain intelligence

**Types**:
- `Energyboard` = Complete energy analysis with gauges
- `Heatboard` = Unity Heat Calculation Model (7 steps)
- `Voltboard` = Voltage health monitoring
- `Summaryboard` = Executive overview (up to 4 transformers)

### Report Files
```
Format: {PREFIX}p{PART}-{CATEGORY}_{DESCRIPTOR}_{RESOLUTION}_{DATES}_{DURATION}.md

FIELDp1-EnergyHealth_T10.AirChiller_AN53111387-1minRES_250101-250331_90d.md
FIELDp2-VoltageHealth_T10.AirChiller_AN53111387-1minRES_250101-250331.md
SETp1-EnergySummary_CherryAve-4_1minRES_250901-250930_30d.md
```

**Report Types**:
- `p1` = Energy Health Analysis
- `p2` = Voltage Health Analysis

---

## Directory Structure

### Single Transformer Analysis
```
Reports/STUDY.{date}.{desc}/
└── TRANSFORMER_{name}/
    ├── FIELD-Energyboard_*.html
    ├── FIELD-Heatboard_*.html
    ├── FIELD-Voltboard_*.html
    ├── FIELD-Summaryboard_*.html
    ├── FIELDp1-EnergyHealth_*.md
    └── FIELDp2-VoltageHealth_*.md
```

### Multi-Transformer Analysis
```
Reports/STUDY.{date}.{desc}/
├── TRANSFORMER_T10.AirChiller/
│   └── [FIELD-* files]
├── TRANSFORMER_T12.Main/
│   └── [FIELD-* files]
└── SITE_{facility_name}/
    ├── SET1-Energyboard_*.html
    ├── SET1-Heatboard_*.html
    ├── SET1-Voltboard_*.html
    ├── SET1-Summaryboard_*.html
    ├── SETp1-EnergySummary_*.md
    └── SETp2-VoltageSummary_*.md
```

---

## Common Commands

### Run Main Analysis
```bash
cd /Users/mdhowell/eestream/eBehavior
python eeBEHAVIOR.py
```

### Launch Visual Interface
```bash
cd /Users/mdhowell/eestream/eVision
streamlit run eeVISION.py
```

### Generate Audio from Dialogue
```bash
cd /Users/mdhowell/eestream/eAudio
python eMultiVoiceTTS.py UNITYCompany-Audios/EpisodeStory/{file}.txt output.mp3
```

**⚠️ Text File Format Requirement**:
- All text files MUST use the format: `[Speaker] dialogue text`
- Each line needs a speaker tag in brackets: `[Narrator]`, `[Host]`, `[Expert]`, etc.
- Example:
  ```
  [Narrator] This is the introduction.
  [Narrator] This is the next paragraph.
  [Expert] This is a quote from an expert.
  ```

### Verify Dashboard Bindings
```bash
cd /Users/mdhowell/eestream/eBehavior/dashboard
python verify_{type}_bindings.py  # type = heat, volt, energy
```

---

## Analysis Level Selection

### Level 1: Individual Transformer Focus
- **Output**: FIELD dashboards + reports in transformer directory
- **Use Case**: Single transformer deep-dive, operational monitoring
- **Files Generated**: 4 FIELD dashboards + 2 FIELD reports

### Level 2: Set Analysis (Combined Facility)
- **Output**: FIELD dashboards per transformer + SET dashboards for facility
- **Use Case**: Facility-wide energy analysis, multiple transformers
- **Files Generated**: FIELD files per transformer + SET files in SITE directory
- **Note**: If only 1 transformer, behaves like Level 1 + FIELD-Summaryboard

### Level 3: Domain Intelligence
- **Output**: Full Level 2 output + strategic quarterly/annual analysis
- **Use Case**: Executive reporting, long-term trends, ROI analysis
- **Files Generated**: All Level 2 files + domain intelligence reports

---

## Dashboard Types

### Energyboard (Primary Dashboard)
**Content**:
- 7 interactive gauges: iTHD, Voltage, Power Factor, Amperage, Capacity, Supply, Consumption
- Electricity Cost & Consumption panels
- 4 Forensics cards: Heat, Cooling, Pollution, Voltage Health

**Use For**: Complete energy overview, executive presentation

### Heatboard (Thermal Analysis)
**Content**:
- Energy Waste - Heat Metrics
- Total Electrical Thermal Burden
- 7-Step Heat Calculation Process
- Model Input Parameters

**Use For**: HVAC optimization, cooling cost analysis

### Voltboard (Voltage Quality)
**Content**:
- Voltage deviation analysis
- Critical warnings system
- G8 motor stress calculations
- Time-series voltage health charts

**Use For**: Equipment protection, voltage issue forensics

### Summaryboard (Executive Overview)
**Content**:
- Up to 4 transformer cards with Power Factor gauges
- Energy wasted percentage
- Above/Below target analysis
- Cost per hour breakdown

**Use For**: Quick facility overview, multi-transformer comparison

---

## Template ID Binding Pattern

### HTML Template
```html
<span id="metric-value">—</span>
<div id="gauge-reading">0.0</div>
```

### Python Generator
```python
replacements = {
    'metric-value': f"{calculated_value:,.0f}",
    'gauge-reading': f"{gauge_value:.2f}"
}

html_content = update_html_by_ids(
    html_content=template,
    replacements=replacements
)
```

**Rules**:
- Always use `update_html_by_ids()` from `dashboard_utils`
- Match ID names exactly (case-sensitive)
- Verify 100% binding coverage with verification scripts
- Never hardcode values in templates

---

## Three-Stage Processing Pipeline

### Stage 1: E-Preparation (ePrep)
```
Input:  raw_file.csv
Process: Fill zeros, trim dates, standardize format
Output: raw_file_V_z.csv
```

### Stage 2: E-Weather (eWeather)
```
Input:  raw_file_V_z.csv
Process: Merge weather data, add synthetic harmonics
Output: raw_file_V_z_th.csv
```

### Stage 3: E-Examine (eBehavior)
```
Input:  raw_file_V_z_th.csv
Process: Analysis, dashboard generation, report creation
Output: Dashboards + Reports in organized directories
```

---

## Configuration Management

### API Keys Location
```
/Users/mdhowell/eestream/eConfig/.env
```

### Required Keys
```bash
OPENAI_API_KEY=sk-...
ELEVENLABS_API_KEY=...  # Optional
NOTION_API_KEY=...      # Optional
```

### Loading Configuration
```python
from eConfig.config_loader import load_config
config = load_config()
api_key = config['OPENAI_API_KEY']
```

---

## Common Data Validations

### Check Column Count
```python
expected_cols = 38
if len(df.columns) != expected_cols:
    print(f"⚠️ Unexpected columns: {len(df.columns)} (expected {expected_cols})")
```

### Check for None Values
```python
if value is None and can_calculate:
    value = calculate_from_available_data()
```

### Validate Date Range
```python
if pd.isna(df['Time']).any():
    print("⚠️ Missing timestamps detected")
```

---

## CSS Naming Conventions

### Dashboard Components
```css
.transformer-card    /* Individual transformer display */
.gauge-container     /* Gauge wrapper with Unity styling */
.stats               /* Metrics display under gauges */
.forensics-card      /* Analysis cards (Heat, Cooling, etc.) */
```

### Unity Color System
```css
--unity-green: #B2D235;
--unity-dark-green: #8BA028;
--gauge-gold: #FFD700;
--critical-red: #FF4444;
--warning-yellow: #FFD54F;
```

---

## JavaScript Pattern

### CleanRebuildConnector Class
```javascript
class CleanRebuildConnector {
    constructor() {
        this.loadData();
    }
    
    loadData() {
        // Fetch and integrate data
    }
    
    updateGauges() {
        // Refresh gauge displays
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new CleanRebuildConnector();
});
```

---

## Voice Selection (eAudio)

### OpenAI TTS Voices
- **alloy** - Neutral, versatile
- **echo** - Warm, authoritative
- **fable** - Expressive, storytelling
- **onyx** - Deep, professional
- **nova** - Clear, energetic (recommended for Unity)
- **shimmer** - Bright, friendly

### ElevenLabs Voices (Premium)
- **Unity** - Custom trained voice
- **Chris** - Professional male
- **Michael** - Authoritative male

---

## Debugging Checklist

When dashboards show placeholder dashes or errors:

1. ✅ Verify function exists and is imported correctly
2. ✅ Check parameter names match function signature
3. ✅ Confirm using correct generator (working_renderer vs old versions)
4. ✅ Run verification script to check binding coverage
5. ✅ Inspect console output for calculation messages
6. ✅ Check browser console for JavaScript errors
7. ✅ Validate data files have expected format (column count, date range)

---

## Critical Reminders

⚠️ **Always check dataset count before creating directories**
```python
if len(analysis_summaries) == 1:
    # Single dataset - skip SET/SITE structure
```

⚠️ **Verify function existence before calling**
```python
from module import function_name  # Verify this succeeds
```

⚠️ **Match parameter names exactly**
```python
func(html_content=x, replacements=y)  # Not html= and data=
```

⚠️ **Never hardcode template values**
```html
<span id="dynamic-value"></span>  <!-- Not: <span>123</span> -->
```

⚠️ **Run verification scripts after changes**
```bash
python verify_dashboard_bindings.py
```

---

## Getting Help

### Documentation
- `eMemory/activeContext.md` - Current work and recent changes
- `eMemory/systemPatterns.md` - Architecture and design patterns
- `eMemory/decisions.md` - Why we made key decisions
- `eMemory/antipatterns.md` - What NOT to do
- `eMemory/techContext.md` - Technologies and setup

### Logs and Debugging
- Console output shows calculation messages and binding info
- Browser console (F12) shows JavaScript errors
- Generated files in `Reports/STUDY.{date}.{desc}/`

### Common Issues
- **Placeholder dashes** → Wrong generator function or missing bindings
- **Function not found** → Check imports and function names
- **Wrong directory structure** → Check dataset count before creating dirs
- **Missing FIELD-Summaryboard** → Ensure single-dataset path generates it

---

**Last Updated**: October 29, 2025  
**Version**: 1.0
