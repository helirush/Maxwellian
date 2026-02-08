# Voltage Health Algorithm - Quick Reference

## 🎛️ Key Tuning Parameters

### **Primary Clustering Control**
```python
# File: eBehavior/core/voltage_health.py, line ~161
if voltage_diff <= 2.0:  # ← MAIN TUNING PARAMETER
```

| Value | Effect | Use Case |
|-------|--------|----------|
| 1.0V | More sensitive, more groups | Detailed motor signature analysis |
| 2.0V | **DEFAULT** - Balanced sensitivity | General purpose voltage health |
| 3.0V | Less sensitive, fewer groups | High-noise environments |
| 5.0V | Very broad grouping | Initial screening/overview |

### **Severity Thresholds**
```python
# File: eBehavior/core/voltage_health.py, line ~197-208
def _get_severity_label(self, voltage_drop):
    if voltage_drop > 80:    return "EXTREME"     # ~400V
    elif voltage_drop > 60:  return "CRITICAL"    # ~420V  
    elif voltage_drop > 40:  return "SEVERE"      # ~440V
    elif voltage_drop > 20:  return "SIGNIFICANT" # ~460V
    elif voltage_drop > 10:  return "MODERATE"    # ~470V
    else:                    return "MINOR"       # >470V
```

### **Motor Health Alert Thresholds**
```python
# File: eBehavior/core/voltage_health.py, line ~396-403
def _assess_device_health(self, frequency_count):
    if frequency_count >= 10:   # HIGH ALERT
    elif frequency_count >= 4:  # CRITICAL CONCERN  
    elif frequency_count >= 2:  # MODERATE CONCERN
    else:                       # WATCH
```

---

## 🔧 Quick Modifications

### **Make More Sensitive (Detect More Groups):**
```python
# Change line ~161 from:
if voltage_diff <= 2.0:
# To:
if voltage_diff <= 1.0:
```

### **Make Less Sensitive (Fewer, Larger Groups):**
```python
# Change line ~161 from: 
if voltage_diff <= 2.0:
# To:
if voltage_diff <= 3.5:
```

### **Adjust Motor Alert Sensitivity:**
```python
# For more sensitive motor alerts, change line ~396:
if frequency_count >= 5:    # Instead of >= 10
elif frequency_count >= 2:  # Instead of >= 4
```

---

## 📊 Expected Group Counts by Scenario

| Voltage Drop Count | Expected Groups | Clustering Tolerance |
|-------------------|-----------------|---------------------|
| 10-50 | 2-4 groups | 2.0V (default) |
| 100-500 | 3-6 groups | 2.0V (default) |
| 1000+ | 4-8 groups | 2.0V (default) |
| 3000+ | 5-10 groups | 2.0V (default) |

---

## ⚠️ Troubleshooting

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| Too many small groups | Tolerance too low | Increase from 2.0V to 3.0V |
| Groups missed | Tolerance too high | Decrease from 2.0V to 1.5V |
| No groups detected | No voltage drops < 480V | Check data or nominal voltage setting |
| False motor alerts | Thresholds too low | Increase frequency thresholds |

---

## 🧪 Test Command
```bash
cd /Users/mdhowell/eestream
python test_voltage_grouping.py
```

**Expected Output:** ✅ Both simple and complex tests should PASS

---

**Last Updated:** August 20, 2025  
**Algorithm Version:** Dynamic Clustering v1.0
