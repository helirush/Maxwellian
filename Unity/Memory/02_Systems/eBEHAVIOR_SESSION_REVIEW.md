# eBEHAVIOR.py Session Review & Preparation
**Date**: 2025-11-26 22:28 UTC  
**Status**: ✅ Ready for discussion and potential updates  
**File**: `/Users/mdhowell/eestream/eBehavior/eeBEHAVIOR.py`  

---

## Executive Summary

eeBEHAVIOR.py is the primary integrated energy analysis tool for the eestream system. It orchestrates a complete workflow:

**Raw CSV → ePrep (Stage 1) → eWeather (Stage 2) → eXamine (Stage 3) → E-Stream Ready**

**File Size**: 4,471 lines  
**Status**: ✅ Production-ready  
**Last Modified**: 2025-11-26 (recent updates to core modules)

---

## Current System Architecture

### Three-Stage Pipeline

**Stage 1: ePrep**
- Function: `stage1_eprep(file_path)`
- Purpose: Fill zeros, trim dates
- Output modifications: H/E/R → V (adds 'V' to filename)
- Exit option available

**Stage 2: eWeather**  
- Function: `stage2_eweather(file_path)`
- Purpose: Add temperature and harmonics data
- Sub-functions:
  - `merge_existing_weather()` - Use existing weather data
  - `download_new_weather()` - Download new data
  - `skip_weather_data()` - Skip weather entirely
- Output modifications: add 'th' to filename
- Exit option available

**Stage 3: eXamine**
- Function: `stage3_examine(file_path, customer_info, transformer_name, transformer_size, analysis_dir_path)`
- Purpose: Performance analysis and report generation
- Outputs: Analysis reports, dashboards, metrics

### Final E-Stream Ready Format
```
MeterName-V-resolution_countCLP_startdate-enddatezth.csv
```

---

## Core Module Dependencies

### Imported Modules (from core/)

1. **ePerformance.py** (287 KB - LARGEST)
   - Core performance analysis engine
   - Main analytical calculations
   - Data processing and metrics

2. **voltage_health.py** (83 KB)
   - Voltage analysis and forensics
   - VHI (Voltage Health Index) calculations
   - Voltage deviation detection
   - ⚠️ Status: Recently fixed for NaN handling

3. **ePreparation.py** (21 KB)
   - CSV preparation and cleanup
   - Date trimming
   - Zero filling

4. **eWeather.py** (52 KB)
   - Weather data integration
   - Temperature and harmonics
   - External data downloads

5. **heat_calculations.py** (13 KB)
   - Unity Heat Calculation Model
   - BTU calculations
   - Thermal analysis

6. **eCooling.py** (25 KB)
   - Cooling load calculations
   - HVAC system modeling

7. **quarterly_analysis.py** (16 KB)
   - Quarterly report generation
   - Multi-period analysis

8. **analysis_schema.py** (22 KB)
   - Data schema definitions
   - Structure validation

### Supporting Systems

**Dashboard System** (7 renderer options available)
- `unified_dashboard_generator.py` - ✅ RECOMMENDED (newest, unified API)
- `working_renderer.py` - Field Dashboard renderer (FIELD-Energyboard_*)
- `dashboard_renderer_fixed.py` - Fixed dashboard (DASHBOARD_* files)
- `heat_dashboard_generator.py` - Heat model dashboards
- Legacy siteboard integration (fallback)

**Utilities** (18 modules)
- `eBehaviorOverlayUtils.py` - Motor forensics and chart overlays
- `file_selection.py` - Interactive file selection UI
- `user_input.py` - User interaction management
- `weather_utils.py` - Weather data management
- `thermal_analysis_utils.py` - Thermal calculations
- `utility_billing.py` - Utility billing integration
- `customer_hierarchy.py` - Customer/facility organization
- `file_naming_system.py` - Output filename generation
- `colors.py` - Terminal color formatting

**Optional Integrations**
- Notion API integration (NOTION_AVAILABLE flag)
- Enhanced voltage analysis utilities (OVERLAY_UTILS_AVAILABLE flag)

