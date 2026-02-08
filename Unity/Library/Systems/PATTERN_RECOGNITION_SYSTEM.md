# Pattern Recognition & Visual Energy Field Analysis

**Category:** System Architecture & Algorithm Specification  
**Status:** Production Active ✅  
**Last Updated:** 2025-12-14  
**Implementation:** `/eBehavior/dashboard/pattern_image_processor.py`, `/eBehavior/dashboard/pattern_analysis_manager.py`

---

## Overview

The Pattern Recognition System enables rapid behavioral analysis of electrical energy fields by extracting and interpreting visual patterns from time-series energy charts. This system allows plant managers and CFOs to quickly understand transformer behavior without deep technical analysis.

### Key Insight
When energy field data is confined to a specific time period (e.g., one month), repetitive behavioral patterns become visually recognizable. These patterns correlate with:
- **Time** - Daily, weekly, monthly cycles
- **Quantity** - Load magnitudes and consumption levels
- **Operations** - Production schedules, equipment cycling

By capturing these pattern observations, we can populate the Summary Dashboard with actionable intelligence that executives can consume in seconds.

---

## System Architecture

### 1. Screenshot Capture & Validation

**Location:** `Patterns/` directory within analysis period folder  
**Format:** PNG screenshots of transformer energy field charts

**Validation Pipeline:**
```
Screenshot → Extract Bottom Metadata → Validate Meter ID → Validate Period → Accept/Reject
```

#### Validation Steps:
1. **Meter ID Extraction**
   - Parse bottom timestamp text: `AN53111387-V : 1min : 44640slices : 01/01/25 00:00 to 01/31/25 23:59`
   - Extract meter base ID: `AN53111387`

2. **Library Cross-Reference**
   - Look up meter in `/eVision/common/library.py`
   - Map to transformer: `AN53111387` → `Cherry-T10 AIR CHILLER`
   - Extract code: `T10`
   - **Gatekeeper:** Reject if meter not in library (not actively streaming)

3. **Period Validation**
   - Extract date range from bottom timestamp
   - Compare against expected analysis period (e.g., `Jan2025`)
   - Validate month and year match
   - **Gatekeeper:** Reject if period mismatch detected

#### Example: Valid Screenshot
```
Meter: AN53111387-V
Library Match: Cherry-T10 AIR CHILLER, Fresno,CA
Transformer: T10
Date Range: 01/01/25 00:00 to 01/31/25 23:59
Expected: Jan2025
Status: ✅ VALID
```

#### Example: Invalid Screenshot
```
Meter: AN64021613-V
Library Match: (NOT FOUND)
Date Range: 10/01/25 00:00 to 10/31/25 23:59
Expected: Jan2025
Status: ❌ INVALID (meter not in library + wrong period)
```

---

### 2. Pattern Interpretation

**Visual Analysis Elements:**
- Load cycling patterns (daily, weekly, monthly)
- Peak demand timing and consistency
- Baseload vs variable load behavior
- Weekend vs weekday differences
- Seasonal operational characteristics

**Pattern Description Format:**
- Concise (1-2 sentences)
- Action-oriented language
- Quantitative where possible
- Production-relevant context

**Example Patterns:**

**T10 Air Chiller:**
```
5-day production cycle. Weekday peaks ~2700 kW, weekend lows ~300 kW. 
Consistent air chiller operations supporting production schedule.
```

**T12 Main:**
```
24/7 continuous base load ~1200 kW with weekday production spikes to 1800 kW. 
Facility core infrastructure with processing overlay.
```

**T15 Fillet:**
```
Highly variable 5-day cycle. Peak demands 1600 kW during processing shifts. 
Near-zero consumption weekends. Production-driven field.
```

---

### 3. Data Storage

**File:** `SET1_PatternAnalysisData.json`  
**Location:** Site output directory (e.g., `/Reports/Study251213r4/FosterFarms/CherryAve_Site/`)

**Structure:**
```json
{
  "last_updated": "2025-12-14T08:30:00",
  "analysis_period": "Jan2025",
  "transformers": {
    "T10": {
      "pattern_interpretation": "5-day production cycle. Weekday peaks...",
      "last_analyzed": "2025-12-14T08:30:00"
    },
    "T12": {
      "pattern_interpretation": "24/7 continuous base load...",
      "last_analyzed": "2025-12-14T08:30:00"
    }
  }
}
```

**Management:** `PatternAnalysisManager` class handles read/write operations

---

### 4. Dashboard Integration

**Summary Dashboard Display:**
- Pattern text appears on each transformer card
- Positioned below production metrics
- Provides immediate behavioral context
- Enables quick executive-level understanding

**User Experience Flow:**
1. Executive opens Summary Dashboard
2. Sees 4 transformer cards with metrics + patterns
3. Gets complete operational picture in <30 seconds
4. Can click energy field circle to dive deeper if needed

**Target Audience:**
- Plant Managers (daily operations review)
- CFOs (monthly financial review)
- Energy Managers (optimization opportunities)
- Operations Directors (capacity planning)

---

## Universal Design

### Flexibility Features:

**Any Number of Transformers:**
- System auto-detects transformers from `dashboard_data_*.json` files
- Works with 1, 4, 8, 12, or any count
- Validates screenshot count against analysis

