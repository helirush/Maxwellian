---
**File**: `LOADER_MIGRATION_GUIDE.md`  
**Tag**: `eMemory.knowledge.evision.loader_migration`  
**Category**: 03_Knowledge  
**Agent**: CLERK  
**Created**: 2025-11-16  
**Last Updated**: 2025-11-16  
**Status**: ACTIVE  
**Importance**: CRITICAL  
**Related**: `01_Context/activeContext.md`, `systemPatterns.md`  
---

# eVision Loader Migration Guide: Loaders 1-2 → Loader 6 Architecture

## 🎯 Mission

Modernize eVision loaders 1-2 by applying three critical fixes that were completed in loaders 3-6. This guide provides step-by-step instructions to ensure **100% consistency** across all six loaders.

---

## ✅ What Needs to Be Done

### Target State: All Loaders (1-6) Identical

After modernization, loaders 1-6 will all have:

1. ✅ **textwrap.dedent()** for HTML table rendering
2. ✅ **Full-width HTML display** with UUID-scoped CSS (height 800px)
3. ✅ **plot_data() parameters** for MPTS MODE chart annotation
4. ✅ **render_overlay_selector() unpacking** for all 8 return values

**Current Status** (November 16, 2025):
- ✅ Loader 6: **COMPLETE** - All fixes implemented and tested
- ✅ Loader 5: **COMPLETE** - All fixes implemented and tested
- ✅ Loader 4: **COMPLETE** - All fixes implemented and tested
- ✅ Loader 3: **COMPLETE** - All fixes implemented and tested
- ⏳ Loader 2: **PENDING** - Ready for migration
- ⏳ Loader 1: **PENDING** - Ready for migration

---

## 📋 Three Core Fixes Explained

### Fix 1: HTML Rendering with textwrap.dedent()

**Problem**: Indented HTML gets parsed as Markdown text instead of raw HTML, causing red text rendering.

**Solution**: Use `textwrap.dedent()` to remove leading indentation before passing to Streamlit.

**Where**: HTML table definition (typically 50-200 lines in each loader)

**Example Pattern**:
```python
import textwrap

html_content = textwrap.dedent(f"""
<table class="highlighted-table">
    <tr>
        <th>Header</th>
    </tr>
    <tr>
        <td>{value}</td>
    </tr>
</table>
""")

st.markdown(html_content, unsafe_allow_html=True)
```

**Files to Check**:
- Loader 1: `eVision/action/loader1.py` - Line 15 (import), HTML section
- Loader 2: `eVision/action/loader2.py` - Line 15 (import), HTML section

---

### Fix 2: Full-Width HTML Display with UUID Scoping

**Problem**: HTML dashboards display cropped/constrained in Streamlit expander, cutting off content on right side.

**Solution**: UUID-scoped CSS to expand HTML container to 100% viewport width without affecting sidebar.

**Where**: HTML file handling section (typically lines 1150-1200)