---

## Recent Changes & Fixes (2025-11-26)

### Dashboard NaN/None Handling Fixes
**Issue**: Energy/Voltage dashboards failing with missing iTHD/harmonics data
- Error: "cannot convert float NaN to integer"
- Error: "unsupported format string passed to NoneType.__format__"

**Files Modified**:
1. `working_renderer.py`
   - NaN-safe int conversions (lines 178-182, 208-288, 505-535, 603-674)
   - Voltage min/max handling
   - Supply/consumption handling
   - Energy waste value handling
   - Heat/cooling/pollution forensic conversions

2. `voltage_dashboard_generator.py`
   - None-safe f-string formatting (lines 267-330)
   - VHI None handling (lines 408-416)

3. `dashboard_utils.py`
   - None-safe replacements (lines 447-457, 484-498)

**Status**: ✅ FIXED - Dashboards now generate with safe fallbacks

### Loader Synchronization (2025-11-26)
- All 6 loaders verified synchronized
- Carbon Credits display unified
- Debug imports standardized
- Timezone-aware datetime parsing confirmed
- Baseline PF checking implemented
- **Status**: ✅ COMPLETE - Production ready

---

## Main Functions Available

### Session Management
- `load_session_state()` - Load previous session data
- `save_session_state(session_data)` - Save current state
- `save_set_summary_to_session()` - Store analysis results
- `get_all_set_summaries_from_session()` - Retrieve all summaries
- `clear_set_summaries_from_session()` - Clear session cache

### User Interaction
- `collect_initial_customer_info()` - Get customer/facility info
- `setup_analysis_directory_and_type()` - Initialize directory structure
- `select_study_level()` - Choose analysis scope (Individual/Set/Domain)
- `get_preparation_preference()` - Ask about data preparation

### Core Processing
- `process_single_file()` - Process one CSV file through pipeline
- `check_file_needs_preparation()` - Check preparation status
- `stage1_eprep()` - Data cleaning and preparation
- `stage2_eweather()` - Weather data integration
- `stage3_examine()` - Analysis and report generation

### Analysis & Reporting
- `analyze_voltage_deviations()` - Voltage quality analysis
- `generate_monthly_voltage_summary()` - Monthly reports
- `generate_quarterly_voltage_summary()` - Quarterly reports
- `generate_set_page2_vault_summary()` - Combined set analysis
- `export_to_notion()` - Export to Notion integration

### Utilities
- `write_to_log()` - Log analysis activities
- `log_session_start()` - Log session initiation
- `log_file_analysis_start()` - Log file processing
- `get_output_format_preference()` - Ask output format
- `get_data_period_from_summaries()` - Extract date ranges

---

## System Capabilities & Features

### Multi-Level Analysis
✅ **Individual Analysis**: Single transformer/meter analysis  
✅ **Set Analysis**: Multiple transformers combined  
✅ **Domain Analysis**: Facility-wide or cross-facility  

### Dashboard Generation
✅ **Energy Dashboards** - Complete energy analysis with gauges  
✅ **Heat Dashboards** - Unity Heat Calculation Model with 7-step analysis  
✅ **Voltage Dashboards** - Voltage health monitoring with critical warnings  
✅ **Site Dashboards** - Facility-level overview  

### Data Handling
✅ **Multi-format input**: CSV with flexible schemas  
✅ **Weather integration**: Temperature and harmonics  
✅ **Billing integration**: Utility cost analysis  
✅ **Session persistence**: Save/load analysis state  

### Advanced Features
✅ **Motor forensics**: Burst pattern detection, HP estimation  
✅ **Thermal modeling**: Heat generation and cooling impact  
✅ **Financial analysis**: Cost-benefit, decay cost modeling  
✅ **Voltage forensics**: Device inference, stress analysis  

---

## Known Issues & Status

### ✅ FIXED
- Dashboard NaN/None formatting errors
- Voltage health analysis with missing iTHD
- Energy/Voltage/Heat dashboard generation

