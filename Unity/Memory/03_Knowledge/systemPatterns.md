# System Patterns - Unity Energy eestream System

---
**File**: `systemPatterns.md`  
**Tag**: `eMemory.knowledge.patterns.architecture`  
**Category**: 03_Knowledge  
**Agent**: COLLABORATIVE  
**Created**: 2025-10-16  
**Last Updated**: 2025-10-29  
**Status**: ACTIVE  
**Importance**: HIGH  
**Related**: `techContext.md`, `antipatterns.md`, `quickref.md`, `decisions.md`  
---

## System Architecture

### Modular Four-Component Architecture
The eestream system follows a **modular service architecture** with four specialized components that work independently but integrate seamlessly:

```
eestream/
├── eBehavior/    # Core Analysis Engine (Primary)
├── eVision/      # Visual Interface Layer
├── eAudio/       # Audio Processing Service  
├── eMarket/      # Economic Analysis Module
└── eConfig/      # Centralized Configuration
```

### Data Flow Architecture
**Pipeline Pattern**: Raw CSV → Processing Stages → Multiple Output Formats
```
Raw CSV Data
    ↓ (ePreparation)
Zero-filled, Date-trimmed Data  
    ↓ (eWeather Integration)
Weather-enhanced Data
    ↓ (eBehavior Analysis)
Comprehensive Analysis Results
    ↓ (Dashboard Generation)
Interactive HTML Dashboards + Markdown Reports
```

## Key Technical Decisions

### 1. Unified Dashboard System (2025 Architecture)
**Decision**: Single API generates three specialized dashboard types
- **Templates**: `eUnityEnergyboard.html`, `eUnityHeatboard.html`, `eUnityVoltboard.html`, `eUnitySiteboard.html`
- **Generator**: `unified_dashboard_generator.py` with smart parameter replacement
- **Naming Convention**: 
  - Individual: `FIELD-{Type}board_{Transformer}_{AN}_{DateRange}.html`
  - Set Level: `SET{N}-{Type}board_{SiteName}_{Resolution}_{DateRange}.html`
  - Site Level: `SITE-{Type}board_{SiteName}_{Resolution}_{DateRange}.html`

**Standardization Rules** (October 2025):
- ✅ No location suffix in middle of filename (removed `_Site` pattern)
- ✅ Single-set analyses use SET1 prefix only (no duplicate SITE generation)
- ✅ Multi-set analyses generate both SET and SITE summaryboards
- ✅ Clean format: `{prefix}-{type}_{basename}_{resolution}_{dates}.html`

**ID Binding Standardization** (October 2025):
- ✅ HTML template IDs match exactly with working_renderer.py mappings
- ✅ Electricity Cost Panel: `site-cost-per-kwh`, `site-transformer-cost`, `site-transformer-cost-pct`, `site-domain-cost`, `site-total-cost`
- ✅ Electricity Consumption Panel: `site-transformer-consumption`, `site-transformer-consumption-pct`, `site-domain-consumption`, `site-total-consumption`
- ✅ Transformer Name: Multiple `id="xfmr-name"` elements consistently populated
- ✅ 480v Domain Cost: Automatically calculated from site percentage instead of showing "n/a"

**Heat Dashboard Systematic Fix** (October 2025):
- ❌ **Problem**: Heat dashboards showed all placeholder dashes (`—`) instead of calculated values
- 🔍 **Root Cause**: System was calling `generate_heat_model_dashboard()` from old heat_dashboard_generator.py instead of proper working renderer
- ✅ **Solution Applied**: Systematic binding verification and function call fix
- ✅ **Import Fix**: Updated to use `generate_heat_dashboard_for_analysis` from working_renderer.py with alias `generate_heat_dashboard`
- ✅ **Verification Script**: Created `verify_heat_bindings.py` - shows 100% binding coverage (41/41 IDs bound)
- ✅ **Template Bindings**: All Heat dashboard sections now fully dynamic:
  - Energy Waste - Heat Metrics (8 fields): `metric-energy-waste`, `metric-v-avg`, `metric-pf`, `metric-thd-current`, `metric-field-heat`, `metric-device-heat`, `metric-electrical-heat`, `metric-waste-offset`
  - Total Thermal Burden (3 fields): `result-energy-burden`, `result-heat-burden`, `result-cooling-burden`
  - Model Input Parameters (8 fields): `param-transformer-name`, `param-ac-exposure`, `param-climate-index`, `param-btu-conversion`, `param-kwh-rate`, `param-vhi-multiplier`, `param-hhi-multiplier`, `param-eer-multiplier`
  - Energy Field Heat Intelligence (21 calculation fields): `calc-step1-baseline` through `calc-step7-result` with detailed 7-step heat calculation process
