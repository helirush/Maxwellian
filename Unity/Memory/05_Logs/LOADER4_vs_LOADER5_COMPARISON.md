# Loader 4 vs Loader 5 - Code Comparison

**Purpose**: Verify loader4 changes match loader5 patterns  
**Date**: November 16, 2025

---

## 1. HTML Table Rendering - textwrap.dedent() Pattern

### Loader 4 (UPDATED)
```python
# Lines 501-628
html_content = textwrap.dedent(f"""
<div class="estream_title">{customer_title}</div>
<div style="height: 0.1em;"></div>
<table class="highlighted-table">
    <tr>
        <th class="row10" colspan="2">
            UNRECOVERED ENERGY EQUIVALENT
            ...
        </th>
    </tr>
    ...
</table>
""")
st.markdown(html_content, unsafe_allow_html=True)
```

### Loader 5 (REFERENCE)
Compare loader5.py around lines 700-900 - should have identical pattern with textwrap.dedent()

**Verification Points**:
- ✓ Uses `textwrap.dedent()` wrapping
- ✓ Every HTML tag starts at column 0
- ✓ Template variable interpolation with `.format()` or f-string
- ✓ `st.markdown(html_content, unsafe_allow_html=True)`

---

## 2. HTML File Viewer - Full-Width Display

### Loader 4 (UPDATED)
```python
# Lines 703-718
elif file_type == "text/html" or file_name.endswith(".html"):
    file_message = f"HTML : {file_name}"
    st.markdown(f"""...""", unsafe_allow_html=True)
    
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
        
    except UnicodeDecodeError:
        st.error("Unable to decode HTML file (not UTF-8).")
```

### Loader 5 (REFERENCE)
Compare loader5.py - should have identical HTML file viewer pattern around line 700+

**Verification Points**:
- ✓ Uses `uuid.uuid4().hex[:8]` for unique ID
- ✓ CSS targets `#{html_container_id}` for scoping
- ✓ Uses `100vw` and `calc(-50vw + 50%)` for full-width
- ✓ Height set to `800` (not 600)
- ✓ Proper `</div>` closing with `st.markdown()`

---

## Testing Script

Run this to verify both loaders:

```bash
cd /Users/mdhowell/eestream

# Check that loader4 now has textwrap.dedent pattern
echo "=== LOADER4 textwrap.dedent usage ==="
grep -A 5 "html_content = textwrap.dedent" eVision/action/loader4.py | head -10

# Check that loader5 has same pattern (reference)
echo -e "\n=== LOADER5 textwrap.dedent usage ==="
grep -A 5 "html_content = textwrap.dedent" eVision/action/loader5.py | head -10

# Check that loader4 has full-width HTML fix
echo -e "\n=== LOADER4 full-width HTML fix ==="
grep -A 3 "html_container_id = " eVision/action/loader4.py | head -5

# Check that loader5 has same fix (reference)
echo -e "\n=== LOADER5 full-width HTML fix ==="
grep -A 3 "html_container_id = " eVision/action/loader5.py | head -5

# Verify height is 800 in both
echo -e "\n=== HEIGHT COMPARISON ==="
echo "Loader4 height:"
grep "st.components.v1.html" eVision/action/loader4.py | head -1
echo "Loader5 height:"
grep "st.components.v1.html" eVision/action/loader5.py | head -1
```

---

## Runtime Testing Checklist

### Test 1: Main Table Rendering
1. Load Loader 4 with a CSV file
2. **Expected**: Metrics table renders cleanly with no red markdown text
3. **Compare**: Side-by-side with Loader 5 - should be identical
4. **Verify**: All values display correctly

### Test 2: HTML File Display
1. Upload an HTML dashboard file to Loader 4
2. **Expected**: Dashboard displays at full width, not cropped
3. **Compare**: Side-by-side with Loader 5 - should look identical
4. **Verify**: 
   - Full viewport width used
   - Sidebar still functional
   - Content not cut off on right
   - Height increased from 600 to 800

### Test 3: Value Display Accuracy
1. Load same CSV in both Loader 4 and Loader 5
2. **Expected**: Identical calculated values
3. **Verify**:
   - kVA, kW, kVAR values
   - CO2e values
   - Voltage, Amperage, THD stats
   - No mathematical differences

---

## Key Differences to Watch

**Should be NO differences** after this update between Loader 4 and Loader 5 for:
- HTML table rendering style
- Full-width display behavior
- Value calculations and display
- File upload handling

**Any differences indicate**:
- ❌ Incomplete application of textwrap.dedent()
- ❌ Missing UUID scoping on HTML viewer
- ❌ Height not updated to 800
- ❌ Other inconsistencies to investigate

---

## Success Criteria

✅ Loader 4 modernization is successful when:
1. Main metrics table renders without markdown artifacts
2. HTML files display full-width without cropping
3. All values calculated correctly
4. Visual output matches Loader 5 exactly
5. No error messages or warnings

---

**Next**: After successful testing, apply same fixes to Loaders 3, 2, and 1.
