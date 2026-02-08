# Architectural Decisions - Unity Energy eestream System

---
**File**: `decisions.md`  
**Tag**: `eMemory.logs.decisions.architecture`  
**Category**: 05_Logs  
**Agent**: COLLABORATIVE  
**Created**: 2025-05-01  
**Last Updated**: 2025-10-17  
**Status**: ACTIVE  
**Importance**: HIGH  
**Related**: `systemPatterns.md`, `progress.md`, `antipatterns.md`  
---

## Purpose
This document captures **why** we made key architectural and design decisions, including alternatives considered, trade-offs evaluated, and the rationale behind choices. Understanding past decisions prevents re-litigating solved problems and provides context for future evolution.

---

## Decision Log

### D001: Unified Dashboard Generator API (September 2025)

**Decision**: Implement single `unified_dashboard_generator.py` that creates all dashboard types (Energy, Heat, Voltage, Site) rather than separate generator modules.

**Alternatives Considered**:
1. **Separate Generators** - Individual modules per dashboard type
2. **Class Hierarchy** - Base dashboard class with specialized subclasses
3. **Unified API** - Single generator with template switching (CHOSEN)

**Trade-offs**:
- ✅ **Pro**: Eliminates code duplication across generators
- ✅ **Pro**: Consistent parameter replacement logic
- ✅ **Pro**: Single point of maintenance for dashboard generation
- ✅ **Pro**: Easier to add new dashboard types
- ❌ **Con**: Single module becomes larger and more complex
- ❌ **Con**: Template-specific logic requires conditional handling

**Rationale**: The commonality between dashboard types (parameter replacement, file naming, validation) far outweighed the differences. Code duplication was causing maintenance issues where bug fixes in one generator weren't applied to others.

**Outcome**: Successful. Enabled rapid dashboard development and consistent behavior across all types.

---

### D002: Transformer-Centric Directory Organization (August 2025)

**Decision**: Organize reports and dashboards by `Facility → Site → Transformer` hierarchy rather than by analysis type or date.

**Alternatives Considered**:
1. **Date-First Organization** - `STUDY.{date}/{dashboard-type}/{transformer}/`
2. **Analysis-Type First** - `{dashboard-type}/STUDY.{date}/{transformer}/`
3. **Transformer-Centric** - `STUDY.{date}/TRANSFORMER_{name}/` (CHOSEN)

**Trade-offs**:
- ✅ **Pro**: Matches industrial organizational workflow
- ✅ **Pro**: All transformer data in one location
- ✅ **Pro**: Simplifies navigation for facility managers
- ✅ **Pro**: Natural fit for multi-level study system (Individual → Set → Domain)
- ❌ **Con**: Cross-transformer comparisons require navigating multiple directories
- ❌ **Con**: Date-based searches less intuitive

**Rationale**: Industrial users think in terms of equipment (transformers) first, not analysis types. When investigating T10.AirChiller issues, users want all T10 data in one place—energy, heat, voltage dashboards together.

**Outcome**: Highly successful. User feedback confirms this matches their mental model and workflow.

---

### D003: Configuration Centralization (June 2025)

**Decision**: Centralize all API keys and configuration in `eConfig/` module with `.env` file, rather than per-module configuration.

**Alternatives Considered**:
1. **Per-Module Config** - Each module (eBehavior, eVision, eAudio) has own config
2. **Central Config File** - Single JSON or YAML config
3. **Environment Variables + Loader** - `.env` file with `config_loader.py` (CHOSEN)

**Trade-offs**:
- ✅ **Pro**: Single source of truth for all configuration
- ✅ **Pro**: Simplified security (one file to protect)
- ✅ **Pro**: Easy deployment with `.env.example` template
- ✅ **Pro**: Standard Python pattern (python-dotenv)
- ❌ **Con**: All modules depend on eConfig
- ❌ **Con**: Monolithic configuration file can grow large

**Rationale**: Configuration drift across modules was causing bugs (API key in one module but not another). Centralization prevents this and simplifies deployment.

**Outcome**: Eliminated configuration-related bugs. Deployment simplified significantly.

---

### D004: JavaScript-Based Dashboard Data Integration (July 2025)

**Decision**: Use JavaScript `CleanRebuildConnector` pattern with client-side parameter replacement rather than server-side template rendering.

**Alternatives Considered**:
1. **Server-Side Rendering** - Python generates complete HTML with all data
2. **Hybrid Approach** - Server generates initial HTML, JavaScript updates
3. **Client-Side Integration** - JavaScript fetches and integrates all data (CHOSEN)

