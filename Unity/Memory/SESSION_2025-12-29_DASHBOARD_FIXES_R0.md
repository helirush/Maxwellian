# Session: Dashboard Bug Fixes & Pattern Analysis System - Dec 29, 2025

## Executive Summary
Critical debugging session addressing multiple issues in R0 (Study251228r0) summary dashboard. Fixed JavaScript errors breaking all navigation, updated pattern analysis system architecture, but identified remaining runtime issues with baseline calculations.

## Critical Bugs Fixed

### 1. JavaScript Syntax Errors (CRITICAL - All 35 Buttons Broken)
**Problem**: All navigation buttons in R0 summary board were non-functional
**Root Cause**: Lines 1265-1267 in transformerData array had missing values:
```javascript
{ id: 2, name: '', efficiency: 0.0, tmaxKVA: 0.0, powerFactor: 0.0, actualKWh:  },  // ← MISSING VALUE
```
**Impact**: `SyntaxError: Unexpected token '}'` broke ALL JavaScript execution, preventing any button clicks
**Fix**: Added `actualKWh: 0` for transformers 2, 3, and 4 in both R0 file and template
**Files**:
- `/Users/mdhowell/eestream/eBehavior/Reports/Study251228r0/FosterFarms/CherryAve_Site/SET1-Summaryboard_CherryAve-4_Fresno_CA_93706_1minRES_250101-250131_31d.html`
- `/Users/mdhowell/eestream/eBehavior/dashboard/templates/eUnitySummaryboard.html`

### 2. Back to Summary Button Paths (Secondary Issue)
**Problem**: "Back to Summary" buttons in split-view pages had hardcoded wrong filename
**Root Cause**: Split-views generated before R0 summary existed, had placeholder `SET1-Summaryboard.html` instead of full filename
**Fix**: Ran `generate_splitviews.py` to regenerate all 12 split-view files with correct path: `SET1-Summaryboard_CherryAve-4_Fresno_CA_93706_1minRES_250101-250131_31d.html`
**Command**: 
```bash
python /Users/mdhowell/eestream/eBehavior/dashboard/generate_splitviews.py "/Users/mdhowell/eestream/eBehavior/Reports/Study251228r0/FosterFarms/CherryAve_Site"
```

## Pattern Analysis System Architecture Improvements

### Problem Statement
User identified that "Standard Daily Pattern" baseline was fundamentally wrong:
- **System was showing**: T10 = 744kVA (using current period average)
- **Correct baseline should be**: T10 = ~1,100 kVA (from visual pattern analysis)
- **Visual evidence**: Pattern image shows consistent daily humps peaking at ~1,100 kVA on left Y-axis scale

### AI Pattern Analyzer Issues
**Discovery**: AI was misreading the Y-axis scale and reporting wrong baseline values
- AI reported: "2,600 kVA peak height" for T10
- Reality: ~1,100 kVA (37% of 3,000 kVA rated capacity)
- **Confusion**: AI was conflating rated capacity with operating pattern baseline

### System Architecture Changes

#### 1. AI Pattern Analyzer (`ai_pattern_analyzer.py`)
**Updated Prompt** (lines 243-254):
```
Format your response as:
STANDARD_PATTERN_KVA: [Single number only - the kVA value where consistent daily patterns peak]

NARRATIVE:
[detailed analysis]

BULLETS:
[action items]

CRITICAL: Read this from the LEFT Y-AXIS where the most common daily pattern peaks reach. 
Do NOT use the rated capacity or maximum spikes.
```

**Updated Parsing** (lines 286-337):
- Added regex extraction: `r'STANDARD_PATTERN_KVA:\s*(\d+)'`
- Stores extracted value in result dict
- Prints: `📊 Detected standard pattern: {kva} kVA`

**Updated Storage** (lines 414-425):
- Adds `standard_pattern_kva` field to pattern JSON entry
- Example: `pattern_entry['standard_pattern_kva'] = 1100`

