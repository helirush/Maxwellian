# MPTS Harmonic Reduction in Cooling Calculations
**Implemented:** 2026-01-08  
**Issue:** Simulation mode wasn't reducing harmonic contribution to cooling loads

## Problem Statement

When users enabled MPTS simulation mode (`reactive_remaining > 0`), the system was not properly accounting for the 95% reduction in harmonic energy that MPTS technology removes from the field.

### The Physics
- MPTS technology acts as a "vacuum cleaner" for dynamic harmonic heat
- When enabled, MPTS attracts 95% of harmonics to its copper absorption system
- Only 5% of harmonics remain in the field (if `reactive_remaining = 5%`)
- This dramatically reduces the Harmonic Heat Index (HHI) component
- Reduced HHI cascades through to lower cooling requirements

## Solution Implemented

### File Modified
`core/ePerformance.py` (lines 2659-2666, 2675, 2723)

### Changes Made

1. **Harmonic Adjustment Logic** (lines 2659-2666):
```python
# MPTS SIMULATION MODE: Adjust harmonics based on reactive_remaining
adjusted_thd = avg_thd_itotal
if reactive_remaining > 0:
    # MPTS attracts 95% of harmonics - only reactive_remaining % stays in field
    adjusted_thd = avg_thd_itotal * (reactive_remaining / 100.0)
    print(f"   MPTS Simulation Mode: Harmonics reduced from {avg_thd_itotal:.2f}% to {adjusted_thd:.2f}% ({100-reactive_remaining:.0f}% reduction)")
```

2. **Pass Adjusted Value to Heat Calculations** (line 2675):
```python
avg_thd=adjusted_thd,  # Unity Composite iTHD (adjusted for MPTS if enabled)
```

3. **Diagnostic Output** (line 2723):
```python
print(f"   HHI factor: {heat_metrics.hhi_factor:.3f} (from THD: {adjusted_thd:.2f}%)")
```

## Impact

### Baseline Mode (`reactive_remaining = 0%`)
- No adjustment made
- THD used as-is from measurements
- Full harmonic heat contribution calculated
- **Example:** 32.4% THD → 32.4% used in HHI calculation

### MPTS Simulation Mode (`reactive_remaining = 5%`)
- Harmonics reduced to 5% of baseline
- 95% harmonic heat removed from field
- Cooling loads reduced proportionally
- **Example:** 32.4% THD → 1.62% used in HHI calculation (95% reduction)

## Calculation Flow

```
Measured THD (32.4%)
    ↓
MPTS Adjustment (if enabled)
    ↓
Adjusted THD (1.62% if reactive_remaining=5%)
    ↓
compute_heat_quantification()
    ↓
HHI Factor Calculation (_compute_hhi_factor)
    ↓
BTU Amplification (btu_after_hhi)
    ↓
Cooling Load (cooling_kw_required)
```

## Testing Recommendations

1. Run baseline study (`reactive_remaining = 0%`)
   - Verify THD not adjusted
   - Record cooling loads

2. Run simulation study (`reactive_remaining = 5%`)
   - Verify THD reduced by 95%
   - Verify cooling loads reduced
   - Compare HHI factors between modes

3. Validate against physics:
   - Higher reactive_remaining = more harmonics remain = higher cooling
   - Lower reactive_remaining = fewer harmonics = lower cooling

## Key Formula

**Harmonic Adjustment:**
```
adjusted_thd = measured_thd × (reactive_remaining / 100)
```

**Example:**
- Measured THD: 32.4%
- Reactive Remaining: 5%
- Adjusted THD: 32.4% × 0.05 = 1.62%
- Harmonic Heat Reduction: 95%

## Notes

- This adjustment only affects simulation mode (reactive_remaining > 0)
- Baseline measurements remain unchanged (reactive_remaining = 0)
- The reduction applies to the HHI (Harmonic Heat Index) component of thermal burden
- Cooling savings from harmonic reduction are now properly captured in cost calculations