**Trade-offs**:
- ✅ **Pro**: Real-time dashboard updates possible
- ✅ **Pro**: Interactive functionality (zoom, pan, filter)
- ✅ **Pro**: Reduced server load
- ✅ **Pro**: Better user experience with responsive UI
- ❌ **Con**: Requires JavaScript enabled
- ❌ **Con**: More complex template structure
- ❌ **Con**: Debugging requires browser dev tools

**Rationale**: Industrial dashboards benefit from interactivity. Users need to zoom into voltage events, filter date ranges, and toggle overlays. Pure static HTML couldn't provide this experience.

**Outcome**: Users love the interactive gauges and real-time updates. Complexity trade-off worth it.

---

### D005: {{PARAMETER}} Syntax for Template Replacement (May 2025)

**Decision**: Use `{{PARAMETER}}` double-curly-brace syntax for template parameters rather than other templating approaches.

**Alternatives Considered**:
1. **Jinja2 Templates** - Python's standard templating engine
2. **Custom XML Tags** - `<param name="value"/>`
3. **Double-Curly Syntax** - `{{PARAMETER}}` (CHOSEN)
4. **JavaScript Template Literals** - `${parameter}`

**Trade-offs**:
- ✅ **Pro**: Clear, readable, visually distinct
- ✅ **Pro**: No conflicts with HTML/CSS/JavaScript syntax
- ✅ **Pro**: Simple regex-based replacement
- ✅ **Pro**: No additional dependencies
- ❌ **Con**: Not a standard templating engine
- ❌ **Con**: Limited logic capabilities (no loops/conditionals)

**Rationale**: Dashboard templates are primarily data replacement, not logic-heavy. Double-curly syntax is familiar (Mustache, Handlebars), readable, and sufficient for our needs without Jinja2 complexity.

**Outcome**: Works well. Simple to maintain and understand.

---

### D006: Three-Stage Processing Pipeline (eBehavior Design, 2024)

**Decision**: Implement strict three-stage pipeline: ePrep → eWeather → eExamine, each producing intermediate files.

**Alternatives Considered**:
1. **Single-Pass Processing** - One script does everything
2. **Two-Stage Pipeline** - Prep+Weather combined, then Analysis
3. **Three-Stage Pipeline** - ePrep → eWeather → eExamine (CHOSEN)

**Trade-offs**:
- ✅ **Pro**: Modular debugging (can inspect intermediate outputs)
- ✅ **Pro**: Reusable stages (skip weather if already merged)
- ✅ **Pro**: Clear separation of concerns
- ✅ **Pro**: Easier to test individual stages
- ❌ **Con**: More intermediate files to manage
- ❌ **Con**: Slightly slower due to I/O between stages

**Rationale**: Industrial energy analysis requires validation at each step. Weather data issues shouldn't corrupt prepared data. Voltage analysis bugs shouldn't require re-running weather integration.

**Outcome**: Modularity has saved countless hours of debugging. Correct decision.

---

### D007: Multi-Level Study System (Level 1/2/3, 2024)

**Decision**: Implement three analysis levels: Individual transformer (Level 1), Set analysis (Level 2), Domain intelligence (Level 3).

**Alternatives Considered**:
1. **Single Analysis Mode** - Only individual transformer reports
2. **Two Levels** - Individual + Facility-wide
3. **Three Levels** - Individual → Set → Domain (CHOSEN)

**Trade-offs**:
- ✅ **Pro**: Flexibility for different analysis needs
- ✅ **Pro**: Supports single-transformer and multi-transformer studies
- ✅ **Pro**: Quarterly/annual domain analysis separate from operational monitoring
- ❌ **Con**: More complex directory structure
- ❌ **Con**: Users must understand level selection

**Rationale**: Different stakeholders need different views. Maintenance teams need Level 1 (individual transformer focus). Facility managers need Level 2 (combined facility view). Executives need Level 3 (strategic quarterly/annual analysis).

**Outcome**: Provides necessary flexibility. Level selection could be more intuitive.

---

### D008: Markdown Reports + HTML Dashboards (Dual Output Format, 2024)

**Decision**: Generate both Markdown technical reports (`.md`) and HTML interactive dashboards (`.html`) for every analysis.

**Alternatives Considered**:
1. **HTML Only** - All output as interactive dashboards
2. **Markdown Only** - All output as text reports
3. **Dual Format** - Both Markdown + HTML (CHOSEN)
4. **PDF Reports** - Rendered PDF documents