**Example Pattern**:
```python
import uuid

html_container_id = f"html-dashboard-{uuid.uuid4().hex[:8]}"

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

**Critical Detail**: Height changed from 600px → 800px for better dashboard visibility

**Files to Check**:
- Loader 1: Around lines 1000-1020 (HTML file handler)
- Loader 2: Around lines 1000-1020 (HTML file handler)

---

### Fix 3: plot_data() Parameters for Chart Annotation

**Problem**: MPTS MODE chart annotation doesn't appear because required parameters not passed to plot_data().

**Solution**: Always pass `selected_units` and `unity_pf` parameters (they enable annotation in dataviewer.py lines 1338-1351).

**Where**: plot_data() function call (typically lines 900-950)

**Example Pattern**:
```python
fig, config = plot_data(
    df=df,
    transformer_size=transformer_size,
    chart_title=chart_title,
    selected_resolution=selected_resolution,
    selected_overlays=st.session_state.get(f"selected_overlays_{overlay_suffix}", []),
    num_rows=len(df),
    start_date_str=start_date_str,
    end_date_str=end_date_str,
    efield_unit=efield_unit,
    base_filename=file_name,
    customer=customer,
    loader_number=1,  # or 2 for loader2
    selected_units=selected_units,           # ← ADD THIS
    unity_pf=unity_pf                        # ← ADD THIS
)
```

**Files to Check**:
- Loader 1: plot_data() call around lines 900-950
- Loader 2: plot_data() call around lines 900-950

---

### Fix 4: render_overlay_selector() Unpacking (8 Return Values)

**Problem**: Not unpacking all 8 return values causes missing chart annotations and parameters.

**Solution**: Unpack all 8 values including heat model parameters and decay cost data.

**Where**: render_overlay_selector() call (typically lines 300-450)

**Current Pattern** (loaders 3-6):
```python
selected_overlays, unity_pf, selected_units, chartlabel, composite_kw_rate, co2e_cost_per_mt, simulation_enabled, heat_model_params = render_overlay_selector(
    key_suffix=overlay_suffix, loader_number=loader_index
)
```

**Files to Check**:
- Loader 1: render_overlay_selector() call around lines 300-450
- Loader 2: render_overlay_selector() call around lines 300-450

---

### Fix 5: Baseline Zero-Out Logic (CRITICAL FIX - November 16)

**Problem**: When MPTS Simulation enabled and PF target = baseline PF, values should be $0 but weren't.
- Example: PF target 75.7% = baseline 75.7% should show $0, not $402,232
- Example: Thermal burden should show 0 BTU/hr, not 1,298,807 BTU/hr

**Root Cause**: Missing "true baseline" detection that checks ALL THREE conditions:
1. PF at baseline (checked)
2. Voltage at baseline (NOT checked)
3. iTHD at baseline (NOT checked)

**Solution**: Add comprehensive baseline detection before economic and thermal calculations.

**Where**: Economics section (lines ~587-622) and thermal section (lines ~624-684)

**Pattern to Implement**:
```python
# Economics: Zero out when PF at baseline
if simulation_enabled and unity_pf is not None:
    pf_tolerance = 0.001
    is_at_baseline_pf = abs(unity_pf - pf_nom) < pf_tolerance
else:
    is_at_baseline_pf = False

if is_at_baseline_pf:
    mini_energy_value = 0.0
    mini_emission_value = 0.0
    mini_energy_value_fmt = "0"
    mini_emission_value_fmt = "0"
else:
    # Calculate values normally
    ...

# Thermal: Zero out when PF + voltage + iTHD all at baseline
voltage_tolerance = 1.0
is_at_baseline_voltage = abs(user_voltage - volts_nom) < voltage_tolerance

thd_tolerance = 0.5
is_at_baseline_thd = abs(user_thd - thd_avg) < thd_tolerance

if is_at_baseline_pf and is_at_baseline_voltage and is_at_baseline_thd:
    heat_btu_per_hour = 0.0
    cooling_cost_hourly = 0.0
    mini_thermal_value_fmt = "0 BTU/hr"
    mini_cooling_value_fmt = "0"
else:
    # Calculate thermal normally
    ...
```

**Status**: ✅ Already applied to loaders 4, 5, 6 (November 16)
**For Loaders 1-2**: Apply this fix when migrating to ensure 100% consistency

---

## 🔍 Verification Checklist

Before starting migration, verify current state:

### Loader 1 Current State
- [ ] Line 15: `import textwrap` present?
- [ ] HTML section uses `textwrap.dedent()`?
- [ ] HTML file handler has UUID scoping?
- [ ] plot_data() call has `selected_units=` and `unity_pf=`?
- [ ] render_overlay_selector() unpacking has 8 values?

### Loader 2 Current State
- [ ] Line 15: `import textwrap` present?
- [ ] HTML section uses `textwrap.dedent()`?
- [ ] HTML file handler has UUID scoping?
- [ ] plot_data() call has `selected_units=` and `unity_pf=`?
- [ ] render_overlay_selector() unpacking has 8 values?

---

## 📐 Step-by-Step Migration: Loader 1

### Step 1: Add textwrap Import
**File**: `eVision/action/loader1.py`  
**Line**: 15

Add to imports:
```python
import textwrap
```

### Step 2: Update HTML Table with textwrap.dedent()
**File**: `eVision/action/loader1.py`  
**Line**: ~427 (check actual line number in your file)

Find:
```python
html_content = f"""
<table class="highlighted-table">
...
```

Replace with:
```python
html_content = textwrap.dedent(f"""
<table class="highlighted-table">
...
""")
```

**Key**: The triple-quoted string must start on the same line as `dedent(f"""` with NO indent before the `<table>` tag.

### Step 3: Update render_overlay_selector() Unpacking
**File**: `eVision/action/loader1.py`  
**Line**: ~405

Find:
```python
selected_overlays, unity_pf, selected_units, chartlabel = render_overlay_selector(...)
```

Replace with:
```python
selected_overlays, unity_pf, selected_units, chartlabel, composite_kw_rate, co2e_cost_per_mt, simulation_enabled, heat_model_params = render_overlay_selector(
    key_suffix=overlay_suffix, loader_number=loader_index
)
```

### Step 4: Update plot_data() Call
**File**: `eVision/action/loader1.py`  
**Line**: ~940

Find:
```python
fig, config = plot_data(
    ...
    loader_number=1,
)
```

Add two parameters before closing paren:
```python
fig, config = plot_data(
    ...
    loader_number=1,
    selected_units=selected_units,
    unity_pf=unity_pf
)
```

### Step 5: Update HTML File Handler
**File**: `eVision/action/loader1.py`  
**Line**: ~1000-1020 (exact location varies by loader)

Find the HTML file handler section:
```python
elif file_type == "text/html" or file_name.endswith(".html"):
    try:
        html_data = uploader_port.getvalue().decode("utf-8")
        st.components.v1.html(html_data, height=600, scrolling=True)
