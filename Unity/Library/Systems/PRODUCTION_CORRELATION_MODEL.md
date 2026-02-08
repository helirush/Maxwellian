# Energy-Weighted Production Correlation Model

**Category:** System Architecture & Educational Framework  
**Status:** Production Active ✅  
**Last Updated:** 2025-12-14  
**Implementation:** `/eBehavior/dashboard/dashboard_utils.py`

---

## Mission Statement

**We are translating 100 years of invisible electrical energy into the native language of industrial operations.**

Plant managers think in **chickens**, data centers think in **transactions**, cold storage thinks in **cubic feet**. Not kilowatts, not kilovolt-amperes, not reactive power.

This model creates **cognitive anchoring** between abstract electrical metrics and concrete production outputs that operators measure obsessively. It's not just data presentation—it's industrial energy education through behavioral association.

---

## The 100-Year Problem

Electrical energy became **invisible infrastructure** after Edison and Tesla won. Like plumbing or HVAC, it disappeared into the walls. You pay the bill. You never question it. The expertise became siloed in electrical engineering departments, disconnected from operations.

**The Unity System restores energy consciousness** by speaking the language operators already speak.

---

## Core Principle: Energy-Weighted Allocation

### Mathematical Foundation

Given:
- **Facility-wide production**: P (e.g., 975,000 birds/week)
- **N transformers** with average power consumption: kW₁, kW₂, ..., kWₙ
- **Total facility power**: kW_total = Σ kWᵢ

For each transformer i:

```
Energy Share (%) = (kWᵢ / kW_total) × 100

Allocated Production = P × (Energy Share / 100)

Energy per Unit = Total kWh / Allocated Production

Cost per Unit = (Total kWh × $/kWh) / Allocated Production
```

### Why This Works

**We don't need to know:**
- Which transformer powers which operation
- Process flow diagrams
- Equipment assignments
- Engineering schematics

**We only need:**
- Total facility energy consumption
- Total facility production output
- The operator's daily experience

**The correlation emerges naturally** as operators observe patterns over weeks/months.

---

## Universal Application

This model works for **any industrial facility** with multiple transformers and measurable primary output:

| Industry | Primary Output | Allocation Unit |
|----------|---------------|-----------------|
| **Poultry Processing** | 975,000 birds/week | Birds per transformer |
| **Data Centers** | 1M transactions/day | Transactions per transformer |
| **Cold Storage** | 500K cubic feet | Cu.ft. maintained per transformer |
| **Tire Manufacturing** | 50K tires/week | Tires per transformer |
| **Pharmaceuticals** | 10K batches/month | Batches per transformer |
| **Food Processing** | 2M lbs product/week | Pounds per transformer |

**The pattern is universal:** Energy consumption → Production allocation → Native language metrics

---

## Educational Psychology

### Cognitive Anchoring Through Association

**Week 1:** "Huh, T10 shows 243,750 birds... interesting"  
**Week 2:** "T10 normally correlates to ~244k birds per month"  
**Week 3:** "Wait, T10 energy dropped AND my bird count is down"  
**Week 4:** "I understand my energy now—it's production visibility"

### The Mental Bridge

```
Abstract Domain          →    The Bridge    →    Concrete Domain
──────────────────────────────────────────────────────────────────
1,318 kW average         ↔    243,750 birds  ↔    "That's my production"
978,063 kWh consumed     ↔    0.79 kWh/bird  ↔    "My efficiency metric"
$215,179 electricity     ↔    $0.17/bird     ↔    "My unit cost"
237 kW reactive waste    ↔    Energy anomaly ↔    "Equipment issue"
```

### Learning Progression

**Phase 1 - Observation (Weeks 1-2)**
- Dashboard shows numbers in native language
- Operators notice patterns
- No electrical knowledge required

**Phase 2 - Correlation (Weeks 3-6)**
- "When T10 runs at 1,300 kW, I process ~244k birds"
- "When energy drops, production drops"
- Natural behavioral association forms

**Phase 3 - Prediction (Weeks 7-12)**
- "T10 is running low today—I bet we're behind schedule"
- "Energy spiked but production didn't—something's wrong"
- Energy becomes a **leading indicator**

**Phase 4 - Optimization (Month 4+)**
- "If I shift load to T12, I could save $0.02/bird"
- "This transformer is wasting energy—it's costing me birds"
- Full operational awareness of energy-production relationship