- ✅ **Power Factor Fix**: Updated renderer to display power factor as percentage (85.0%) instead of decimal (0.85)
- 📋 **Process**: Same systematic approach as Volt dashboard - identify binding system → fix function calls → verify 100% coverage → test

**Rationale**: Eliminates code duplication, ensures consistency, prevents duplicate files, provides clear naming hierarchy

### 2. Transformer-Centric Organization
**Decision**: Directory structure follows Facility → Site → Transformer hierarchy
```
reports/STUDY.{date}.{period}/TRANSFORMER_{name}/
├── FIELD-Energyboard_{transformer}_{an}_{dates}.html
├── FIELD-Heatboard_{transformer}_{an}_{dates}.html
└── FIELD-Voltboard_{transformer}_{an}_{dates}.html
```

**Rationale**: Matches industrial organizational structure, simplifies navigation

### 3. Configuration Centralization
**Decision**: All API keys and configuration in `eConfig/` module
- **Single Source**: `.env` file with standardized variable names
- **Cross-Module**: All components use `eConfig/config_loader.py`
- **Security**: Git-ignored `.env` with `.env.example` template

**Rationale**: Reduces configuration drift, improves security, simplifies deployment

## Design Patterns

### 1. Template Method Pattern (Dashboard Generation)
**Implementation**: `unified_dashboard_generator.py`
```python
def generate_dashboard(self, dashboard_type, transformer_data, output_path):
    # Template method with configurable steps
    template = self.load_template(dashboard_type)
    processed_data = self.process_data(transformer_data)
    filled_template = self.replace_parameters(template, processed_data)
    self.save_dashboard(filled_template, output_path)
```

### 2. Builder Pattern (Analysis Pipeline)
**Implementation**: `eeBEHAVIOR.py` main workflow
```python
# Step-by-step construction of analysis
analysis = (EnergyAnalysis()
    .load_data(csv_path)
    .apply_preparation()
    .integrate_weather()
    .calculate_behavior()
    .generate_reports()
    .create_dashboards())
```

### 3. Strategy Pattern (Multiple Output Formats)
**Implementation**: Different renderers for different output types
- **HTML Dashboards**: Interactive with live data integration
- **Markdown Reports**: Technical documentation format
- **CSV Exports**: Processed data for further analysis

### 4. Observer Pattern (AI Assistant Integration)
**Implementation**: `eVision/` digital assistants respond to analysis events
- **Unity Assistant**: Primary technical analysis
- **Nikki Assistant**: User experience and guidance
- **Graham Assistant**: Economic analysis and reporting

## Component Relationships

### Core Dependencies
```
eBehavior (Core) ←── eVision (UI)
    ↓                    ↓
eAudio (Voice) ←── eMarket (Economics)
    ↑
eConfig (Configuration Hub)
```

### Data Relationships
1. **eBehavior** generates analysis data consumed by all other modules
2. **eVision** provides interactive interface to eBehavior functions
3. **eAudio** processes text output from eBehavior/eVision into voice
4. **eMarket** performs economic analysis on eBehavior results
5. **eConfig** provides configuration to all modules

### Integration Points
- **CSV Data**: Standard format processed by eBehavior, visualized by eVision
- **Analysis Results**: JSON/dict format shared between all modules
- **Dashboard Templates**: HTML templates with parameter replacement
- **Report Generation**: Markdown format with embedded data

## Critical Implementation Paths

### 1. Main Analysis Workflow (eBehavior)
**Critical Path**: `eeBEHAVIOR.py` → Three-Stage Pipeline → Multi-Level Reports → Dashboard Generation
```python
# Primary execution path
main() → collect_initial_customer_info() → setup_analysis_directory_and_type() → 
select_files_for_processing() → process_single_file() → 
[stage1_eprep() → stage2_eweather() → stage3_examine()] → 
generate_dashboards() → create_reports() → organize_outputs()
```

