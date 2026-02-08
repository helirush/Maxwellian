# Customer Hierarchy & Naming System

## Overview
The eBehavior system uses a 3-level hierarchical naming structure for organizing transformer analysis dashboards and reports. This system allows proper aggregation and identification from individual transformers up to company-wide SITE level analysis.

**Author:** MD Howell / Cove  
**Date:** January 10, 2025  
**Status:** Implemented and Active

---

## Three-Level Hierarchy

### Level 1: SITE (Company Level)
- **Purpose:** Aggregates ALL transformers across ALL locations for a company
- **Identifier:** Company name + SET count (e.g., `FosterFarms-1`)
- **Count Indicator:** `-{num_sets}` shows how many SETs are in the SITE
- **Use Case:** Company-wide energy analysis, multi-location portfolio management
- **Trigger:** More than 4 transformers analyzed
- **Example Filename:** `SITE-Summaryboard_FosterFarms-1_1minRES_251001-251031_31d.html`

### Level 2: SET (SubCompany/Plant Level)
- **Purpose:** Aggregates transformers at a specific plant/facility location
- **Identifier:** Plant name + FIELD count + Location (e.g., `CherryAve-4_Fresno_CA_93706`)
- **Count Indicator:** `-{num_fields}` shows how many FIELDs (transformers) are in the SET
- **Use Case:** Single-location analysis with multiple transformers
- **Trigger:** 2-4 transformers at same location
- **Example Filename:** `SET1-Summaryboard_CherryAve-4_Fresno_CA_93706_1minRES_251001-251031_31d.html`

### Level 3: FIELD (Individual Transformer)
- **Purpose:** Individual transformer analysis
- **Identifier:** Transformer name (e.g., `T10.AirChiller`)
- **Use Case:** Single transformer detailed analysis
- **Trigger:** 1 transformer
- **Example Filename:** `FIELD-Summaryboard_T10.AirChiller_251001-251031.html`

---

## Input Format

### Customer Facility String
The system parses the `customer_facility` input in the following formats:

**Format 1 (Preferred):** `"Company Name: Facility Name"`
```
Foster Farms: Cherry Ave Facility
```

**Format 2 (Alternative):** `"Company Name, Facility Name, City, State ZIP"`
```
Foster Farms, Cherry Ave Facility, Fresno, CA 93706
```

### Site Location String
Separate `site_location` field in format: `"City, State ZIP"`  
Input format:
```
Fresno, CA 93706
```
Parsed format (underscores replace commas/spaces):
```
Fresno_CA_93706
```

---

## Parsing Logic

### Implementation
File: `/Users/mdhowell/eestream/eBehavior/utils/customer_hierarchy.py`

### Key Functions

#### `parse_customer_hierarchy(customer_facility, site_location)`
Parses input strings into hierarchical components.

**Returns:**
```python
{
    'company_name': 'FosterFarms',           # Clean name (no spaces)
    'company_display': 'Foster Farms',       # Display version
    'subcompany_name': 'CherryAveFacility',  # Clean facility name
    'subcompany_display': 'Cherry Ave Facility',  # Display version
    'plant_name': 'CherryAve',              # Short plant identifier
    'set_identifier': 'CherryAve_Fresno_CA_93706',  # SET level name (underscores)
    'site_identifier': 'FosterFarms'        # SITE level name
}
```

#### `get_dashboard_prefix(num_transformers, hierarchy)`
Returns appropriate prefix based on transformer count:
- `"FIELD-"` for 1 transformer
- `"SET1-"` for 2-4 transformers
- `"SITE-"` for >4 transformers

#### `get_dashboard_name(num_transformers, hierarchy, dashboard_type)`
Generates complete dashboard name with proper hierarchy level.

---

## Dashboard Types

All four dashboard types follow this hierarchy:

### 1. Energy Dashboard
- **FIELD:** `FIELD-Energyboard_T10.AirChiller_date.html`
- **SET:** `SET1-Energyboard_CherryAve-4_Fresno_CA_93706_1minRES_date_31d.html`
- **SITE:** `SITE-Energyboard_FosterFarms-1_1minRES_date_31d.html`

### 2. Heat Dashboard
- **FIELD:** `FIELD-Heatboard_T10.AirChiller_date.html`
- **SET:** `SET1-Heatboard_CherryAve-4_Fresno_CA_93706_1minRES_date_31d.html`
- **SITE:** `SITE-Heatboard_FosterFarms-1_1minRES_date_31d.html`

### 3. Voltage Dashboard
- **FIELD:** `FIELD-Voltboard_T10.AirChiller_date.html`
- **SET:** `SET1-Voltboard_CherryAve-4_Fresno_CA_93706_1minRES_date_31d.html`
- **SITE:** `SITE-Voltboard_FosterFarms-1_1minRES_date_31d.html`

### 4. Summary Dashboard
- **FIELD:** `FIELD-Summaryboard_T10.AirChiller_date.html`
- **SET:** `SET1-Summaryboard_CherryAve-4_Fresno_CA_93706_1minRES_date_31d.html`
- **SITE:** `SITE-Summaryboard_FosterFarms-1_1minRES_date_31d.html`

---

## Integration Points

### File: `working_renderer.py`
**Function:** `generate_site_dashboard()`
- Lines 915-1001: Parses customer hierarchy and generates proper filenames
- Uses `customer_info` dictionary to extract `customer_facility` and `site_location`
- Determines prefix based on number of transformers in `analysis_summaries`

### File: `dashboard_utils.py`
**Function:** `extract_summary_dashboard_values()`
- Lines 168-291: Calculates SET-level aggregated metrics
- Populates individual transformer cards (xfmr1-xfmr4)
- Provides both SET-level and FIELD-level data replacements

