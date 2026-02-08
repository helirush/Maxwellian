# Loaders 1-4 Modernization Plan

---
**File**: `PLAN_LOADERS_1-4_MODERNIZATION.md`  
**Tag**: `eMemory.planning.loaders_modernization`  
**Category**: 05_Logs  
**Created**: 2025-11-16  
**Status**: PLANNING  
**Importance**: CRITICAL  
**Related**: `CODEX_HEADER_FIX_SUMMARY.md`, `activeContext.md`  

---

## Overview

**Objective**: Apply critical fixes and enhancements from loaders 5-6 to loaders 1-4 to ensure consistent implementation across all eVision analysis windows.

**Status Summary**:
- ✅ **Loader 6**: Complete (Decay Model + HTML fixes)
- ✅ **Loader 5**: Complete (HTML fixes + Decay Model ready)
- 🚧 **Loaders 1-4**: PENDING - Need systematic modernization

---

## Critical Fixes to Replicate

### 1. HTML Rendering Fix (textwrap.dedent)
**Source**: Codex's Loader6 fix (November 14, 2025)  
**Problem**: Streamlit markdown parser treats indented HTML as markdown text instead of raw HTML  
**Solution**: Wrap HTML templates with `textwrap.dedent()` to remove leading whitespace

**Pattern to Apply**:
```python
import textwrap

html_content = textwrap.dedent("""
<table class="highlighted-table">
    <tr>
        <td>Value</td>
    </tr>
</table>
""").format(
    variable1=value1,
    variable2=value2
)

st.markdown(html_content, unsafe_allow_html=True)
```

**Impact**: 
- Fixes raw HTML/markdown text display issues
- Ensures proper rendering of PHYSICS columns (ENERGY VALUE, EMISSION VALUE, etc.)
- Prevents red markdown text artifacts

---

### 2. Full-Width HTML Display Fix
**Source**: Loader5/6 implementation (November 13, 2025)  
**Problem**: Energy dashboards cropped in expander container; fixed 600px height too short  
**Solution**: UUID-scoped CSS + increase height to 800px

**Pattern to Apply**:
```python
import uuid

# Create unique container ID for scoped styling
html_container_id = f"html-dashboard-{uuid.uuid4().hex[:8]}"

# Scoped CSS - only affects this specific container
st.markdown(f"""
    <style>
    #{html_container_id} {{
        width: 100vw !important;
        margin-left: calc(-50vw + 50%) !important;
        margin-right: calc(-50vw + 50%) !important;
    }}
    </style>
    <div id="{html_container_id}">
""", unsafe_allow_html=True)

st.components.v1.html(html_data, height=800, scrolling=True)

st.markdown("</div>", unsafe_allow_html=True)
```

**Impact**:
- Energy dashboards display at full viewport width
- Taller viewport (800px) shows more content without scrolling
- Sidebar menus preserved (scoped CSS)
- Professional dashboard viewing experience

---

### 3. Decay Cost Model Integration
**Source**: Full Day Session (November 15, 2025)  
**Problem**: Cooling cost shown but equipment decay cost missing  
**Solution**: Integrate decay_model.py with three-vector multiplicative model

**Files to Reference**:
- `eVision/action/decay_model.py` - Core module (187 lines)
- `eVision/action/loader6.py` - Integration example

**Key Functions**:
```python
from decay_model import calculate_decay_cost, calculate_total_cooling_and_decay_cost

# Single point calculation
decay_cost = calculate_decay_cost(
    thermal_stress_pct=12.0,  # 12% above baseline
    harmonic_stress_pct=8.5,   # 8.5% above 5% baseline
    voltage_stress_pct=4.2     # 4.2% outside ±10% deviation
)

# Combined thermal + decay cost
total_cost = calculate_total_cooling_and_decay_cost(
    cooling_cost_hourly=25.50,
    thermal_stress_pct=12.0,
    harmonic_stress_pct=8.5,
    voltage_stress_pct=4.2
)
```

**UI Integration**:
- Add "Equipment Cost ($/yr)" input in dataviewer.py (default $50K)
- Update header table: "COOLING VALUE" → "COOLING AND DECAY COSTS"
- Display combined metric: Cooling + Decay = Total Thermal System Cost

**Impact**:
- Equipment life calculations showing 50-129% faster degradation under stress
- Business case strengthened: ROI improves from 2-3 years to 1-2 years
- Customer narrative: "Your harmonics cost you $3,200/year in premature failure"

---

### 4. Physics Calculations Standardization
**Source**: Loader6 overhaul (November 13, 2025)  
**Key Fixes**:

#### 4.1 Hours in Dataset Calculation
- **Problem**: Hardcoded 8760 hours (full year) instead of actual dataset duration
- **Solution**: Calculate from actual time range