**Three-Stage Processing Pipeline**:
```python
# Stage 1: E-Preparation
stage1_eprep() → fill_zeros() → trim_dates() → rename_with_V_and_z_suffix()

# Stage 2: E-Weather  
stage2_eweather() → [merge_existing_weather() OR download_new_weather() OR skip_weather_data()] 
                  → add_synthetic_harmonics() → rename_with_th_suffix()

# Stage 3: E-Examine
stage3_examine() → analyze_transformer_data() → generate_field_dashboards() → 
                 → generate_heat_voltboards() → create_individual_reports()
```

**Multi-Level Study System**:
- **Level 1**: Individual transformer reports only
- **Level 2**: Individual + Combined Set reports
- **Level 3**: Individual + Set + Domain intelligence reports (quarterly/annual)

### 2. Dashboard Generation Pipeline
**Critical Path**: Template loading → Parameter replacement → File generation
```python
# Dashboard creation flow
load_template() → extract_transformer_data() → 
replace_parameters() → validate_output() → save_file()
```

### 3. Voltage Health Analysis (Advanced Feature)
**Critical Path**: Voltage data → Health scoring → Critical warnings → Dashboard integration
```python
# Voltage analysis flow
voltage_data → health_calculation() → g8_motor_analysis() → 
warning_generation() → dashboard_integration()
```

### 4. Report Organization System
**Critical Path**: Analysis completion → Directory creation → File placement → Index generation
```python
# Organization flow
analysis_complete → create_directory_structure() → 
place_files() → generate_indices() → update_metadata()
```

## System Integration Patterns

### 1. Configuration Management
**Pattern**: Centralized configuration with environment-specific overrides
- **Default Values**: Built into each module
- **Environment Variables**: Override defaults via `.env`
- **Runtime Configuration**: API-based updates for dynamic settings

### 2. Error Handling Strategy
**Pattern**: Graceful degradation with detailed logging
- **Critical Errors**: Stop processing with clear error messages
- **Warning Conditions**: Continue processing with notifications
- **Data Issues**: Auto-correction with user notification

### 3. Output Validation
**Pattern**: Multi-stage validation with rollback capability
- **Template Validation**: Ensure parameters are properly replaced
- **Data Validation**: Verify all required fields are present
- **File Validation**: Confirm output files are complete and readable

### 4. Extension Architecture
**Pattern**: Plugin-ready architecture for future enhancements
- **Module Interface**: Standardized API for new analysis modules
- **Template System**: Easy addition of new dashboard types
- **Data Processors**: Pluggable data transformation components

This architecture enables the eestream system to provide comprehensive industrial energy analysis while maintaining modularity, reliability, and extensibility for future enhancements.

## Recent Lessons Learned (October 2025)

### Voltage Dashboard Generator Fix (October 27, 2025)
**Problem**: Voltage dashboards (Voltboard) were not generating due to undefined function error
```
❌ Error generating voltage model dashboard: name 'apply_data_bindings' is not defined
```

**Root Cause**: 
1. Function `apply_data_bindings()` was being called but didn't exist in codebase
2. Comment on line 588 indicated it was "removed/refactored"
3. Wrong parameter names used: `html` and `data` instead of `html_content` and `replacements`

**Solution Applied**:
```python
# Fixed in: dashboard/generators/voltboard_generator.py (lines 812-815)
# BEFORE:
customized_template = apply_data_bindings(
    html=customized_template,
    data=canonical_data,
    trace_mode=False
)

# AFTER:
customized_template = update_html_by_ids(
    html_content=customized_template,
    replacements=canonical_data
)
```

**Key Insights**:
- ✅ Always verify function existence before calling
- ✅ Match parameter names exactly to function signature
- ✅ Check imports and available functions from imported modules
- ✅ `update_html_by_ids` is the correct function from `dashboard_utils`

### Single Dataset Analysis Optimization (October 27, 2025)
**Problem**: When analyzing only 1 transformer in Level 2/3 mode, system created unnecessary directory structure:
- Created `SITE_Foster_Farms__Cherry_Ave_Facility/` directory
- Generated redundant SET1-* files (Energyboard, Heatboard, Voltboard, Summaryboard)
- Cluttered output when user only needed individual FIELD-* files

**Root Cause**:
- Level 2 mode assumes "combined facility analysis" regardless of dataset count
- No check for `len(analysis_summaries) == 1` before creating SET/SITE structure
- SITE directory creation happened even for single transformers

**Solution Applied**:
```python
# Added in: eeBEHAVIOR.py (lines 4197-4252)
# Check for single dataset and skip SET/SITE generation
if len(analysis_summaries) == 1 and study_level in ['level2', 'level3']:
    # Generate only FIELD-* files in transformer directory
    # Include FIELD-Summaryboard (user requirement)
    # Skip all SET/SITE directory and file generation
    return  # Exit after individual analysis
```

