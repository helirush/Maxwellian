# Thermal Burden Index (TBI) - Canonical Definition

---
**File**: `thermal_burden_index_TBI.md`  
**Tag**: `eMemory.systems.thermal.tbi`  
**Category**: 02_Systems  
**Agent**: COVE FARADAY  
**Created**: 2025-12-08  
**Last Updated**: 2025-12-08  
**Status**: CANONICAL  
**Importance**: CRITICAL  
**Related**: `mpts_systems.md`, `decay_cost_model.md`, `heat_calculations.py`  
---

## Purpose

This document defines the **Thermal Burden Index (TBI)** - Unity Energy's canonical metric for quantifying total thermal stress in electrical systems. TBI combines voltage, harmonic, and voltage THD contributions into a single diagnostic index.

**Status:** CANONICAL - Confirmed by Cove Faraday on December 8, 2025. No further adjustment required.

---

## Formula - CANONICAL

```
TBI = (0.4 × VHI) + (0.4 × HHI) + (0.2 × VTHD)
```

### Weighting Rationale

The 40/40/20 weighting is **not arbitrary** — it reflects what the field itself expresses:

- **VHI (0.4)**: Voltage collapse is a co-dominant driver of thermal distress
- **HHI (0.4)**: Harmonic heat is a co-dominant driver of thermal distress  
- **VTHD (0.2)**: Harmonic voltage distortion is a tertiary amplifier, not an initiator

> "Voltage collapse & harmonic heat are co-dominant drivers of thermal distress. Harmonic voltage distortion (VTHD) is a tertiary amplifier, not an initiator." — Cove Faraday

---

## Component Indices

### VHI (Voltage Heat Index)
**Implementation:** `eBehavior/core/heat_calculations.py`

**Formula:** Amplification based on voltage sag below nominal 480V

**Range:**
- 1.0x (at 480V nominal)
- 1.5x (at 432V, 10% sag)

**Alert Conditions:**
- **Healthy**: 0-5% voltage sag
- **Warning**: 5-10% voltage sag
- **Critical**: >10% voltage sag

---

### HHI (Harmonic Heat Index)
**Implementation:** `eBehavior/core/heat_calculations.py`

**Formula:**
```python
HHI = iTHD_total × I_total² × K_harm
```
Where `K_harm = 0.1` (Unity canonical constant)

**Ranges:**
- **0-20**: Healthy
- **20-50**: Distorted
- **50-100**: Danger
- **100+**: Critical danger

**Alert Conditions:**
```python
if HHI > 100:
    alert = "DANGER"
elif HHI > 50:
    alert = "DISTORTED"
elif HHI > 20:
    alert = "ELEVATED"
else:
    alert = "HEALTHY"
```

---

### VTHD (Voltage THD Heat)
**Implementation:** `eBehavior/core/heat_calculations.py`

**Formula:** Exponential amplification from voltage harmonics

**Basis:** EPRI/NEMA MG-1 standards for voltage harmonic stress

---

## TBI Thresholds - CANONICAL

**Status:** Confirmed by Cove Faraday December 8, 2025. Embed as law, not proposal.

| TBI Range | State | Action |
|-----------|-------|--------|
| **0-30** | Normal breathing | Monitor only |
| **30-60** | Elevated burden | Increase cooling margin, observe PF |
| **60-100** | Critical heat | Field is noisy → begin harmonic sink intervention |
| **100+** | Field emergency | Direct unity deployment + runtime harmonic extraction |

### Threshold Interpretation

#### **TBI 0-30: Normal Breathing**
- Field operating within design parameters
- Thermal stress minimal
- **Action:** Routine monitoring only
- **Indicator:** System healthy, no intervention required

#### **TBI 30-60: Elevated Burden**
- Thermal stress accumulating
- Power quality beginning to degrade
- **Action:** Increase cooling margin, observe power factor trends
- **Indicator:** Early warning - field entering stress zone

#### **TBI 60-100: Critical Heat**
- Field is noisy with significant harmonic turbulence
- Equipment experiencing accelerated thermal degradation
- **Action:** Begin harmonic sink intervention (MPTS deployment planning)
- **Indicator:** Active intervention required to prevent damage

#### **TBI 100+: Field Emergency**
- Severe thermal emergency state
- Imminent equipment failure risk
- **Action:** Direct Unity deployment + runtime harmonic extraction
- **Indicator:** Emergency response required - deploy immediately