### ⚠️ WARNINGS
- One file >50 MB (GitHub warning, not blocking)
- If using Bank of America data: ensure harmonics column handling

### ✅ OPERATIONAL
- All 6 loaders synchronized
- Production directories clean
- Archive consolidated and verified
- GitHub repository up to date (commit 05c62d4)

---

## Ready for Discussion

### Topics to Cover
1. **Data Source**: What CSV file(s) to analyze?
2. **Analysis Type**: Individual / Set / Domain level?
3. **Customer Info**: Facility name, location, characteristics?
4. **Weather**: Use existing / download new / skip?
5. **Dashboard Preferences**: Energy / Heat / Voltage / All?
6. **Output Format**: Markdown reports / HTML dashboards / Both?
7. **Notion Export**: Export results to Notion? (if NOTION_API_KEY set)

### Typical Workflow
```
1. Start eeBEHAVIOR.py
2. Select study level (Individual/Set/Domain)
3. Provide customer/facility info
4. Select CSV file(s) to analyze
5. Choose preparation preference
6. Confirm weather data handling
7. Select output formats
8. Process files through 3-stage pipeline
9. Generate dashboards and reports
10. Option: Export to Notion
11. Save session state for next time
```

---

## Quick Reference: File Locations

**Main Script**: `/Users/mdhowell/eestream/eBehavior/eeBEHAVIOR.py`

**Core Modules**: `/Users/mdhowell/eestream/eBehavior/core/`  
- ePerformance.py (main analysis)
- voltage_health.py (voltage analysis)
- ePreparation.py (data prep)
- eWeather.py (weather integration)
- heat_calculations.py (thermal model)

**Utilities**: `/Users/mdhowell/eestream/eBehavior/utils/`  
- file_selection.py (file picker)
- user_input.py (UI/interaction)
- weather_utils.py (weather data)
- utility_billing.py (billing)

**Dashboard Renderers**: `/Users/mdhowell/eestream/eBehavior/dashboard/`  
- `unified_dashboard_generator.py` ✅ RECOMMENDED
- working_renderer.py (FIELD-Energyboard)
- dashboard_renderer_fixed.py (Fixed format)
- heat_dashboard_generator.py (Heat models)

**Reports & Output**: `/Users/mdhowell/eestream/eBehavior/reports/`

**Logs**: `/Users/mdhowell/eestream/eBehavior/logs/eeBehavior_analysis.log`

---

## Session State Persistence

Session data stored at: `~/.eeB802_session.json`

Automatically saves:
- Customer/facility information
- Analysis setup preferences
- Set summaries and metrics
- File processing status
- Combined set data

This allows continuing analysis across multiple sessions without re-entering information.

---

## Integration Status

**✅ AVAILABLE:**
- File selection UI (interactive)
- Weather data integration
- Utility billing analysis
- Customer hierarchy management
- Session state persistence
- Dashboard generation (multiple renderers)

**⚠️ OPTIONAL:**
- Notion integration (requires NOTION_API_KEY)
- Enhanced overlay utilities (advanced voltage analysis)
- Notion report export

**ℹ️ INFO:**
- Directory structure manager (transform-centric organization)
- Logging system (full audit trail)
- Color terminal output (better readability)

---

## Recommended Next Steps

1. **Run eeBEHAVIOR.py** with sample data to verify operation
2. **Test data flow** through all 3 stages
3. **Generate dashboards** and verify rendering
4. **Check dashboard** output for accuracy
5. **Review any** specific analysis needs or customizations
6. **Discuss** findings and next phase improvements

---

## For Discussion

**What would you like to:**
1. Analyze a specific dataset?
2. Test a particular feature or workflow?
3. Debug or fix something specific?
4. Enhance or customize the system?
5. Review recent changes or verify functionality?

I'm ready whenever you want to proceed!

---

**Status**: ✅ REVIEWED AND READY  
**Last Updated**: 2025-11-26 22:30 UTC  
**Archive Commit**: 05c62d4 (helirush/eestream)  
**System Status**: All systems operational