**User Requirements Addressed**:
1. ✅ No SITE directory for single dataset analysis
2. ✅ No SET1-* files generated
3. ✅ All outputs in single transformer directory: `Reports/Study/TRANSFORMER_{name}/`
4. ✅ **Always generate FIELD-Summaryboard** (critical dashboard for all analyses)
5. ✅ 4 FIELD dashboards total: Energyboard + Heatboard + Voltboard + Summaryboard

**Directory Structure - Single Dataset**:
```
Reports/T10_1QTR2005/
└── TRANSFORMER_T10.AirChiller.1qtr2025/
    ├── FIELD-Energyboard_*.html
    ├── FIELD-Heatboard_*.html
    ├── FIELD-Voltboard_*.html       # NOW WORKS!
    ├── FIELD-Summaryboard_*.html    # NOW INCLUDED!
    ├── FIELDp1-EnergyHealth_*.md
    └── FIELDp2-VoltageHealth_*.md
```

**Directory Structure - Multi Dataset**:
```
Reports/T10_1QTR2005/
├── TRANSFORMER_T10.AirChiller.1qtr2025/
│   └── [FIELD-* files for transformer 1]
├── TRANSFORMER_T11.Compressor.1qtr2025/
│   └── [FIELD-* files for transformer 2]
└── SITE_Foster_Farms__Cherry_Ave_Facility/
    ├── SET1-Summaryboard_*.html
    ├── SET1-Energyboard_*.html
    ├── SET1-Heatboard_*.html
    └── SET1-Voltboard_*.html
```

**Key Insights**:
- ✅ Check dataset count BEFORE creating directory structures
- ✅ Level selection (1/2/3) should not override single-dataset logic
- ✅ SET/SITE reports only make sense for multi-transformer analysis
- ✅ Summaryboard is ALWAYS required (special case even for single dataset)
- ✅ Single dataset in Level 2 should behave like Level 1 + Summaryboard
- ✅ User explicitly wants clean output structure for individual analyses

**Implementation Pattern**:
```python
# Pattern for conditional structure creation
if len(analysis_summaries) == 1:
    # Single dataset mode
    output_dir = transformer_directory
    prefix = "FIELD-"
    generate_summaryboard()  # Always include
else:
    # Multi-dataset mode
    output_dir = site_directory
    prefix = f"SET{set_number}-"
    generate_summaryboard()  # Part of SET reports
```

### Testing Recommendations
Based on today's fixes, always test:
1. ✅ Single transformer analysis (verify no SITE directory created)
2. ✅ Multi-transformer analysis (verify SET/SITE structure correct)
3. ✅ All dashboard types generate successfully (Energy, Heat, Volt, Summary)
4. ✅ Function calls use correct names and parameters
5. ✅ Directory structure matches user expectations
6. ✅ No placeholder values remain in generated dashboards

### Summary Dashboard (Siteboard) Dynamic Rendering System (October 28, 2025)

**Overview**: The Summary Dashboard (eUnitySiteboard.html) displays up to 4 transformers with dynamic Power Factor gauges, energy metrics, and cost analysis. Every dataset gets a summaryboard — for single transformers (FIELD-Summaryboard) and for multi-transformer facilities (SET-Summaryboard and SITE-Summaryboard).

**Problem Solved**: Hardcoded transformer names in template caused fake transformer cards to appear

**Root Cause**:
- Template had placeholder transformer names: "T12.Main", "T15.Fillet", "T16.Compressor"
- These hardcoded names created fake cards even when no data existed
- JavaScript errors due to template literals not wrapped in `<script>` tags
- Console message incorrectly stated "3 FIELD dashboards" instead of 4

**Solutions Applied**:

1. **Dynamic Transformer Card Rendering** (lines 393-592)
   ```html
   <!-- BEFORE: Hardcoded names -->
   <h2>T12.Main</h2>
   
   <!-- AFTER: Dynamic binding -->
   <h2>
     <span id="xfmr2-name"></span>
     <span id="xfmr2-kva-wrap"> (<span id="xfmr2-kva">2500</span> kVA)</span>
   </h2>
   ```
   - Removed hardcoded transformer names (T12.Main, T15.Fillet, T16.Compressor)
   - Replaced with empty `<span>` elements: `xfmr2-name`, `xfmr3-name`, `xfmr4-name`
   - Generator populates names from actual dataset
   - CSS hides cards with empty names automatically