```python
def get_duration_in_hours(df):
    """Calculate actual hours in dataset from time column"""
    if len(df) < 2:
        return 8760  # Default if insufficient data
    
    time_col = find_time_column(df)
    if time_col is None:
        return 8760
    
    df[time_col] = pd.to_datetime(df[time_col], errors='coerce')
    time_range = df[time_col].max() - df[time_col].min()
    return time_range.total_seconds() / 3600
```

#### 4.2 MPTS Simulation Zero-Out Logic
- **Problem**: Simulation at baseline PF should show zero improvement
- **Solution**: Check if target PF within 2% of nominal PF

```python
if simulation_enabled and abs(unity_pf - pf_nom) < 0.02:
    # At baseline: no improvement yet, all values = 0
    mini_energy_value_fmt = "0"
    mini_emission_value_fmt = "0"
    mini_thermal_value_fmt = "0 BTU/hr"
    mini_cooling_value_fmt = "0 kW/hr"
else:
    # Calculate actual values using user inputs and dataset hours
    ...
```

#### 4.3 Dollar Sign Handling
- **Problem**: Python `.format()` misinterprets `$` in values
- **Solution**: Remove `$` from format strings, add to HTML template

```python
# WRONG:
mini_energy_value_fmt = f"${mini_energy_value:,.0f}"  # $ gets parsed

# RIGHT:
mini_energy_value_fmt = f"{mini_energy_value:,.0f}"   # No $ 

# In HTML template:
<td class="row30" id="mini-energy-value">${mini_energy_value_fmt}</td>
```

---

## Implementation Strategy

### Phase 1: Analysis (Immediate)
**Task**: Examine each loader 1-4 to identify current state

```bash
# Check each loader for:
# 1. HTML template locations and formatting
# 2. Current physics calculation implementations
# 3. Existing decay cost integration (if any)
# 4. Full-width display implementations (if any)

for loader in {1..4}; do
  echo "=== LOADER $loader ==="
  grep -n "textwrap\|dedent" eVision/action/loader$loader.py || echo "No dedent"
  grep -n "decay_model\|decay_cost" eVision/action/loader$loader.py || echo "No decay"
  grep -n "100vw\|html-dashboard" eVision/action/loader$loader.py || echo "No full-width"
done
```

**Deliverable**: Analysis report with change matrix

---

### Phase 2: HTML Fix Application (Session 1)
**Tasks**:
1. Apply `textwrap.dedent()` to all HTML templates in loaders 1-4
2. Add `import textwrap` at top of each file
3. Verify no CSS comments in HTML templates (they render as text)

**Per Loader**:
- Identify all HTML templates in that loader
- Wrap each with `textwrap.dedent("""\n....\n""")`
- Ensure every line starts at column 0 inside the triple quotes
- Test rendering in eVision

**Verification**:
```python
# Create snapshot of rendered HTML for verification
with open(f'/tmp/loader{N}_table_debug.html', 'w') as f:
    f.write(html_content)
# Check that no red markdown text appears
# Check that all values display correctly
```

---

### Phase 3: Decay Cost Model Integration (Session 2)
**Tasks**:
1. Import decay_model.py module in each loader
2. Add Equipment Cost input to dataviewer.py
3. Calculate decay cost in mini-dashboard calculations
4. Update header table title and display

**Per Loader**:
- Add import: `from decay_model import calculate_total_cooling_and_decay_cost`
- Add decay cost calculation to physics section
- Update mini-dashboard HTML to show combined cooling+decay
- Test with sample data

**Verification**:
- Verify decay cost > $0 when stress conditions exist
- Test zero-out at baseline conditions
- Confirm business case impact shown to user

---

### Phase 4: Full-Width Display Fix (Session 3)
**Tasks**:
1. Add UUID import and container ID generation
2. Implement scoped CSS styling
3. Update HTML component height to 800px
4. Test on loaders with dashboard file uploads

**Per Loader**:
- Add import: `import uuid`
- Generate `html_container_id` before rendering
- Wrap HTML components with scoped CSS
- Change height from 600 → 800
- Test with HTML file upload

**Verification**:
- Energy dashboards display full-width
- All gauges visible without cropping
- Sidebar menus functional
- No CSS leaking to other elements

---

### Phase 5: Physics Calculations Standardization (Session 4)
**Tasks**:
1. Implement `get_duration_in_hours()` utility function
2. Fix MPTS simulation zero-out logic in all loaders
3. Fix dollar sign handling in format strings
4. Test physics value calculations

**Per Loader**:
- Import `get_duration_in_hours` from utils
- Replace hardcoded 8760 with dynamic calculation
- Add zero-out logic for baseline PF
- Fix all `$` symbols in format strings
- Test with multiple datasets