**Trade-offs**:
- ✅ **Pro**: Markdown for version control, diffs, and technical documentation
- ✅ **Pro**: HTML for executive presentation and interactivity
- ✅ **Pro**: Different audiences prefer different formats
- ✅ **Pro**: Markdown easily converted to other formats
- ❌ **Con**: Duplicate content maintenance
- ❌ **Con**: Larger output file sets

**Rationale**: Engineers and technical users prefer Markdown (readable in VS Code, git-friendly, searchable). Executives and facility managers prefer interactive HTML dashboards (visual, no technical setup required).

**Outcome**: Both formats actively used by different user groups. Validates dual-output approach.

---

### D009: Single Dataset Optimization (October 2025)

**Decision**: Skip SET/SITE directory generation for single-transformer analysis, generate FIELD-Summaryboard in transformer directory instead.

**Alternatives Considered**:
1. **Always Generate SET/SITE** - Regardless of dataset count
2. **Never Generate Summaryboard for Level 1** - Skip summary dashboard
3. **Conditional Generation** - Check dataset count, adapt behavior (CHOSEN)

**Trade-offs**:
- ✅ **Pro**: Clean output structure for single-transformer analysis
- ✅ **Pro**: No unnecessary directories or redundant files
- ✅ **Pro**: Summaryboard always available (user requirement)
- ✅ **Pro**: Multi-transformer analysis still gets full SET/SITE structure
- ❌ **Con**: Additional conditional logic in generation code
- ❌ **Con**: Two different output patterns to maintain

**Rationale**: User feedback indicated confusion and clutter when analyzing single transformers in Level 2 mode. Creating a SITE directory with SET files was unnecessary—all data should be in transformer directory with FIELD prefix.

**Outcome**: Cleaner user experience. Output matches user expectations for single vs multi-transformer analysis.

---

## Decision-Making Principles

### 1. User Mental Model First
Organize by how users think about the domain (transformers, facilities, equipment) not by how the software is structured (modules, classes, functions).

### 2. Simplicity Over Flexibility (Usually)
Choose the simpler solution unless flexibility is clearly needed. We've avoided over-engineering (e.g., plugin architecture) until proven necessary.

### 3. Validate Early, Validate Often
Multiple validation layers prevent bad data from propagating. Better to fail fast with clear errors than produce incorrect dashboards.

### 4. Optimize for Debugging
Modular pipeline stages and intermediate files make debugging easier. Worth the small performance cost.

### 5. Consistency Across Modules
Dashboard generation, file naming, directory structure should follow consistent patterns. Reduces cognitive load.

---

## Lessons from Reversed Decisions

### Reversed D001: Separate Heat Dashboard Generator
**Original Decision**: Keep `heat_dashboard_generator.py` separate from unified system  
**Reversal Date**: October 2025  
**Reason**: Caused binding inconsistencies, placeholder dashes appeared in dashboards  
**New Decision**: Integrate heat dashboard into unified system via `working_renderer.py`  
**Lesson**: Consistency matters more than modularity when systems share 90% of their logic

---

## Future Decisions to Make

### F001: Export to PDF
**Question**: Should we add PDF export for dashboards?  
**Considerations**:
- User requests for printable reports
- Requires additional dependencies (wkhtmltopdf or headless browser)
- Interactive elements lost in PDF format
- Alternative: "Print to PDF" from browser

**Status**: Pending user prioritization

### F002: Real-Time Data Integration
**Question**: Should we support live data streaming vs batch file analysis?  
**Considerations**:
- Requires database integration or API endpoints
- Significant architecture change from file-based processing
- Use case: continuous monitoring vs periodic analysis
- Performance implications for dashboard updates

**Status**: Awaiting market demand validation

### F003: Cloud Deployment
**Question**: Should eestream be cloud-deployable or remain local-only?  
**Considerations**:
- Data privacy concerns (industrial energy data is sensitive)
- Local processing maintains security
- Cloud enables collaboration and remote access
- Hybrid approach possible (local processing, cloud dashboards)

**Status**: Depends on customer requirements

---

## Contributing to This Document

When making significant architectural decisions:
1. Document the decision here BEFORE implementation
2. Include alternatives considered and trade-offs
3. Explain rationale clearly
4. Update with outcome after implementation
5. Reference decision number (D###) in code comments

**Format**:
```markdown
### D###: Decision Title (Date)

**Decision**: [What we decided]

**Alternatives Considered**: [Options evaluated]

**Trade-offs**: [Pros and cons]

**Rationale**: [Why this choice]

**Outcome**: [Results after implementation]
```

This ensures future collaborators (human or AI) understand not just *what* we built, but *why* we built it that way.
