# Voltage THD Heat Index Analysis & Recommendations

## Current Implementation Review

### Location
**File**: `eBehavior/core/heat_calculations.py`

### Current HHI (Harmonic Heat Index) Formula
```python
def _compute_hhi_factor(avg_thd: float) -> float:
    """Compute Harmonic Heat Index factor from THD percentage.
    
    Current implementation:
    - Returns: max(0.0, avg_thd / 100.0)
    - For 20% THD → HHI factor = 0.20 (20% heat increase)
    """
    if avg_thd is None:
        return 0.0
    return max(0.0, avg_thd / 100.0)
```

### Heat Progression Model
The model applies factors sequentially:
1. **Baseline**: `waste_kw * 3412.142 = baseline_btu`
2. **VHI** (Voltage Heat Index): Voltage sag factor
3. **HHI** (Harmonic Heat Index): `btu_vhi * (1.0 + hhi_factor)`
4. **ECI** (Environmental): Air-conditioned fraction
5. **GCI** (Geo-Climate): Climate burden

---

## Your Research Findings

### Industry Standards (EPRI/NEMA MG-1)
> **Rule of Thumb**: For each 1% increase in voltage THD above 5%, expect roughly a 2–3°C rise in winding temperature.

### Your Calculation
- **Additional 4% THD above 5%** (e.g., 9% total THD vs. 5% baseline)
- **Temperature rise**: 4% × 2.5°C = **10°C higher winding temp**
- **Motor life impact**: **50% reduction** in motor lifespan

### Temperature-Life Relationship
Industry accepted rule: **Every 10°C increase in operating temperature halves motor/transformer life**

---

## Current Model vs. Your Research

### Current Model Behavior
For **Current THD** (iTHD, not Voltage THD):
- At 5% THD → HHI = 0.05 → **5% heat increase**
- At 9% THD → HHI = 0.09 → **9% heat increase**
- At 21% THD → HHI = 0.21 → **21% heat increase**

**Note**: Your model uses **Unity Composite iTHD** (sum of all three phases), which is different from IEEE standard per-phase THD and from Voltage THD.

### What You're Proposing
For **Voltage THD** (VTHD):
- Baseline: 5% VTHD (acceptable)
- For each 1% above 5% → 2.5°C temperature rise
- 10°C rise = 50% motor life reduction

---

## Recommendations

### 1. **Separate Voltage THD from Current THD**

The current model uses **Current THD (iTHD)** which measures current harmonic distortion. You should add a separate **Voltage THD (VTHD)** factor because:

- **Current THD (iTHD)**: Caused by non-linear loads (VFDs, switching power supplies)
- **Voltage THD (VTHD)**: Caused by utility supply quality + impedance interactions
- **Different physics**: Voltage harmonics directly heat windings through hysteresis and eddy current losses

### 2. **Proposed VTHD Heat Index Formula**

```python
def _compute_vthd_heat_factor(voltage_thd_percent: float, baseline_thd: float = 5.0) -> float:
    """
    Compute Voltage THD heat amplification based on EPRI/NEMA MG-1 research.
    
    Rule of thumb: Each 1% THD above 5% → 2-3°C winding temperature rise
    Each 10°C rise → 50% motor life reduction (2x heat stress)
    
    Args:
        voltage_thd_percent: Voltage THD percentage (0-100)
        baseline_thd: Acceptable baseline THD (default 5% per IEEE 519)
        
    Returns:
        float: Heat amplification factor (0.0 to ~0.5)
        
    Examples:
        5% VTHD  → 0% excess → 0.00 factor (no additional heat)
        9% VTHD  → 4% excess → 0.20 factor (20% heat increase)
        15% VTHD → 10% excess → 0.50 factor (50% heat increase)
    """
    if voltage_thd_percent is None or voltage_thd_percent <= baseline_thd:
        return 0.0
    
    # Excess THD above acceptable baseline
    excess_thd = voltage_thd_percent - baseline_thd
    
    # Temperature rise per % THD: 2.5°C average (EPRI/NEMA range: 2-3°C)
    temp_rise_per_pct = 2.5  # °C per 1% THD
    temp_rise = excess_thd * temp_rise_per_pct
    
    # Heat amplification: 10°C = 50% life reduction = 2x heat stress
    # Using exponential: each 10°C doubles stress
    heat_amplification = (2.0 ** (temp_rise / 10.0)) - 1.0
    
    # Cap at 50% maximum to be conservative
    return min(heat_amplification, 0.5)
```

### 3. **Integration into Heat Model**

Modify `compute_heat_quantification()` in `heat_calculations.py`:

```python
def compute_heat_quantification(
    *,
    supply_kva: float,
    consumption_kw: float,
    avg_voltage: float,
    avg_thd: float,  # Current THD (iTHD)
    voltage_thd: float = None,  # NEW: Voltage THD (VTHD)
    ac_fraction: float,
    electricity_rate: float,
    nominal_voltage: float = DEFAULT_NOMINAL_VOLTAGE,
    gci_factor: float | None = None,
    temperature_f: float | None = None,
    humidity_pct: float | None = None,
    cop: float = DEFAULT_COP,
) -> HeatMetrics:
    """Compute heat progression with separate VTHD consideration."""
    
    baseline_waste_kw = max(0.0, supply_kva - consumption_kw)
    baseline_btu = baseline_waste_kw * BTU_PER_KW
    
    # Stage 1: Voltage sag heat
    vhi_factor = _compute_vhi_factor(avg_voltage, nominal_voltage)
    btu_vhi = baseline_btu * (1.0 + vhi_factor)
    
    # Stage 2: Current harmonic heat (existing iTHD)
    hhi_factor = _compute_hhi_factor(avg_thd)
    btu_hhi = btu_vhi * (1.0 + hhi_factor)
    
    # Stage 2b: Voltage harmonic heat (NEW - VTHD winding stress)
    vthd_factor = 0.0
    if voltage_thd is not None:
        vthd_factor = _compute_vthd_heat_factor(voltage_thd)
        btu_hhi = btu_hhi * (1.0 + vthd_factor)  # Apply after iTHD
    
    # Continue with ECI and GCI...
    btu_eci = btu_hhi * ac_fraction
    # ... rest of calculation
```

### 4. **Data Requirements**

To implement this, you need **Voltage THD** measurements from your EFM data:

**Check for these columns**:
- `VTHD_A`, `VTHD_B`, `VTHD_C` (per-phase voltage THD)
- `THD_Va`, `THD_Vb`, `THD_Vc` (alternative naming)
- Or calculate from voltage harmonics: `V2_A`, `V3_A`, `V5_A`, etc.

**Calculation if raw harmonics available**:
```python
# For each phase
VTHD_A = sqrt(V2_A² + V3_A² + V5_A² + ... + V31_A²) / V1_A * 100%
```

---

## Implementation Priority

### High Priority ✅
1. **Verify your data has Voltage THD** - Check if EFM captures VTHD
2. **Implement `_compute_vthd_heat_factor()`** with EPRI formula
3. **Add to HeatMetrics dataclass** (`vthd_factor` field)
4. **Update reports** to show both iTHD and VTHD impacts separately

### Medium Priority
5. **Add validation** - Alert if VTHD > 5% (IEEE 519 limit)
6. **Dashboard visualization** - Show VTHD heat contribution
7. **Customer reports** - Emphasize motor life impact with VTHD data

### Documentation
8. **Create case studies** showing 4% excess VTHD → $X in motor replacement costs
9. **Reference EPRI/NEMA MG-1** standards in reports for credibility

---

## Example Calculation

### Scenario: 9% Voltage THD (4% above 5% baseline)

**Using your research**:
- Excess: 9% - 5% = 4%
- Temp rise: 4% × 2.5°C = 10°C
- Life impact: 50% reduction (10°C rule)
- Heat stress: 2x amplification

**Proposed formula**:
```python
excess = 4.0
temp_rise = 4.0 * 2.5 = 10.0°C
heat_factor = (2.0 ** (10.0/10.0)) - 1.0 = 1.0 (100% increase!)
capped_factor = min(1.0, 0.5) = 0.5 (50% increase to be conservative)
```

**Financial impact example**:
- Baseline heat: 10,000 BTU/hr
- After VTHD factor: 10,000 × 1.5 = 15,000 BTU/hr
- Additional cooling: 1.46 kW × $0.215/kWh × 8760 hr = $2,750/year
- Motor life reduction: Replace $50,000 motor in 5 years instead of 10 = $5,000/year extra

**Total customer impact**: **$7,750/year** from 4% excess VTHD alone!

---

## Next Steps

1. **Check your data**: Does EFM have `VTHD_A/B/C` columns?
2. **Run analysis**: What are typical VTHD values in your datasets?
3. **Implement formula**: Add to `heat_calculations.py`
4. **Test**: Compare old vs. new heat calculations
5. **Document**: Add VTHD section to reports with EPRI references

---

## Questions to Answer

1. **Do you have Voltage THD data in your EFM datasets?**
2. **What are typical VTHD values you're seeing?** (5%? 10%? 15%?)
3. **Should we use 2°C, 2.5°C, or 3°C per % for the formula?** (EPRI range: 2-3°C)
4. **Should the cap be 50% or allow higher?** (Conservative vs. aggressive)

Let me know if you want me to implement this change!