```

Replace with:
```python
elif file_type == "text/html" or file_name.endswith(".html"):
    file_message = f"HTML : {file_name}"
    st.markdown(
        f"""
        <div style='background-color: rgba(100, 110, 50, 1); color: white; 
        padding: 10px; margin: 10px 0; border-radius: 10px; 
        text-align: center; border: 1px solid white; font-weight: bold;'>
            context: {file_name}
        </div>
        """, 
        unsafe_allow_html=True
    )
    try:
        html_data = uploader_port.getvalue().decode("utf-8")
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

---

## 📐 Step-by-Step Migration: Loader 2

Repeat all steps from "Migration: Loader 1" section but:
- Change `loader_number=1` → `loader_number=2`
- Change all file paths from `loader1.py` → `loader2.py`

---

## 🧪 Testing After Migration

### Test 1: CSV Data Load
1. Load a CSV file in Loader 1
2. Verify metrics table displays without red markdown text
3. Verify chart appears with proper annotation
4. Check that MPTS MODE label appears when enabled

### Test 2: HTML Dashboard
1. Load an HTML file in Loader 1
2. Verify dashboard displays full-width (not cropped)
3. Verify height is sufficient (800px)
4. Check sidebar is still visible and functional

### Test 3: Simulation Mode
1. Enable MPTS Simulation in overlay selector
2. Move power factor slider
3. Verify chart annotation updates
4. Verify metrics recalculate correctly

### Test 4: Consistency Check
Run all six loaders with identical data:
- [ ] All metrics tables render identically
- [ ] All charts display identically
- [ ] All HTML files display identically
- [ ] All simulations behave identically

---

## 🔗 Reference Files (Read-Only)

Use these as reference when confused:

**Loader 6 (Complete Reference)**:
- `eVision/action/loader6.py` - Lines 15, 476, 1000-1013, 1268-1269

**Loader 5 (Complete Reference)**:
- `eVision/action/loader5.py` - Lines 15, 486, 1180-1197, 1125-1126

**Loader 4 (Complete Reference)**:
- `eVision/action/loader4.py` - Lines 15, 476, 1000-1013, 940-941

**Loader 3 (Complete Reference)**:
- `eVision/action/loader3.py` - Lines 15, 405, 572-573, 632-645

---

## ⚠️ Common Mistakes to Avoid

### Mistake 1: textwrap.dedent() Indentation
```python
# ❌ WRONG - dedent() call indented
    html_content = textwrap.dedent(f"""
    <table>
    """)

# ✅ CORRECT - dedent() call at proper indent level
html_content = textwrap.dedent(f"""
<table>
""")
```

### Mistake 2: Missing UUID Import
```python
# ❌ WRONG - forgot to import uuid
html_container_id = f"html-dashboard-{uuid.uuid4().hex[:8]}"

# ✅ CORRECT
import uuid
html_container_id = f"html-dashboard-{uuid.uuid4().hex[:8]}"
```

### Mistake 3: Height Not Updated
```python
# ❌ WRONG - still using old height
st.components.v1.html(html_data, height=600, scrolling=True)

# ✅ CORRECT
st.components.v1.html(html_data, height=800, scrolling=True)
```

