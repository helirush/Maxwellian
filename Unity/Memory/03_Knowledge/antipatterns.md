# Anti-Patterns - Unity Energy eestream System

---
**File**: `antipatterns.md`  
**Tag**: `eMemory.knowledge.antipatterns.lessons`  
**Category**: 03_Knowledge  
**Agent**: COLLABORATIVE  
**Created**: 2025-10-16  
**Last Updated**: 2025-10-29  
**Status**: ACTIVE  
**Importance**: HIGH  
**Related**: `systemPatterns.md`, `decisions.md`, `progress.md`  
---

## Purpose
This document captures **what NOT to do** based on actual bugs, issues, and mistakes encountered during development. Each anti-pattern includes the problem, why it's bad, and the correct approach.

Learning from mistakes is faster than learning from scratch.

---

## Code Anti-Patterns

### AP-001: Hardcoded Template Values

**❌ Anti-Pattern**:
```html
<!-- eUnitySiteboard.html - BAD EXAMPLE -->
<h2>T12.Main</h2>
<h2>T15.Fillet</h2>
<h2>T16.Compressor</h2>
```

**Why It's Bad**:
- Creates "ghost" transformer cards for data that doesn't exist
- Confuses users with fake information
- Template cannot adapt to different datasets
- Manual editing required for every dataset change

**✅ Correct Approach**:
```html
<!-- Use dynamic data bindings -->
<h2>
  <span id="xfmr2-name"></span>
  <span id="xfmr2-kva-wrap"> (<span id="xfmr2-kva">2500</span> kVA)</span>
</h2>
```

**CSS Auto-Hide**:
```css
.transformer-card:has(span[id$="-name"]:empty) {
  display: none;
}
```

**Lesson**: Always use data bindings, never hardcode placeholder data in templates.

**Incident**: Summaryboard showing fake T12/T15/T16 transformers (October 28, 2025)

---

### AP-002: Calling Undefined Functions

**❌ Anti-Pattern**:
```python
# voltboard_generator.py - BAD EXAMPLE
customized_template = apply_data_bindings(
    html=customized_template,
    data=canonical_data,
    trace_mode=False
)
```

**Why It's Bad**:
- Crashes at runtime with `NameError: name 'apply_data_bindings' is not defined`
- Function was removed/refactored but calls weren't updated
- No static type checking caught the error
- Users see cryptic error messages

**✅ Correct Approach**:
```python
# Check imports and use correct function
from dashboard.dashboard_utils import update_html_by_ids

customized_template = update_html_by_ids(
    html_content=customized_template,
    replacements=canonical_data
)
```

**Prevention**:
- Always verify function existence before calling
- Check imports match function names
- Match parameter names exactly to function signature
- Use IDE autocomplete to verify function availability

**Lesson**: Comments like "removed/refactored" should trigger immediate verification of all call sites.

**Incident**: Voltage dashboard generation failure (October 27, 2025)

---

### AP-003: Creating Directories Before Checking Data Count

**❌ Anti-Pattern**:
```python
# eeBEHAVIOR.py - BAD EXAMPLE
# Always create SITE directory regardless of dataset count
site_directory = create_directory(f"SITE_{facility_name}")
generate_set_dashboards(analysis_summaries, site_directory)
```

**Why It's Bad**:
- Creates unnecessary directories for single-transformer analysis
- Generates redundant SET files when only FIELD files needed
- Clutters output structure
- Confuses users expecting clean single-transformer output

**✅ Correct Approach**:
```python
# Check dataset count BEFORE creating structure
if len(analysis_summaries) == 1:
    # Single dataset - use transformer directory
    output_dir = transformer_directory
    prefix = "FIELD-"
    generate_summaryboard(output_dir, prefix)
else:
    # Multi-dataset - create SET/SITE structure
    site_directory = create_directory(f"SITE_{facility_name}")
    generate_set_dashboards(analysis_summaries, site_directory)
```

**Prevention**:
- Check data conditions before creating file system structure
- Adapt behavior to actual dataset characteristics
- Don't assume Level 2/3 always means multi-transformer

**Lesson**: Directory structure should reflect data reality, not analysis level selection.

**Incident**: Unnecessary SITE directory for single-transformer analysis (October 27, 2025)

---

### AP-004: Mismatched Parameter Names