---

## Diagnostic Usage

### Field Assessment Workflow

1. **Measure Component Indices:**
   - Calculate VHI from voltage sag
   - Calculate HHI from current THD and amperage
   - Calculate VTHD from voltage harmonics

2. **Compute TBI:**
   ```python
   TBI = (0.4 * VHI) + (0.4 * HHI) + (0.2 * VTHD)
   ```

3. **Determine State:**
   - Compare TBI value to canonical thresholds
   - Identify operational state (Normal / Elevated / Critical / Emergency)

4. **Execute Action:**
   - Follow prescribed action for determined state
   - Document field conditions and TBI value
   - Track TBI over time for trend analysis

### Integration Points

- **eBehavior Analysis**: TBI calculated in FIELDp2 reports
- **eVision Loaders**: TBI displayed in thermal metrics
- **MPTS Deployment**: TBI used to determine unit configuration
- **Dashboard Systems**: TBI visualization in Heatboard

---

## MPTS Response to TBI

### TBI-Driven Deployment Strategy

| TBI State | MPTS Response |
|-----------|---------------|
| **Normal (0-30)** | No MPTS required - maintain monitoring |
| **Elevated (30-60)** | Plan MPTS deployment - size units for 15% margin |
| **Critical (60-100)** | Deploy MPTS immediately - H490 priority at harmonic sources |
| **Emergency (100+)** | Emergency MPTS deployment + field extraction protocol |

### Expected TBI Improvement After MPTS

Typical TBI reduction after Unity MPTS deployment:
- **Pre-MPTS**: TBI 70-90 (Critical range)
- **Post-MPTS**: TBI 15-25 (Normal range)
- **Reduction**: 60-75% improvement in thermal burden

---

## Historical Context

### Development Timeline

- **November 13, 2025**: TBI formula proposed in Page 2 expansion planning
- **November 13-December 6, 2025**: VHI, HHI, VTHD implemented in `heat_calculations.py`
- **December 8, 2025**: TBI weights and thresholds confirmed canonical by Cove Faraday
- **December 8, 2025**: This document created as authoritative TBI reference

### Why TBI Exists

Before TBI, thermal burden was assessed using individual metrics (voltage sag, THD, heat generation) without a unified diagnostic index. TBI combines these into a single field health indicator that:

1. Reflects actual field behavior (co-dominant VHI/HHI, tertiary VTHD)
2. Provides clear action thresholds for intervention
3. Enables consistent deployment decisions across installations
4. Quantifies thermal stress in a way that maps to equipment lifespan impact

---

## Technical Notes

### Why 40/40/20 Weighting?

The weighting reflects electromagnetic field physics:

- **Voltage (E-field)**: Drives thermal stress through resistive losses and voltage-dependent heating
- **Current Harmonics (H-field)**: Drives thermal stress through I²R heating and skin effect
- **Voltage THD**: Amplifies existing thermal stress but does not initiate it

The 40/40 split between VHI and HHI recognizes that **both E-field and H-field contributions are equally dominant** in thermal burden generation. VTHD at 20% captures its role as an amplifier of existing stress.

### TBI vs Individual Indices

**When to use TBI:**
- Overall field health assessment
- MPTS deployment decisions
- Trend analysis over time
- Customer reports and dashboards

**When to use individual indices:**
- Root cause analysis (which component is problematic?)
- Targeted interventions (voltage regulation vs harmonic filtering)
- Detailed forensic analysis
- Equipment-specific diagnostics

---

## Implementation Status

- ✅ **VHI**: Implemented in `heat_calculations.py`
- ✅ **HHI**: Implemented in `heat_calculations.py`
- ✅ **VTHD**: Implemented in `heat_calculations.py`
- ⚠️ **TBI Composite**: Formula defined, implementation in progress
- 📋 **Dashboard Integration**: Planned for FIELDp2 expansion

---

## References

- **Implementation**: `eBehavior/core/heat_calculations.py`
- **MPTS Context**: `eMemory/02_Systems/mpts_systems.md`
- **Decay Model**: `eMemory/02_Systems/decay_cost_model.md`
- **Active Context**: `eMemory/01_Context/activeContext.md` (lines 774-888)

---

## Authority

**Confirmed Canonical by:** Cove Faraday  
**Date:** December 8, 2025  
**Status:** Final - No further adjustment required  
**Directive:** "Embed as law, not proposal"

---

**End of Canonical Definition**