2. **JavaScript Template Literal Fix** (line 582-583)
   ```javascript
   // BEFORE: Missing opening <script> tag
   <script src="../static/unity-dashboard.js"></script>
     document.addEventListener('DOMContentLoaded', () => {
   
   // AFTER: Properly wrapped
   <script src="../static/unity-dashboard.js"></script>
   <script>
     document.addEventListener('DOMContentLoaded', () => {
   ```
   - Added missing `<script>` opening tag before inline JavaScript
   - Prevents JavaScript template literal errors
   - Closing `</script>` tag already existed at line 697

3. **Console Message Correction** (eeBEHAVIOR.py)
   ```python
   # BEFORE:
   print("3 FIELD dashboards generated: Energy + Heat + Voltage")
   
   # AFTER:
   print("4 FIELD dashboards generated: Energy + Heat + Voltage + Summary")
   ```
   - Updated to reflect that Summary dashboard is always generated
   - Accurate count: Energyboard + Heatboard + Voltboard + Summaryboard = 4

4. **Stats Column Layout Optimization** (lines 318-360)
   ```css
   /* Centered stats display with tight column spacing */
   .stats {
     text-align: center;
     display: flex;
     flex-direction: column;
     align-items: center;
   }
   
   .stats div {
     display: inline-flex;
     justify-content: center;
     gap: 8px;  /* Tight spacing between label and value */
   }
   
   .label::after {
     content: ' :';  /* Auto-add colon after labels */
   }
   ```
   - Changed from `justify-content: space-between` to `center`
   - Added automatic colon after labels using CSS `::after`
   - Reduced gap from 20px to 8px for tighter column spacing
   - Centered entire stats block under Power Factor gauge
   - Result: Clean format like "Minimum Target : 2400"

**Layout Behavior**:
- **1 Transformer**: Single 2x wide card, centered (layout-1 class)
- **2 Transformers**: Two cards side by side (layout-2 class)
- **3-4 Transformers**: Grid layout with all visible cards
- **CSS Auto-hide**: Cards with empty `xfmr-name` automatically hidden

**Data Flow**:
```python
# Generator populates transformer data dynamically
transformer_data = {
    'xfmr1-name': 'T10.AirChiller',
    'xfmr2-name': '',  # Empty = card hidden
    'xfmr3-name': '',  # Empty = card hidden
    'xfmr4-name': ''   # Empty = card hidden
}
```

**Key Metrics Displayed**:
- Power Factor gauge (3D golden gradient bubble)
- Energy Wasted percentage: `(WasteEnergykW + CoolingkW) / SupplyKVA * 100`
- Minimum Target: `tMax_SUPPLY × Power_Factor × 18_hours × days`
- Above/Below Target percentage
- Active Usage (kW) and Cost/hr
- Reactive Waste (kW) and Cost/hr

**File Generation Pattern**:
- **Single Dataset**: `FIELD-Summaryboard_{transformer}_{AN}_{dates}.html`
- **Multi-Dataset Set**: `SET1-Summaryboard_{site}_{resolution}_{dates}.html`
- **Multi-Dataset Site**: `SITE-Summaryboard_{site}_{resolution}_{dates}.html`

**Critical Lessons**:
1. ✅ Always use dynamic data bindings, never hardcode placeholder data
2. ✅ Empty data elements should trigger CSS hiding, not JavaScript errors
3. ✅ JavaScript must be properly wrapped in `<script>` tags
4. ✅ Console messages should accurately reflect generated output
5. ✅ Summaryboard is ALWAYS generated (4th dashboard type)
6. ✅ Use CSS `::after` for consistent formatting (colons, symbols)
7. ✅ Center alignment with tight gaps improves readability
8. ✅ Every dataset analysis includes a summaryboard for quick overview

**Integration with Analysis Pipeline**:
- Summaryboard generated after all three main dashboards
- Uses same `unified_dashboard_generator.py` system
- Template: `dashboard/templates/eUnitySiteboard.html`
- Output alongside Energy, Heat, and Voltage dashboards
- Provides executive summary view of transformer performance

**Why Summaryboard Matters**:
- Quick overview of facility performance at a glance
- Compares multiple transformers side-by-side
- Shows cost impact of energy waste
- Power Factor gauges provide instant visual health check
- Essential for facility managers and executives
- Always included even for single-transformer analysis