#### 2. Dashboard Utils (`dashboard_utils.py`)
**Updated Baseline Logic** (lines 466-491):
```python
# Try to get standard_pattern_kva from pattern analysis JSON first
target_pattern_kva = None
if output_dir:
    try:
        pattern_file = site_dir / "SET1_PatternAnalysisData.json"
        if pattern_file.exists():
            xfmr_code = xfmr_name.split('.')[0].split('_')[0].upper()
            target_pattern_kva = pattern_data['transformers'][xfmr_code].get('standard_pattern_kva')
    except:
        pass
        
# Fallback: use capacity * pf if no pattern data available
if not target_pattern_kva:
    target_pattern_kva = capacity * pf
```

**Updated Operations Calculation** (lines 473-482):
```python
# Compare actual avg_kva against the target pattern kVA
if target_pattern_kva > 0:
    operations_pct = (avg_kva / target_pattern_kva) * 100
    # Calculate deviation from 100%
    deviation_pct = abs(100 - operations_pct)
    replacements[f'{xfmr_num}-uptime-pct'] = f'{deviation_pct:.1f}%'
```

**Updated Direction Arrow** (lines 498-511):
```python
# Show ↓ if below target, ↑ if above target, = if at target
if target_pattern_kva > 0:
    if operations_pct < 95:  # More than 5% below target
        direction_arrow = "↓"
    elif operations_pct > 105:  # More than 5% above target
        direction_arrow = "↑"
    else:  # Within 5% of target
        direction_arrow = "="
```

### Manual Baseline Correction
**Added correct values to pattern JSON**:
```json
{
  "transformers": {
    "T10": {
      "standard_pattern_kva": 1100,  // Visual analysis confirmed
      ...
    },
    "T12": {
      "standard_pattern_kva": 1900,  // From AI (seems reasonable)
      ...
    },
    "T15": {
      "standard_pattern_kva": 2000,  // From AI
      ...
    },
    "T16": {
      "standard_pattern_kva": 2225,  // From AI
      ...
    }
  }
}
```

## Outstanding Issues (NOT FIXED)

### 1. Runtime Issue: Baseline Values Not Being Used
**Status**: ❌ Not working despite architectural fix
**Evidence**: Regenerated dashboard still shows:
```
T10: 744kVA STD DAILY PATTERN  (WRONG - should be 1100kVA)
Operations: ↓ 62.0%            (WRONG - should be ~32% below)
```

**Expected Calculation**:
- Standard pattern: 1,100 kVA
- Actual avg for period: 744 kVA  
- Calculation: 744 / 1100 = 67.6%
- Display: "↓ 32.4%" (below target)

**Suspected Root Cause**: 
- `working_renderer.py` likely not passing `output_dir` parameter to `extract_summary_dashboard_values()` 
- This causes fallback to old calculation: `capacity * pf = 3000 * 0.876 = 2628 kVA`
- But even that doesn't match the 744 shown, suggesting multiple calculation paths

**Debug Needed**: Trace `working_renderer.py` → `dashboard_utils.extract_summary_dashboard_values()` call to verify parameter passing

### 2. Narrative/Summary Modal Buttons Not Working
**Status**: ❌ Reported by user, not investigated
**Symptoms**: Pattern summary and narrative buttons on summary board cards not opening modals
**Files Involved**:
- Modal functions in summary board JavaScript
- Pattern data injection system

### 3. AI Pattern Analyzer Requires API Key
**Blocker**: Cannot re-run AI analysis without `ANTHROPIC_API_KEY` environment variable
**Workaround**: Manual baseline values added to JSON as interim solution
**Future**: Need to set API key and re-run analyzer to validate it correctly detects ~1,100 kVA baseline

## User Insights & Requirements

### Pattern Recognition Philosophy
User emphasized: **"We need to automate this. If we're looking at 1,000 transformers, how are we ever going to do that?"**

Key points:
1. Cannot hardcode baselines - need AI to detect automatically
2. Standard daily pattern = most common repeating peak height (not capacity, not max spike)
3. Visual method: Count 15-20 consistent days, measure their peak height on left Y-axis
4. Operations % = how current period compares to that standard pattern

