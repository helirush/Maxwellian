# VTHD Heat Factor - Quick Reference Card

## Formula Summary

```python
# Voltage THD Heat Factor (Exponential Scaling)
excess_thd = voltage_thd_percent - 5.0  # IEEE 519 baseline
temp_rise_celsius = excess_thd × 2.5    # EPRI rule: 2.5°C per 1% THD
heat_factor = (2.0 ** (temp_rise / 10.0)) - 1.0  # Exponential
vthd_factor = min(heat_factor, 0.5)    # Capped at 50%
```

## Quick Lookup Table

| VTHD% | Excess | Temp Rise | Heat Factor | Life Impact | Annual Cost* |
|-------|--------|-----------|-------------|-------------|--------------|
| 5%    | 0%     | 0°C       | 0.000       | Normal      | $0           |
| 6%    | 1%     | 2.5°C     | 0.189       | 84% life    | ~$69k        |
| 7%    | 2%     | 5.0°C     | 0.414       | 71% life    | ~$151k       |
| 8%    | 3%     | 7.5°C     | 0.500 ⚠️    | 67% life    | ~$182k       |
| **9%** | **4%** | **10.0°C** | **0.500** ⚠️ | **67% life** | **~$363k** ⭐ |
| 10%   | 5%     | 12.5°C    | 0.500 ⚠️    | 67% life    | ~$363k       |
| 12%   | 7%     | 17.5°C    | 0.500 ⚠️    | 67% life    | ~$363k       |
| 15%   | 10%    | 25.0°C    | 0.500 ⚠️    | 67% life    | ~$363k       |

*Based on 2,500 kVA transformer, $0.215/kWh, 75% AC

⚠️ = Capped at maximum factor (conservative modeling)

## Key Thresholds

### IEEE 519 Standards
- **✅ 0-5%**: Acceptable voltage quality
- **⚠️ 5-8%**: Caution - equipment stress increasing
- **❌ >8%**: Violation - serious concern

### EPRI Temperature Rules
- **1% excess VTHD** → **2.5°C** winding temperature rise
- **10°C rise** → **50% motor life reduction**
- **20°C rise** → **75% motor life reduction**

### Financial Impact (Example: 2,500 kVA)
- **6% VTHD** (1% excess): +$69k/year
- **9% VTHD** (4% excess): +$363k/year ⭐ **Your example**
- **12% VTHD** (7% excess): +$363k/year (capped)

## Use Cases

### Low VTHD (3-5%)
- ✅ Clean utility supply
- ✅ Good power quality
- ✅ No additional heat penalty
- **Action**: Monitor, no immediate concern

### Moderate VTHD (6-7%)
- ⚠️ Minor power quality issues
- ⚠️ 16-29% motor life reduction
- ⚠️ $69k-$151k additional annual cost
- **Action**: Investigate sources, plan mitigation

### High VTHD (8-10%)
- ❌ Significant power quality problems
- ❌ 33% motor life reduction
- ❌ ~$363k additional annual cost
- **Action**: Immediate mitigation required

### Critical VTHD (>10%)
- 🚨 Severe power quality violation
- 🚨 33% motor life reduction (capped model)
- 🚨 ~$363k+ additional annual cost
- **Action**: Emergency response, equipment at risk

## Customer Talking Points

### The Problem
> "Your facility has **9% Voltage THD**, which is **4% above** the IEEE 519 standard of 5%. According to EPRI research, each 1% above 5% increases motor winding temperature by 2.5°C."

### The Impact
> "At 9% VTHD, your motors are running **10°C hotter** than they should. Industry standards show this reduces motor life by **33%** - a 10-year motor now lasts only **6.7 years**."

### The Cost
> "This excess heat requires **$363,000/year** in additional cooling costs, plus accelerated motor replacement. A $50,000 motor that should last 10 years now needs replacing after 7 years, costing an extra **$2,500/year**."

### The Solution
> "Unity's voltage conditioning technology can reduce VTHD to acceptable levels, eliminating this **$365,000/year** burden while extending your motor life back to normal."

## Integration Checklist

### Phase 1: Verify Data ✅
- [ ] Check for VTHD columns in CSV files
- [ ] Confirm VTHD values are reasonable (0-20%)
- [ ] Calculate average VTHD per phase

### Phase 2: Code Integration
- [ ] Extract VTHD in `ePerformance.py`
- [ ] Pass `voltage_thd` to heat calculations
- [ ] Store VTHD metrics in analysis summary

### Phase 3: Reporting
- [ ] Add VTHD to energy health reports
- [ ] Display VTHD warnings when > 5%
- [ ] Show motor life impact calculation
- [ ] Include EPRI/NEMA MG-1 references

### Phase 4: Customer Value
- [ ] Create VTHD case studies
- [ ] Develop ROI calculators
- [ ] Train sales team on VTHD messaging
- [ ] Add VTHD to proposal templates

## Code Snippets

### Check for VTHD in Data
```python
# Check if VTHD columns exist
vthd_columns = ['VTHD_A', 'VTHD_B', 'VTHD_C']
has_vthd = all(col in df.columns for col in vthd_columns)

if has_vthd:
    avg_vthd = (df['VTHD_A'].mean() + 
                df['VTHD_B'].mean() + 
                df['VTHD_C'].mean()) / 3
    print(f"Average VTHD: {avg_vthd:.1f}%")
else:
    print("⚠️ VTHD data not available")
```

### Calculate VTHD Impact
```python
from core.heat_calculations import _compute_vthd_heat_factor

vthd_percent = 9.0  # Your example
vthd_factor = _compute_vthd_heat_factor(vthd_percent)
temp_rise = (vthd_percent - 5.0) * 2.5
life_reduction = (1 - 1/(1 + vthd_factor)) * 100

print(f"VTHD: {vthd_percent:.1f}%")
print(f"Temperature rise: {temp_rise:.1f}°C")
print(f"Heat factor: {vthd_factor:.3f}")
print(f"Motor life reduction: {life_reduction:.0f}%")
```

### Include in Heat Calculation
```python
heat_metrics = compute_heat_quantification(
    supply_kva=2500.0,
    consumption_kw=2100.0,
    avg_voltage=470.0,
    avg_thd=21.0,           # Current THD (iTHD)
    voltage_thd=9.0,        # Voltage THD (VTHD) ⭐
    ac_fraction=0.75,
    electricity_rate=0.215
)

print(f"VTHD factor: {heat_metrics.vthd_factor:.3f}")
print(f"Cooling w/ VTHD: {heat_metrics.cooling_kw_final:.2f} kW")
print(f"Annual cost: ${heat_metrics.cooling_cost_per_year:,.0f}")
```

## References

- **EPRI**: "Effects of Harmonics on Equipment"
- **NEMA MG-1**: Motors and Generators Standard
- **IEEE 519-2014**: Harmonic Control Practices
- **Arrhenius Equation**: Insulation aging temperature dependency

## Contact

Questions about VTHD implementation?
- Review: `/eBehavior/VTHD_IMPLEMENTATION_SUMMARY.md`
- Test: `python test_vthd_heat_factor.py`
- Analysis: `/eBehavior/VOLTAGE_THD_HEAT_ANALYSIS.md`