**Any Naming Scheme:**
- T10, T12, T15, T16 (Foster Farms)
- TR-A, TR-B, TR-C (generic)
- Unit1, Unit2 (numbered)
- Substation-North, Substation-South (descriptive)

**Any Facility:**
- Cross-references library.py for meter mappings
- Only accepts meters actively being streamed
- Rejects meters not in current configuration

---

## Implementation Files

### Core Modules:

**`pattern_image_processor.py`**
- Screenshot validation pipeline
- Meter ID extraction and library lookup
- Period validation from bottom timestamps
- Transformer identification
- OCR capabilities (when available)

**`pattern_analysis_manager.py`**
- JSON data persistence
- Pattern CRUD operations
- Multi-transformer batch updates
- Timestamp management

**`manual_validate_screenshots.py`**
- Interactive validation tool
- User-guided meter ID entry
- Date validation
- Validation reports

### Integration Points:

**`dashboard_utils.py`**
- Loads pattern data during dashboard generation
- Passes patterns to template renderer

**`working_renderer.py`**
- Injects pattern data into HTML templates
- Handles missing patterns gracefully

**Template: `eUnitySummaryboard.html`**
- Displays pattern text on transformer cards
- Positioned in production metrics section

---

## Workflow

### Pattern Capture Process:

```
1. Run energy analysis (eeBEHAVIOR.py)
2. Generate energy field charts
3. System checks for Patterns/ directory
4. If not exists, create and prompt user to capture screenshots
5. User captures transformer energy field screenshots
6. User selects "Continue" when ready
7. System validates all screenshots:
   - Extract meter IDs
   - Cross-reference library.py
   - Validate periods
   - Identify transformers
8. User reviews validation report
9. For valid screenshots, user enters/confirms pattern interpretations
10. System saves patterns to SET1_PatternAnalysisData.json
11. Dashboard generation proceeds
12. Patterns appear on Summary Dashboard automatically
```

### Validation Workflow:

```bash
# Manual validation tool
python manual_validate_screenshots.py \
  /path/to/Patterns \
  /path/to/site_output \
  Jan2025
```

**Interactive prompts:**
- User views each screenshot
- Reads bottom timestamp
- Enters meter ID
- Enters date range
- System validates and provides immediate feedback

---

## Benefits

### Executive Level:
- **Speed:** Understand monthly operations in <30 seconds
- **Context:** See beyond numbers to behavioral patterns
- **Actionable:** Identify optimization opportunities quickly
- **Accessible:** No technical expertise required

### Technical Level:
- **Universal:** Works across all facilities and configurations
- **Validated:** Gatekeeper ensures data quality
- **Automated:** Minimal manual intervention once configured
- **Scalable:** Handles any transformer count

### Business Level:
- **ROI:** Faster decision-making on energy investments
- **Efficiency:** Reduced time spent in data analysis meetings
- **Compliance:** Documented behavioral patterns for audits
- **Planning:** Better capacity and operations forecasting

---

## Technical Notes

### Meter ID Format:
- Base: `AN53111387` or `AM18040454`
- Full: `AN53111387-V` (with voltage designation)
- System strips suffix for library lookup

### Date Format:
- Screenshots: `MM/DD/YY` (e.g., `01/01/25`)
- Expected: Month name + year (e.g., `Jan2025`)
- Validation: Matches month and year components

### Library.py Structure:
```python
energy_fields = {
    "AN53111387m1 : Cherry-T10 AIR CHILLER, Fresno,CA - c.240323": "/path/to/data",
    "AN54021613m1 : Cherry-T12 MAIN, Fresno,CA - c.240412": "/path/to/data",
    ...
}
```

### Pattern Storage:
- One JSON file per site
- Cumulative across analysis runs
- Timestamps track updates
- Old patterns preserved until overwritten

---

## Future Enhancements

### Planned:
- [ ] Full OCR automation (eliminate manual entry)
- [ ] ML-based pattern classification
- [ ] Comparative analysis (month-over-month)
- [ ] Anomaly detection from pattern deviations
- [ ] Automatic pattern generation from time-series

### Under Consideration:
- [ ] Pattern confidence scoring
- [ ] Multi-language pattern descriptions
- [ ] Voice-to-text pattern capture
- [ ] Pattern templates library

---

## Use Cases

### Monthly Executive Review:
"Show me what happened last month across all transformers"
→ Summary Dashboard with 4 pattern observations
→ Complete picture in 30 seconds

### Energy Optimization:
"Which transformers have optimization potential?"
→ Patterns reveal cycling inefficiencies
→ Target T15 for demand response program

### Capacity Planning:
"Can we add a new production line?"
→ Patterns show weekend low utilization
→ Available capacity identified

### Maintenance Scheduling:
"When can we do transformer maintenance?"
→ Pattern reveals consistent weekend lows
→ Schedule maintenance without production impact

---

## References

- Implementation: `/eBehavior/dashboard/pattern_*.py`
- Meter Library: `/eVision/common/library.py`
- Dashboard Templates: `/eBehavior/dashboard/templates/`
- Customer Hierarchy: `customerHierarchySystem.md`

---

**Maintainer:** MD Howell, Unity Energy LLC  
**Version:** 1.0  
**Date:** 2025-12-14