---

## Implementation Details

### Function: `calculate_energy_weighted_production_allocation()`

**Location:** `/eBehavior/dashboard/dashboard_utils.py`

**Inputs:**
```python
transformer_power_list = [
    ('T10.AirChiller_AN53111387', 1318.0, 978063),    # (name, avg_kW, total_kWh)
    ('T12.Main_AN54021613', 2100.2, 1560150),
    ('T15.Fillet_AN53110845', 1650.8, 1226094),
    ('T16.Compressor_AN54022983', 1845.5, 1370685)
]
facility_production_per_week = 975000  # birds
days_in_period = 31
cost_per_kwh = 0.2198
```

**Outputs:**
```python
{
    'T10.AirChiller_AN53111387': {
        'energy_share_pct': 21.8,
        'allocated_units': 907125,           # birds for entire period
        'allocated_units_per_week': 204750,  # birds per week
        'energy_per_unit': 1.078,            # kWh/bird
        'cost_per_unit': 0.237,              # $/bird
        'total_kwh': 978063,
        'total_cost': 214968.25,
        'avg_kw': 1318.0
    },
    # ... T12, T15, T16
}
```

### Dashboard Display

**Summary Dashboard - Each Transformer Card Shows:**
```
┌─────────────────────────────────────┐
│ T10.AirChiller (3000 kVA)          │
│                                     │
│    [Power Factor Gauge: 84.7%]     │
│                                     │
│  TRANSFORMER ENERGY FIELD          │
│  Production ↑ 5.4%                 │
│                                     │
│  Energy per Bird: 1.078 kWh        │  ← Energy-weighted
│  Cost per Bird: $0.237             │  ← allocation
│  Allocated: 204,750 birds/wk       │  ← based on share
│                                     │
│  Pattern: 5-day production cycle.   │
│  Weekday peaks ~2700 kW, weekend   │
│  lows ~300 kW...                   │
│                                     │
│  Active Usage: 1318.0 kW           │
│  Active Cost/hr: $289.88           │
│  Reactive Waste: 237.9 kW          │
│  Waste Cost/hr: $52.29             │
└─────────────────────────────────────┘
```

---

## Real-World Example: Foster Farms Cherry Ave

### Facility Profile
- **4 Transformers:** T10 (Air Chiller), T12 (Main), T15 (Fillet), T16 (Compressor)
- **Production:** 975,000 birds/week (facility-wide)
- **Analysis Period:** January 2025 (31 days)
- **Electricity Rate:** $0.2198/kWh

### Energy-Weighted Allocation Results

| Transformer | Avg kW | Energy Share | Allocated Birds/Week | kWh/Bird | $/Bird |
|-------------|--------|--------------|----------------------|----------|--------|
| **T10** | 1,318.0 | 21.8% | 204,750 | 1.078 | $0.237 |
| **T12** | 2,100.2 | 34.7% | 326,175 | 1.079 | $0.237 |
| **T15** | 1,650.8 | 27.3% | 256,425 | 1.079 | $0.237 |
| **T16** | 1,845.5 | 30.5% | 286,650 | 1.079 | $0.237 |
| **Total** | 6,044.5 | 100% | 975,000 | 1.079 | $0.237 |

### Operator Learning Path

**Month 1 - Baseline Understanding:**
```
Operator: "T10 shows 204k birds/week... but that's just the air chiller?"
Unity: "Think of it as T10's 'production responsibility' based on energy use"
Operator: "Okay, I'll watch the pattern"
```

**Month 2 - Pattern Recognition:**
```
Operator: "T10 dropped to 1,100 kW this week"
Unity Dashboard: "Allocated birds decreased to 170k/week"
Operator: "Hmm, and we were behind schedule... correlation?"
```

**Month 3 - Correlation Confidence:**
```
Operator: "T10 is my canary—when it dips, I know production is off"
Manager: "How'd you know we'd miss target this week?"
Operator: "T10's energy was low Monday-Wednesday"
```

**Month 6 - Operational Integration:**
```
Operator: "T10 is running 0.05 kWh/bird over baseline"
Operator: "That's costing us $0.01/bird × 200k birds = $2k/week"
Operator: "Maintenance crew—check the air chiller compressor"
```

