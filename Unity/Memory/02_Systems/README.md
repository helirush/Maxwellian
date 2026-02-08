# 02_Systems - System Documentation Index
**Last Updated**: 2025-11-26  
**Purpose**: Complete reference documentation for all eestream systems and models

---

## System Documentation Files

### 🎯 Core Analysis System
**eBEHAVIOR_SESSION_REVIEW.md** (NEW - 11 KB)
- Complete reference for the eBEHAVIOR.py integrated analysis tool
- Three-stage pipeline architecture (ePrep → eWeather → eXamine)
- 8 core modules with dependencies and capabilities
- 5+ dashboard renderer options
- 40+ main functions documented
- Recent fixes and known issues
- Typical workflow and quick references
- **Last Updated**: 2025-11-26 22:30 UTC
- **Status**: ✅ Production-ready
- **Use When**: Setting up eBehavior analysis or understanding the analysis pipeline

### 💡 Financial & Cost Modeling
**decay_cost_model.md** (18 KB)
- Decay cost financial modeling system
- Cost calculations and projections
- Long-term financial impact analysis
- Energy cost decay patterns
- **Use When**: Analyzing financial impacts or modeling long-term costs

### 🔄 System Integration & Exchange
**exchange_system.md** (11 KB)
- System exchange and data transfer mechanisms
- Integration points between modules
- Data flow and exchange protocols
- **Use When**: Understanding inter-module communication

### 📊 MPTS & Dashboard Implementation
**MPTS_MINI_DASHBOARD_IMPLEMENTATION.md** (5.8 KB)
- MPTS Mini Dashboard implementation details
- Dashboard configuration and setup
- Display parameters and options
- **Use When**: Setting up or customizing MPTS dashboards

**mpts_systems.md** (9.4 KB)
- Unity MPTS (Multi-Phase Transformer System) documentation
- MPTS architecture and capabilities
- System integration notes
- **Use When**: Understanding MPTS calculations and behavior

### 🔌 API & Server Systems
**csv_server_api.md** (10.7 KB)
- CSV server API documentation
- Data access and retrieval interfaces
- API endpoints and usage
- **Use When**: Integrating with CSV server or building API consumers

---

## Quick Navigation

### By Purpose

**If you want to...**

**Understand the analysis pipeline:**
→ eBEHAVIOR_SESSION_REVIEW.md

**Model financial impacts:**
→ decay_cost_model.md

**Understand system integration:**
→ exchange_system.md

**Work with dashboards:**
→ MPTS_MINI_DASHBOARD_IMPLEMENTATION.md

**Understand MPTS calculations:**
→ mpts_systems.md

**Access CSV data via API:**
→ csv_server_api.md

---

## Document Relationships

```
eBEHAVIOR_SESSION_REVIEW (main analysis)
├── References: MPTS_MINI_DASHBOARD_IMPLEMENTATION
├── References: mpts_systems
├── Integrates: decay_cost_model
└── Uses: csv_server_api

exchange_system (data flow)
├── Connects: All modules
└── Enables: Data movement between systems

Financial Analysis Path:
├── eBEHAVIOR_SESSION_REVIEW (data analysis)
├── → decay_cost_model (cost calculation)
└── → exchange_system (result distribution)
```

---

## File Inventory

| File | Size | Purpose | Last Updated |
|------|------|---------|--------------|
| eBEHAVIOR_SESSION_REVIEW.md | 11K | Core analysis system | 2025-11-26 |
| decay_cost_model.md | 18K | Financial modeling | 2025-11-15 |
| exchange_system.md | 11K | System integration | 2025-11-15 |
| MPTS_MINI_DASHBOARD_IMPLEMENTATION.md | 5.8K | Dashboard setup | 2025-11-15 |
| mpts_systems.md | 9.4K | MPTS documentation | 2025-11-15 |
| csv_server_api.md | 10.7K | API documentation | 2025-11-20 |

**Total**: 6 documentation files covering complete system architecture

---

## Recent Additions (2025-11-26)

✅ **eBEHAVIOR_SESSION_REVIEW.md** added to eMemory
- Comprehensive reference for the main analysis engine
- Part of ongoing documentation consolidation
- Covers three-stage pipeline, all modules, recent fixes
- Ready for team reference and discussion

---

## How to Use This Directory

1. **Start with eBEHAVIOR_SESSION_REVIEW.md** for core system overview
2. **Reference specific files** based on what you're working on
3. **Cross-reference documents** using the relationship diagram above
4. **Check Last Updated dates** to understand currency of information

---

## System Components Documented

- ✅ Analysis Pipeline (eBEHAVIOR.py)
- ✅ Dashboard Systems (MPTS)
- ✅ Financial Modeling (Decay Costs)
- ✅ Data Integration (Exchange System)
- ✅ API Access (CSV Server)
- ✅ System Architecture (Relationships)

---

## For More Information

- **Active Context**: Check `/01_Context/activeContext.md` for current system state
- **Technical Patterns**: See `/03_Knowledge/systemPatterns.md` for recurring patterns
- **Progress Tracking**: Review `/05_Logs/progress.md` for recent changes
- **Quick Reference**: Check `/03_Knowledge/quickref.md` for common tasks

---

**Purpose**: Serve as the central reference for understanding all eestream systems  
**Status**: ✅ Comprehensive and current  
**Last Reviewed**: 2025-11-26 22:40 UTC