### Mistake 4: Partial render_overlay_selector() Unpacking
```python
# ❌ WRONG - only unpacking 4 values
selected_overlays, unity_pf, selected_units, chartlabel = render_overlay_selector(...)

# ✅ CORRECT - unpacking all 8 values
selected_overlays, unity_pf, selected_units, chartlabel, composite_kw_rate, co2e_cost_per_mt, simulation_enabled, heat_model_params = render_overlay_selector(...)
```

---

## 📊 Verification Commands

Run these grep commands to verify migrations:

```bash
# Check for textwrap import in loaders 1-2
grep "import textwrap" /Users/mdhowell/eestream/eVision/action/loader1.py
grep "import textwrap" /Users/mdhowell/eestream/eVision/action/loader2.py

# Check for textwrap.dedent in HTML sections
grep "textwrap.dedent" /Users/mdhowell/eestream/eVision/action/loader1.py
grep "textwrap.dedent" /Users/mdhowell/eestream/eVision/action/loader2.py

# Check for uuid import
grep "import uuid" /Users/mdhowell/eestream/eVision/action/loader1.py
grep "import uuid" /Users/mdhowell/eestream/eVision/action/loader2.py

# Check for HTML container ID (full-width display)
grep "html_container_id" /Users/mdhowell/eestream/eVision/action/loader1.py
grep "html_container_id" /Users/mdhowell/eestream/eVision/action/loader2.py

# Check for height=800
grep "height=800" /Users/mdhowell/eestream/eVision/action/loader1.py
grep "height=800" /Users/mdhowell/eestream/eVision/action/loader2.py

# Check for 8-value unpacking
grep "simulation_enabled, heat_model_params = render_overlay_selector" /Users/mdhowell/eestream/eVision/action/loader1.py
grep "simulation_enabled, heat_model_params = render_overlay_selector" /Users/mdhowell/eestream/eVision/action/loader2.py

# Check for plot_data parameters
grep "selected_units=selected_units" /Users/mdhowell/eestream/eVision/action/loader1.py
grep "unity_pf=unity_pf" /Users/mdhowell/eestream/eVision/action/loader1.py
```

---

## 🎯 Completion Checklist

After migrating both loaders 1 and 2:

- [ ] **Loader 1**: All 4 fixes applied and tested
- [ ] **Loader 2**: All 4 fixes applied and tested
- [ ] **Verification**: All 6 loaders now have identical implementations
- [ ] **Testing**: CSV data loads correctly
- [ ] **Testing**: HTML dashboards display full-width
- [ ] **Testing**: MPTS MODE annotations work
- [ ] **Testing**: Simulation mode updates properly
- [ ] **Memory**: This guide updated with completion date
- [ ] **Update activeContext.md**: Mark loaders 1-2 as complete

---

## 📅 Timeline

| Phase | Status | Date | Note |
|-------|--------|------|------|
| Loaders 5-6 complete | ✅ | Nov 12-13, 2025 | Reference implementations |
| Loader 4 migrated | ✅ | Nov 14, 2025 | All 4 fixes applied |
| Loader 3 migrated | ✅ | Nov 15, 2025 | All 4 fixes applied |
| Loaders 3-6 verified | ✅ | Nov 16, 2025 09:00 | 100% consistency confirmed |
| **Loader 4 baseline fix** | ✅ | Nov 16, 2025 19:15 | **Critical: True baseline logic** |
| **All loaders 3-6 now 100% identical** | ✅ | Nov 16, 2025 19:15 | **READY FOR LOADERS 1-2** |
| Loader 2 migration | ⏳ | **READY** | Use LOADER_MIGRATION_GUIDE + Fix 5 |
| Loader 1 migration | ⏳ | **READY** | Use LOADER_MIGRATION_GUIDE + Fix 5 |
| All loaders verified | ⏳ | **NEXT** | Final consistency test |

---

## 🔗 Quick Links

- **eMemory Home**: `/Users/mdhowell/eestream/eMemory/README.md`
- **Active Context**: `/Users/mdhowell/eestream/eMemory/01_Context/activeContext.md`
- **System Patterns**: `/Users/mdhowell/eestream/eMemory/03_Knowledge/systemPatterns.md`
- **Loader 6 Reference**: `/Users/mdhowell/eestream/eVision/action/loader6.py`

---

**This guide enables seamless modernization of all eVision loaders to match the latest Loader 6 architecture.**

