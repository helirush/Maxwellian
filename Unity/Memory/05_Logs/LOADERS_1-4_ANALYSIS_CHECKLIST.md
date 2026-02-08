# Loaders 1-4 Analysis Checklist

**Goal**: Quick assessment of current state before modernization  
**Date**: 2025-11-16

---

## Quick Status Check Commands

Run these to identify what needs to be fixed in each loader:

```bash
cd /Users/mdhowell/eestream

# Check for textwrap.dedent usage (should be present but isn't)
echo "=== TEXTWRAP.DEDENT USAGE ==="
grep -l "textwrap" eVision/action/loader{1..4}.py 2>/dev/null || echo "⚠️ Not found in loaders 1-4"
grep -l "textwrap" eVision/action/loader{5..6}.py 2>/dev/null && echo "✅ Present in loaders 5-6"

# Check for decay_model usage
echo -e "\n=== DECAY_MODEL USAGE ==="
grep -l "decay_model\|decay_cost" eVision/action/loader{1..4}.py 2>/dev/null || echo "⚠️ Not found in loaders 1-4"
grep -l "decay_model\|decay_cost" eVision/action/loader{5..6}.py 2>/dev/null && echo "✅ Present in loaders 5-6"

# Check for full-width HTML fix
echo -e "\n=== FULL-WIDTH HTML FIX ==="
grep -l "100vw\|html-dashboard\|uuid" eVision/action/loader{1..4}.py 2>/dev/null || echo "⚠️ Not found in loaders 1-4"
grep -l "100vw\|html-dashboard\|uuid" eVision/action/loader{5..6}.py 2>/dev/null && echo "✅ Present in loaders 5-6"

# Check for get_duration_in_hours
echo -e "\n=== DURATION CALCULATION ==="
grep -l "get_duration_in_hours\|hours_in_dataset" eVision/action/loader{1..4}.py 2>/dev/null || echo "⚠️ Likely hardcoded 8760 in loaders 1-4"
grep -l "get_duration_in_hours\|hours_in_dataset" eVision/action/loader{5..6}.py 2>/dev/null && echo "✅ Dynamic calculation in loaders 5-6"
```

---

## Per-Loader Analysis Template

### Loader 1 Analysis

**File**: `/Users/mdhowell/eestream/eVision/action/loader1.py`

- [ ] Check for HTML templates (search: `st.markdown("""` or `html_content`)
- [ ] Identify if HTML templates are indented (likely → need dedent)
- [ ] Check imports: `import textwrap` present?
- [ ] Check imports: `import uuid` present?
- [ ] Check for `100vw` or `html-dashboard` CSS?
- [ ] Look for physics calculations (search: `mini_energy_value`, `mini_cooling_value`)
- [ ] Check if hardcoded `8760` exists (should use `hours_in_dataset`)
- [ ] Look for MPTS simulation logic
- [ ] Check if decay_model imported
- [ ] Look for dollar sign handling issues

**Status**: ⚠️ PENDING

---

### Loader 2 Analysis

**File**: `/Users/mdhowell/eestream/eVision/action/loader2.py`

- [ ] Check for HTML templates (search: `st.markdown("""` or `html_content`)
- [ ] Identify if HTML templates are indented (likely → need dedent)
- [ ] Check imports: `import textwrap` present?
- [ ] Check imports: `import uuid` present?
- [ ] Check for `100vw` or `html-dashboard` CSS?
- [ ] Look for physics calculations (search: `mini_energy_value`, `mini_cooling_value`)
- [ ] Check if hardcoded `8760` exists (should use `hours_in_dataset`)
- [ ] Look for MPTS simulation logic
- [ ] Check if decay_model imported
- [ ] Look for dollar sign handling issues

**Status**: ⚠️ PENDING

---

### Loader 3 Analysis

**File**: `/Users/mdhowell/eestream/eVision/action/loader3.py`

- [ ] Check for HTML templates (search: `st.markdown("""` or `html_content`)
- [ ] Identify if HTML templates are indented (likely → need dedent)
- [ ] Check imports: `import textwrap` present?
- [ ] Check imports: `import uuid` present?
- [ ] Check for `100vw` or `html-dashboard` CSS?
- [ ] Look for physics calculations (search: `mini_energy_value`, `mini_cooling_value`)
- [ ] Check if hardcoded `8760` exists (should use `hours_in_dataset`)
- [ ] Look for MPTS simulation logic
- [ ] Check if decay_model imported
- [ ] Look for dollar sign handling issues

**Status**: ⚠️ PENDING

---

### Loader 4 Analysis

**File**: `/Users/mdhowell/eestream/eVision/action/loader4.py`

- [ ] Check for HTML templates (search: `st.markdown("""` or `html_content`)
- [ ] Identify if HTML templates are indented (likely → need dedent)
- [ ] Check imports: `import textwrap` present?
- [ ] Check imports: `import uuid` present?
- [ ] Check for `100vw` or `html-dashboard` CSS?
- [ ] Look for physics calculations (search: `mini_energy_value`, `mini_cooling_value`)
- [ ] Check if hardcoded `8760` exists (should use `hours_in_dataset`)
- [ ] Look for MPTS simulation logic
- [ ] Check if decay_model imported
- [ ] Look for dollar sign handling issues

**Status**: ⚠️ PENDING

---

## Key Search Patterns

| Issue | Search For | Should Find | Loaders 1-4 Status |
|-------|-----------|-------------|-------------------|
| HTML rendering fix | `textwrap.dedent` | Python module imported + used on HTML | ❌ Missing |
| Full-width display | `100vw` + `html-dashboard` | UUID-based scoped CSS | ❌ Missing |
| Duration calculation | `hours_in_dataset` | Dynamic calculation from data | ❌ Likely hardcoded |
| Decay cost model | `decay_model` | Module imported and used | ❌ Missing |
| Physics calculations | `mini_energy_value_fmt` | Should use user inputs | ⚠️ Verify |
| Dollar sign fix | `${mini_energy_value_fmt}` | $ in HTML, not in format strings | ⚠️ Verify |
| Zero-out logic | `abs(unity_pf - pf_nom) < 0.02` | MPTS baseline check | ⚠️ Verify |

---

## Reference Files to Compare

**Source of Truth**:
- `eVision/action/loader6.py` - Latest implementation (all fixes applied)
- `eVision/action/loader5.py` - Intermediate implementation
- `eVision/action/decay_model.py` - Physics module reference
- `eVision/action/dataviewer.py` - UI input reference

**Key Sections to Reference**:
- **Loader 6 HTML fix**: Lines ~700-900 (textwrap.dedent + HTML template)
- **Loader 6 Physics calcs**: Lines ~629-723 (hours_in_dataset + zero-out logic)
- **Loader 6 Decay integration**: Lines ~700-850 (decay cost calculations)
- **Dataviewer inputs**: Lines ~114-206 (Equipment Cost input + returns)

---

## Expected Findings

**Loaders 1-4 likely have**:
- ❌ No `import textwrap` → HTML renders as markdown text
- ❌ No `import uuid` → No full-width CSS fix
- ❌ Hardcoded `8760` hours → Physics calculations wrong for short datasets
- ❌ No decay_model import → No equipment decay cost shown
- ⚠️ MPTS simulation logic → Need to verify zero-out behavior
- ⚠️ Physics formulas → Might have dollar sign handling issues

---

## Next Steps

1. Run the quick check commands above
2. Review findings for each loader
3. Update this checklist with actual findings
4. Proceed to Phase 2 (HTML fix) with findings in mind

---

**This is a living document - update as you discover the actual state of each loader.**