**Verification**:
- Physics values change based on dataset duration
- Simulation shows $0 at baseline PF
- All dollar amounts display correctly
- No HTML artifacts in physics columns

---

### Phase 6: Comprehensive Testing (Session 5-6)
**Tasks**:
1. Test all loaders 1-6 with standard datasets
2. Test HTML rendering with various file types
3. Test decay cost calculations with stress conditions
4. Test MPTS simulation workflows
5. Test full-width dashboard display

**Test Cases**:
```
For each loader 1-6:
├── Load CSV with 24 hours of data
├── Check: physics calculations correct
├── Load CSV with 7 days of data
├── Check: hours_in_dataset = 168
├── Load HTML file
├── Check: renders full-width, no markdown text
├── Enable MPTS simulation at baseline PF
├── Check: all physics values = 0
├── Move PF slider to 98%
├── Check: physics values show savings
├── Check: decay cost reflects new conditions
└── Check: no red markdown text anywhere
```

---

## File Change Matrix

| File | Loader 1 | Loader 2 | Loader 3 | Loader 4 | Loader 5 | Loader 6 |
|------|----------|----------|----------|----------|----------|----------|
| `loaderN.py` | ⚠️ Plan | ⚠️ Plan | ⚠️ Plan | ⚠️ Plan | ✅ Done | ✅ Done |
| HTML Templates | ⚠️ Plan | ⚠️ Plan | ⚠️ Plan | ⚠️ Plan | ✅ Done | ✅ Done |
| textwrap.dedent() | ⚠️ Plan | ⚠️ Plan | ⚠️ Plan | ⚠️ Plan | ✅ Done | ✅ Done |
| Full-width CSS | ⚠️ Plan | ⚠️ Plan | ⚠️ Plan | ⚠️ Plan | ✅ Done | ✅ Done |
| decay_model.py | ⚠️ Plan | ⚠️ Plan | ⚠️ Plan | ⚠️ Plan | ⏳ Ready | ✅ Done |
| Physics calcs | ⚠️ Plan | ⚠️ Plan | ⚠️ Plan | ⚠️ Plan | ✅ Done | ✅ Done |
| dataviewer.py | ⚠️ Plan | ⚠️ Plan | ⚠️ Plan | ⚠️ Plan | ✅ Done | ✅ Done |

---

## Priority and Sequencing

**High Priority** (Stability critical):
1. ✅ HTML rendering fix (textwrap.dedent) - **BLOCKING ISSUE**
2. ✅ Physics calculation standardization - **DATA ACCURACY CRITICAL**

**Medium Priority** (Feature complete):
3. ⚠️ Decay cost model integration - **BUSINESS VALUE**
4. ⚠️ Full-width display fix - **USER EXPERIENCE**

**Recommended Sequence**:
1. Phase 1: Analysis (quick review)
2. Phase 2: HTML fix (1-2 sessions)
3. Phase 5: Physics calc fix (1 session) - CAN BE DONE IN PARALLEL
4. Phase 3: Decay cost integration (1-2 sessions)
5. Phase 4: Full-width fix (1 session)
6. Phase 6: Testing (1-2 sessions)

---

## Key Success Metrics

- ✅ All loaders 1-6 render HTML without markdown artifacts
- ✅ Physics values calculated from actual dataset duration
- ✅ MPTS simulation zero-out logic working correctly
- ✅ Decay costs displayed with cooling costs
- ✅ Dashboards display at full viewport width
- ✅ All dollar amounts formatted correctly
- ✅ Comprehensive test suite passes for all loaders

---

## Risk Mitigation

**Risk**: HTML template changes break rendering in production
**Mitigation**: 
- Create `/tmp/loaderN_table_debug.html` snapshots
- Test before and after on multiple datasets
- Keep backups of original files

**Risk**: Physics calculations change user-visible metrics
**Mitigation**:
- Verify with known good data
- Compare old vs new calculations
- Document any changes in release notes

**Risk**: Decay cost integration requires coordination
**Mitigation**:
- decay_model.py already complete
- dataviewer.py interface documented
- Reference loader6 implementation

---

## Next Steps After Modernization

1. **eBehavior Integration**: Add decay cost to FIELDp1 and FIELDp2 reports
2. **Customer Presentations**: Create decay cost visualizations
3. **Episode Content**: "Full Value of MPTS: Beyond Energy to Equipment Longevity"
4. **Documentation**: Update coding standards with textwrap.dedent pattern
5. **Monitoring**: Track physics calculation accuracy across all loaders

---

**Memory Exchange**: Include this plan in next eMemory ZIP file snapshot.