### File: `unified_dashboard_generator.py`
**Function:** `_generate_summary_dashboard()`
- Lines 298-357: Generates summary dashboards using site dashboard generator
- Handles both FIELD and SET level generation

### File: `eeBEHAVIOR.py`
**Lines:** 1272: Dashboard types list
```python
dashboard_types = ['energy', 'heat', 'volt', 'summary']
```

---

## Data Structure: customer_info

The `customer_info` dictionary contains:
```python
{
    'customer_facility': 'Foster Farms: Cherry Ave Facility',  # Used for hierarchy parsing
    'customer_name': 'Foster Farms',                           # Alternative field
    'site_location': 'Fresno, CA 93706',                      # Used for SET identifier
    'total_monthly_kwh': 500000,                              # For calculations
    'total_monthly_cost': 60000,                              # For cost metrics
    'electricity_rate': 0.12,                                 # Blended rate
    'utility_data_type': 'accurate',                          # Data quality flag
    # ... other fields
}
```

---

## Calculation Details

### SET-Level Metrics (Multiple Transformers)
When generating SET-level dashboards, the system calculates:

**Summed Values:**
- Total capacity (kVA)
- Total average kW
- Total average kVA
- Total energy waste (kW)
- Total costs ($/hour)

**Weighted Averages:**
- Power factor (weighted by kVA for accuracy)
- Energy waste percentage

**Individual Cards:**
- Each transformer (xfmr1-xfmr4) retains its individual metrics
- Allows comparison between transformers in the SET

### Example Calculation
For 2 transformers (T10 and T12):
```
T10: 2500 kVA, 1200 kW, 1500 kVA, 80% PF
T12: 3000 kVA, 1800 kW, 2100 kVA, 86% PF

SET-level:
- Total Capacity: 5,500 kVA
- Total kW: 3,000 kW
- Total kVA: 3,600 kVA
- Weighted PF: 83.5% (weighted by kVA)
- Energy Waste: 16.5%
```

---

## Examples

### Example 1: Foster Farms Cherry Ave Plant (4 Transformers)
**Input:**
- Customer Facility: `"Foster Farms: Cherry Ave Facility"`
- Site Location: `"Fresno, CA 93706"`
- Transformers: T10, T12, T15, T16

**Output:**
- **Dashboard Level:** SET1 (2-4 transformers)
- **Count Indicator:** `-4` (4 FIELDs in this SET)
- **Summary Dashboard:** `SET1-Summaryboard_CherryAve-4_Fresno_CA_93706_1minRES_251001-251031_31d.html`
- **Directory:** `.../FosterFarms/CherryAve_Site/`
- **Hierarchy:**
  - SITE: FosterFarms (company-wide, if >4 total transformers)
  - SET: CherryAve-4_Fresno_CA_93706 (this plant with 4 transformers)
  - FIELD: T10, T12, T15, T16 (individual transformers)

### Example 2: Single Transformer Analysis
**Input:**
- Customer Facility: `"Foster Farms: Cherry Ave Facility"`
- Transformer: T10.AirChiller

**Output:**
- **Dashboard Level:** FIELD (1 transformer)
- **Summary Dashboard:** `FIELD-Summaryboard_T10.AirChiller_251001-251031.html`
- **Directory:** `.../FosterFarms/T10.AirChiller.Oct2025.31d_AN53111387/`

### Example 3: Multi-Location Company (8 Transformers)
**Input:**
- Customer Facility: `"Foster Farms: Cherry Ave Facility"`
- Site Location: `"Fresno, CA 93706"`
- Total Transformers: 8 (across multiple locations/SETs)

**Output:**
- **Dashboard Level:** SITE (>4 transformers)
- **Count Indicator:** `-1` (1 SET in this SITE - could be more with multiple SETs)
- **Summary Dashboard:** `SITE-Summaryboard_FosterFarms-1_1minRES_251001-251031_31d.html`
- **Aggregation:** Company-wide metrics across all locations

---

## Benefits

1. **Clear Hierarchy:** Three distinct levels (SITE/SET/FIELD) prevent confusion
2. **Scalability:** System works for 1 transformer or hundreds
3. **Location Context:** SET level includes location for multi-facility companies
4. **Consistent Naming:** All dashboard types follow same hierarchy
5. **Easy Aggregation:** Clear path from individual → plant → company
6. **Future-Proof:** Can add additional hierarchy levels if needed

---

## Testing

Test file: `utils/customer_hierarchy.py` (run as script)
```bash
cd /Users/mdhowell/eestream/eBehavior
python utils/customer_hierarchy.py
```

Validates:
- Parsing of different input formats
- Correct hierarchy extraction
- Proper prefix determination
- Filename generation for all levels

---

## Future Enhancements

Possible extensions:
1. **REGION Level:** Group multiple SITE locations by region (e.g., "West Coast")
2. **DIVISION Level:** Corporate divisions with multiple facilities
3. **Multi-SET Support:** SET2, SET3 for multiple transformer groups at same facility
4. **Historical Tracking:** Compare dashboards across time periods

---

## Related Documentation

- **Summaryboard Implementation:** `eMemory/summaryboardImplementation.md`
- **Dashboard System:** `dashboard/README_UNIFIED_DASHBOARDS.md`
- **Directory Structure:** `directory_structure.py`

---

## Contact

For questions or issues with the customer hierarchy system:
- Author: MD Howell
- Email: mike@unityenergy.com
- System: eBehavior / eStream Analysis Platform