**❌ Anti-Pattern**:
```python
# Calling function with wrong parameter names
result = process_data(
    html=template_content,  # Wrong name
    data=replacement_dict   # Wrong name
)
```

**Why It's Bad**:
- Causes `TypeError: unexpected keyword argument` errors
- Function signature expects `html_content` and `replacements`
- Parameter name mismatch causes runtime failures
- Harder to debug than syntax errors

**✅ Correct Approach**:
```python
# Match exact parameter names from function signature
result = process_data(
    html_content=template_content,
    replacements=replacement_dict
)
```

**Prevention**:
- Read function signatures before calling
- Use IDE parameter hints
- Copy-paste parameter names from function definition
- Check function documentation

**Lesson**: Parameter names are part of the API contract. Match them exactly.

**Incident**: Voltage dashboard `apply_data_bindings()` call (October 27, 2025)

---

### AP-005: Using Wrong Function from Module

**❌ Anti-Pattern**:
```python
# eeBEHAVIOR.py - BAD EXAMPLE
from dashboard.heat_dashboard_generator import generate_heat_model_dashboard

# Later...
generate_heat_model_dashboard(analysis_summary, csv_file_path, ...)
# This function has placeholder dashes, not live data
```

**Why It's Bad**:
- Calls outdated/deprecated function instead of working version
- Results in placeholder dashes (`—`) instead of calculated values
- Multiple versions of same functionality cause confusion
- Hard to debug because function "works" but produces wrong output

**✅ Correct Approach**:
```python
# Use correct function from working renderer
from dashboard.working_renderer import generate_heat_dashboard_for_analysis as generate_heat_dashboard

# Later...
generate_heat_dashboard(analysis_summary, analysis_dir_path, ...)
# This function properly binds all template IDs
```

**Prevention**:
- Verify which module contains "working" version
- Check template binding coverage before using generator
- Run verification scripts to confirm 100% binding coverage
- Deprecate old functions clearly or remove them

**Lesson**: When multiple implementations exist, verify you're using the correct one.

**Incident**: Heat dashboard showing placeholder dashes (October 19, 2025)

---

### AP-006: Missing Script Tag Wrappers

**❌ Anti-Pattern**:
```html
<!-- Template with inline JavaScript - BAD EXAMPLE -->
<script src="../static/unity-dashboard.js"></script>
  document.addEventListener('DOMContentLoaded', () => {
    // JavaScript code here
  });
</script>
```

**Why It's Bad**:
- Missing opening `<script>` tag before inline JavaScript
- Causes JavaScript template literal errors
- Browser fails to execute code correctly
- Hard to spot visually in large templates

**✅ Correct Approach**:
```html
<!-- Properly wrapped inline JavaScript -->
<script src="../static/unity-dashboard.js"></script>
<script>
  document.addEventListener('DOMContentLoaded', () => {
    // JavaScript code here
  });
</script>
```

**Prevention**:
- Always wrap inline JavaScript in `<script>` tags
- Use editor syntax highlighting to catch issues
- Validate HTML with W3C validator
- Test dashboards in browser console

**Lesson**: Every JavaScript block needs proper opening and closing `<script>` tags.

**Incident**: Summaryboard JavaScript errors (October 28, 2025)

---

## Data Anti-Patterns

### AP-101: Assuming Data Format Without Validation

**❌ Anti-Pattern**:
```python
# Processing CSV without checking column count
df = pd.read_csv(filename)
# Assumes 38 columns but file has 223 columns
result = analyze_data(df)
```

**Why It's Bad**:
- Crashes when CSV has unexpected harmonic columns (Har2-Har63)
- Error message: "Expected 38 fields, saw 223"
- No early warning that data format is wrong
- Processing fails late in pipeline after expensive operations

**✅ Correct Approach**:
```python
# Validate data format early
df = pd.read_csv(filename)
expected_columns = 38
if len(df.columns) != expected_columns:
    print(f"⚠️ Unexpected column count: {len(df.columns)} (expected {expected_columns})")
    # Offer to clean/standardize data
    df = remove_harmonic_columns(df)
result = analyze_data(df)
```

**Prevention**:
- Validate data format immediately after loading
- Check column count, names, and types
- Fail fast with clear error messages
- Offer auto-correction for known issues

**Lesson**: Never assume data format. Always validate early.