---

## Benefits by Stakeholder

### **Plant Manager**
- "I can see energy efficiency in birds/dollars, not technical metrics"
- "I understand which transformer impacts production most"
- "Energy anomalies alert me to operational issues immediately"

### **CFO**
- "Cost per bird is a KPI I already track—now I see energy's role"
- "I can justify energy efficiency investments with production impact"
- "$0.01/bird savings × 975k birds/week = $507k/year—that's ROI"

### **Operations Director**
- "Energy is now a leading indicator for production planning"
- "I can optimize transformer loading based on production schedules"
- "Shift planning considers both labor AND energy costs per bird"

### **Maintenance Engineer**
- "When per-bird energy increases, I know equipment is degrading"
- "Preventive maintenance is prioritized by production impact"
- "Energy anomalies guide troubleshooting before production fails"

### **Energy Manager**
- "Finally, operations cares about energy because it speaks their language"
- "Demand response programs can be tied to bird production schedules"
- "Power factor corrections show up as $/bird improvements"

---

## Technical Notes

### Assumptions & Limitations

**Assumptions:**
1. Facility production is relatively stable week-to-week
2. All transformers contribute to primary production output
3. Energy consumption correlates with operational intensity
4. Baseline production rate is known (e.g., 975k birds/week)

**Limitations:**
1. Does not account for transformer-specific operations (e.g., support vs. production)
2. Assumes proportional energy-production relationship
3. Seasonal production variations require recalibration
4. New equipment installations may skew historical patterns

**Calibration:**
- Update `facility_production_per_week` quarterly based on actual output
- Adjust for seasonal variations (e.g., summer production dips)
- Recalculate after major equipment changes or expansions

### Data Requirements

**Minimum Required:**
- Transformer average kW (from energy monitoring)
- Facility production output (from operations tracking)
- Analysis period duration (days)
- Electricity rate ($/kWh)

**Optional Enhancements:**
- Historical production data for trend analysis
- Shift schedules for load correlation
- Equipment run-time logs for validation

---

## Future Enhancements

### Planned Features

**Multi-Product Facilities:**
- Handle facilities producing multiple products (e.g., whole birds + parts)
- Weight allocation by product energy intensity
- Separate dashboards per product line

**Dynamic Recalibration:**
- Auto-adjust allocation as production rates change
- Detect seasonal patterns and apply corrections
- Machine learning to predict optimal allocations

**Comparative Benchmarking:**
- Compare per-unit metrics across facilities
- Industry baselines for energy efficiency
- Best-in-class performance targets

**Advanced Correlations:**
- Weather impact on energy-production relationship
- Time-of-day production efficiency analysis
- Equipment degradation curves

### Under Consideration

- **Voice interface:** "Alexa, what's T10's bird allocation today?"
- **Predictive alerts:** "T10 energy declining—expect 15k fewer birds this week"
- **Mobile dashboard:** Production managers monitor from anywhere
- **API integration:** Feed per-unit metrics to ERP systems

---

## References

- Implementation: `/eBehavior/dashboard/dashboard_utils.py` (calculate_energy_weighted_production_allocation)
- Dashboard Integration: `/eBehavior/dashboard/dashboard_utils.py` (extract_summary_dashboard_values)
- Template: `/eBehavior/dashboard/templates/eUnitySummaryboard.html`
- Related: `PATTERN_RECOGNITION_SYSTEM.md` (behavioral analysis)

---

## Philosophical Foundation

> "The most powerful way to teach is through the language the student already speaks."

For 100+ years, electrical energy has been explained in watts, volts, and amperes. Industrial operators learned to ignore it because it wasn't in their language.

**The Unity System doesn't teach electrical engineering.**  
**It teaches energy consciousness through production correlation.**

When a plant manager sees "0.79 kWh/bird" instead of "978,063 kWh/month," they understand immediately. When that number increases to "0.85 kWh/bird," they know exactly what it costs them: production efficiency loss.

This is not just better data visualization. **This is industrial energy education through cognitive anchoring.**

Welcome to the energy literacy revolution.

---

**Maintainer:** MD Howell, Unity Energy LLC  
**Contributors:** Cove Faraday (Framework Architecture), Agent Mode (Implementation)  
**Version:** 1.0  
**Date:** 2025-12-14