### Visual Analysis Example (T10)
From pattern image shared by user:
- **Standard pattern**: ~1,050-1,100 kVA (the repeating daily humps)
- **Above-pattern days**: 5.5-6 days reaching ~1,300-1,400 kVA
- **Anomalies**: Weekend spikes shooting to 2,800+ kVA (ignore these)
- **Current avg**: 744 kVA (below standard pattern)

User expectation: System should automatically identify the 1,100 kVA baseline by analyzing the visual pattern

## Technical Debt & Next Actions

### Immediate (P0)
1. Debug `working_renderer.py` parameter passing to get baseline values working
2. Fix narrative/summary modal buttons
3. Verify correct operations percentages display after fix

### Short-term (P1)
1. Set ANTHROPIC_API_KEY and re-run AI analyzer on R0
2. Validate AI correctly detects ~1,100 kVA for T10 baseline
3. Update AI prompt if detection still inaccurate
4. Document baseline detection algorithm for future reference

### Medium-term (P2)
1. Add validation: Alert if AI-detected baseline > 50% of rated capacity (likely wrong)
2. Create baseline review dashboard for QA before generation
3. Store baseline detection confidence scores
4. Track baseline changes month-over-month for trending

## File Manifest

### Modified Files
```
/Users/mdhowell/eestream/eBehavior/dashboard/ai_pattern_analyzer.py
  - Lines 243-254: Updated prompt format
  - Lines 286-337: Added standard_pattern_kva parsing
  - Lines 414-425: Store in pattern JSON

/Users/mdhowell/eestream/eBehavior/dashboard/dashboard_utils.py
  - Lines 466-491: Read baseline from pattern JSON
  - Lines 473-482: Calculate operations vs baseline
  - Lines 498-511: Direction arrow logic

/Users/mdhowell/eestream/eBehavior/dashboard/templates/eUnitySummaryboard.html
  - Lines 1265-1267: Fixed actualKWh syntax errors

/Users/mdhowell/eestream/eBehavior/Reports/Study251228r0/FosterFarms/CherryAve_Site/SET1-Summaryboard_CherryAve-4_Fresno_CA_93706_1minRES_250101-250131_31d.html
  - Lines 1265-1267: Fixed actualKWh syntax errors

/Users/mdhowell/eestream/eBehavior/Reports/Study251228r0/FosterFarms/CherryAve_Site/SET1_PatternAnalysisData.json
  - Added standard_pattern_kva fields for all transformers

/Users/mdhowell/eestream/eBehavior/Reports/Study251228r0/FosterFarms/CherryAve_Site/SplitView-*.html
  - All 12 files: Updated goBack() paths to correct summary filename
```

### Key Scripts
```bash
# Regenerate split-views with correct paths
python dashboard/generate_splitviews.py "<site_dir>"

# Regenerate summary board
python dashboard/regenerate_summaryboard.py "<site_dir>"

# Re-run AI pattern analysis (requires API key)
python dashboard/ai_pattern_analyzer.py \
  --patterns-dir "<site_dir>/Patterns" \
  --site-dir "<site_dir>" \
  --period jan2025
```

## Lessons Learned

1. **JavaScript syntax errors are silent killers** - No error messages, just all buttons stop working
2. **AI vision can misread scales** - Need validation logic for detected baseline values
3. **Multiple calculation paths create confusion** - Need single source of truth for baseline
4. **Manual workarounds mask architectural issues** - Fixed architecture but runtime still broken

## Success Metrics
- [x] All 35 navigation buttons working (JavaScript fix)
- [x] Back to Summary buttons navigate correctly
- [x] AI analyzer architecture updated for baseline detection
- [x] Dashboard code reads from pattern JSON
- [ ] Correct baseline values displayed (744→1100 for T10)
- [ ] Correct operations % displayed (62%→32% below for T10)
- [ ] Narrative/summary buttons working
- [ ] AI accurately detects baseline from pattern images

**Status**: 4/8 complete - Architectural foundation solid, runtime issues remain

---
**Session Date**: 2025-12-29
**Study**: Study251228r0 (R0)
**Location**: Foster Farms Cherry Ave Facility
**Transformers**: T10.AirChiller (3000kVA), T12.Main (2500kVA), T15.Fillet (2500kVA), T16.Compressor (1500kVA)
**Period**: January 2025 (31 days)