**Incident**: Q1 2025 merged CSV with 223 columns (October 23, 2025)

---

### AP-102: Ignoring None Values in Calculations

**❌ Anti-Pattern**:
```python
# Attempting calculation without checking for None
total_cost = transformer_cost + domain_cost  # Crashes if domain_cost is None
```

**Why It's Bad**:
- `TypeError: unsupported operand type(s) for +: 'float' and 'NoneType'`
- Crashes instead of showing "n/a" or calculating from available data
- Poor user experience (error instead of graceful degradation)

**✅ Correct Approach**:
```python
# Check for None and calculate if possible
if domain_cost is None and site_480_pct is not None and site_total_cost is not None:
    # Auto-calculate 480v domain cost
    domain_cost = site_total_cost * (site_480_pct / 100.0)
    print(f"💰 Calculated 480v Domain Cost: ${domain_cost:,.0f}")

total_cost = transformer_cost + (domain_cost or 0)
```

**Prevention**:
- Check for None before arithmetic operations
- Auto-calculate from available data when possible
- Provide meaningful defaults or display "n/a"
- Log when calculations are skipped due to missing data

**Lesson**: Missing data should degrade gracefully, not crash.

**Incident**: 480v Domain Cost showing "n/a" (October 18, 2025)

---

## Architecture Anti-Patterns

### AP-201: Configuration Drift Across Modules

**❌ Anti-Pattern**:
```
# Each module has own config file - BAD EXAMPLE
eBehavior/config.py
eVision/config.py
eAudio/config.py
eMarket/config.py
```

**Why It's Bad**:
- API key in one module but not another
- Inconsistent configuration values across modules
- Difficult to update settings (must change 4 files)
- Security risk (keys scattered across codebase)

**✅ Correct Approach**:
```
# Centralized configuration
eConfig/
├── .env (single source of truth)
└── config_loader.py (shared by all modules)
```

**Prevention**:
- Centralize configuration in single location
- All modules import from eConfig
- Use environment variables for secrets
- Maintain `.env.example` template

**Lesson**: Configuration belongs in one place, not scattered across modules.

**Incident**: Configuration drift before June 2025 centralization

---

### AP-202: Duplicate Code Across Generators

**❌ Anti-Pattern**:
```
# Separate generator for each dashboard type - BAD EXAMPLE
dashboard/energyboard_generator.py  (300 lines)
dashboard/heatboard_generator.py    (280 lines)
dashboard/voltboard_generator.py    (290 lines)
# 80% of code is identical parameter replacement logic
```

**Why It's Bad**:
- Bug fixes must be applied to all three files
- Inconsistent behavior across dashboard types
- Maintenance burden increases linearly with dashboard types
- New features require updating multiple files

**✅ Correct Approach**:
```
# Unified generator with template switching
dashboard/unified_dashboard_generator.py
- Single parameter replacement system
- Template-specific logic in separate small modules
- Consistent behavior across all dashboard types
```

**Prevention**:
- Identify common patterns and extract them
- Use template method pattern for shared logic
- Keep dashboard-specific code minimal and isolated

**Lesson**: If you copy-paste code more than twice, create a shared function.

**Incident**: Pre-unified system had code duplication issues

---

## UI/UX Anti-Patterns

### AP-301: Confusing File Naming Patterns

**❌ Anti-Pattern**:
```
# Inconsistent naming with location suffix - BAD EXAMPLE
SET1-Summaryboard_CherryAve-4_Site_1minRES_250901-250930_30d.html
                              ^^^^^ Unwanted suffix in middle
```

**Why It's Bad**:
- "_Site" suffix appears in middle of filename
- Inconsistent with other file naming patterns
- Harder to parse programmatically
- Users confused by extra suffix

**✅ Correct Approach**:
```
# Clean, consistent naming
SET1-Summaryboard_CherryAve-4_1minRES_250901-250930_30d.html
Format: {PREFIX}-{TYPE}_{BASENAME}_{RESOLUTION}_{DATES}_{DURATION}.html
```

**Prevention**:
- Define file naming convention once
- Use helper function for filename generation
- Don't insert variable suffixes in middle of name
- Keep pattern consistent across all file types

**Lesson**: File naming should be predictable and parseable.

**Incident**: Dashboard filename standardization (October 17, 2025)

---

### AP-302: Inaccurate Console Messages

