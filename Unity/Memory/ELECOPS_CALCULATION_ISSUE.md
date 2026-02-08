# ElecOps Calculation Issue

## Problem
The current `dashboard_utils.py` (lines 493-538) calculates ElecOps as:
- `operations_pct = (avg_kva / target_pattern_kva) * 100`
- `deviation_pct = 100 - operations_pct`

This treats `target_pattern_kva` as the **maximum expected**, showing ↓ when below and ↑ when above.

## Correct Interpretation
Per Mr. Howell's explanation:
- Each month has a **baseline target**  
- ElecOps measures days that were **above or below** the baseline
- Example: "17 days were targeted, 5.5 days above target" means ↑ 17.7%

## Needed Fix
The ElecOps calculation in `dashboard_utils.py` should:
1. Use the target as a **baseline** (not maximum)
2. Calculate percentage of days above/below baseline
3. Display ↑ when above baseline, ↓ when below

## Affected Files
- `/Users/mdhowell/eestream/eBehavior/dashboard/dashboard_utils.py` (lines 493-538)
- `/Users/mdhowell/eestream/eBehavior/dashboard/templates/eUnitySummaryboard.html` (lines 989, 1061, 1133, 1205) - **FIXED** (changed OPERATIONS to ElecOps)

## Status
Template label fixed (OPERATIONS → ElecOps). Python calculation logic needs to be reviewed and updated per Mr. Howell's requirements.

## Last Updated
2026-01-04