**❌ Anti-Pattern**:
```python
# Console message doesn't match reality - BAD EXAMPLE
print("✅ 3 FIELD dashboards generated: Energy + Heat + Voltage")
# Actually generated 4: Energy + Heat + Voltage + Summary
```

**Why It's Bad**:
- Users expect 3 dashboards but get 4
- Creates confusion and distrust
- Hard to debug when output doesn't match messages
- Breaks user expectations

**✅ Correct Approach**:
```python
# Accurate console message
print("✅ 4 FIELD dashboards generated: Energy + Heat + Voltage + Summary")
# Message matches reality
```

**Prevention**:
- Update console messages when behavior changes
- Count actual outputs, don't hardcode numbers
- Test console output matches file generation
- Use variables for counts when possible

**Lesson**: Console messages are user documentation. Keep them accurate.

**Incident**: Summaryboard generation message (October 28, 2025)

---

## Performance Anti-Patterns

### AP-401: Loading Entire Large File Into Memory

**❌ Anti-Pattern**:
```python
# Loading 500MB CSV into memory at once - BAD EXAMPLE
df = pd.read_csv("huge_dataset.csv")
# System runs out of memory
```

**Why It's Bad**:
- Memory usage spikes to multiple GB
- System becomes unresponsive
- May crash with out-of-memory error
- Poor user experience on systems with limited RAM

**✅ Correct Approach**:
```python
# Process in chunks for large files
chunk_size = 10000
for chunk in pd.read_csv("huge_dataset.csv", chunksize=chunk_size):
    process_chunk(chunk)
# Or use memory-mapped files
```

**Prevention**:
- Check file size before loading
- Use chunked processing for files >100MB
- Implement progress indicators for long operations
- Monitor memory usage during development

**Lesson**: Large datasets require chunked processing, not in-memory loading.

**Status**: Known issue, optimization pending

---

## Testing Anti-Patterns

### AP-501: No Verification After Code Changes

**❌ Anti-Pattern**:
```python
# Making changes without verification - BAD EXAMPLE
def update_dashboard_generator():
    # Change function calls
    # Change parameter names
    # Commit and deploy
    # Hope it works
```

**Why It's Bad**:
- Changes break production without warning
- No verification that all template IDs are bound
- Users see placeholder dashes or errors
- Difficult to identify which change caused the issue

**✅ Correct Approach**:
```python
# Create verification script before and after changes
def verify_dashboard_bindings():
    template_ids = extract_template_ids("template.html")
    bound_ids = extract_bound_ids("generator.py")
    coverage = len(bound_ids) / len(template_ids) * 100
    print(f"Binding coverage: {coverage}% ({len(bound_ids)}/{len(template_ids)})")
    assert coverage == 100, "Not all template IDs are bound!"

# Run verification after changes
verify_dashboard_bindings()
```

**Prevention**:
- Create verification scripts for critical systems
- Run verification before committing changes
- Automate verification in CI/CD pipeline
- Document verification process

**Lesson**: Verification scripts catch bugs before users see them.

**Incident**: Heat dashboard systematic fix included verification script (October 19, 2025)

---

## Summary: Key Principles to Avoid Anti-Patterns

1. **Always validate data early** - Fail fast with clear errors
2. **Never hardcode what should be dynamic** - Use data bindings and configuration
3. **Verify function existence before calling** - Check imports and signatures
4. **Check conditions before creating structures** - Adapt to data reality
5. **Centralize, don't duplicate** - Single source of truth for config and logic
6. **Console messages must match reality** - Update messages when behavior changes
7. **Create verification scripts** - Prove correctness before deployment
8. **Process large data in chunks** - Don't load everything into memory

---

## Contributing to This Document

When you encounter a bug or issue:
1. Document the anti-pattern here AFTER fixing it
2. Include the problematic code and why it's bad
3. Show the correct approach
4. Explain prevention strategies
5. Reference the incident date

**Format**:
```markdown
### AP-###: Anti-Pattern Title

**❌ Anti-Pattern**: [Problematic code]

**Why It's Bad**: [Consequences]

**✅ Correct Approach**: [Better code]

**Prevention**: [How to avoid]

**Lesson**: [Key takeaway]

**Incident**: [When this was encountered]
```

This ensures we learn from every mistake and never repeat the same error twice.
