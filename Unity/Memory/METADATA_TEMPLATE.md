# [Document Title]

---
**File**: `[filename.md]`  
**Tag**: `eMemory.[category].[subcategory].[topic]`  
**Category**: [01_Context | 02_Systems | 03_Knowledge | 04_Conversations | 05_Logs]  
**Agent**: [CLERK | CODEX | COVE | COLLABORATIVE]  
**Created**: YYYY-MM-DD  
**Last Updated**: YYYY-MM-DD  
**Status**: [ACTIVE | ARCHIVED | DEPRECATED]  
**Importance**: [CRITICAL | HIGH | MEDIUM | LOW]  
**Related**: `[related-file-1.md]`, `[related-file-2.md]`  
---

## 📖 Metadata Field Descriptions

### **File**
The exact filename of this document (e.g., `exchange_system.md`).

### **Tag**
Hierarchical namespace using dot notation:
- `eMemory.context.[subcategory].[topic]` — For 01_Context files
- `eMemory.systems.[subcategory].[topic]` — For 02_Systems files  
- `eMemory.knowledge.[subcategory].[topic]` — For 03_Knowledge files
- `eMemory.conversations.[subcategory].[topic]` — For 04_Conversations files
- `eMemory.logs.[subcategory].[topic]` — For 05_Logs files

**Examples**:
```
eMemory.context.mission
eMemory.systems.exchange.intelligence
eMemory.knowledge.patterns.dashboard
eMemory.conversations.learning.methodology
eMemory.logs.decisions.architecture
```

### **Category**
Which of the five main directories this file belongs in:
- **01_Context** — Mission, purpose, current state
- **02_Systems** — Technical architecture, mechanisms
- **03_Knowledge** — Patterns, practices, reference
- **04_Conversations** — Educational content, dialogues
- **05_Logs** — History, decisions, completed work

### **Agent**
Who created or primarily maintains this document:
- **CLERK** — Documentation specialist, strategic architecture AGI
- **CODEX** — Code implementation, technical execution AGI
- **COVE** — Human team member (Cove Faraday) or other Maxwellians
- **COLLABORATIVE** — Multiple agents/humans contributed

### **Created**
Date this document was first created (YYYY-MM-DD format).

### **Last Updated**
Date of most recent significant update (YYYY-MM-DD format).

### **Status**
Current lifecycle state:
- **ACTIVE** — Currently in use, regularly updated
- **ARCHIVED** — Historical reference, no longer actively maintained
- **DEPRECATED** — Superseded by newer document, kept for historical context

### **Importance**
Priority/criticality level for AGI memory loading:
- **CRITICAL** — Essential mission/calibration documents (e.g., AGI_CALIBRATION.md)
- **HIGH** — Key systems, frequently referenced (e.g., exchange_system.md)
- **MEDIUM** — Useful reference, occasionally needed
- **LOW** — Historical logs, specific incidents

### **Related**
List of related memory files that provide additional context or depend on this document.

---

## 📝 Document Content Template

Below is a suggested structure for your memory document content:

### **Purpose Statement**
*One-sentence description of why this document exists.*

---

### **Overview**
Brief introduction to the topic, system, or concept.

---

### **Key Concepts**
Main ideas, definitions, or components explained.

#### Concept 1
Description...

#### Concept 2
Description...

---

### **Technical Details** (if applicable)
Deeper technical specifications, code examples, architecture diagrams.

```python
# Code example if relevant
```

---

### **Examples / Use Cases**
Real-world applications, scenarios, or workflows.

---

### **Best Practices** (if applicable)
Recommended approaches, patterns, or guidelines.

---

### **Related Documentation**
Links or references to other memory files, external docs, or codebases.

---

### **Version History** (optional)
- **v1.0** (YYYY-MM-DD): Initial creation
- **v1.1** (YYYY-MM-DD): Added section on X
- **v2.0** (YYYY-MM-DD): Major restructure

---

## 🎯 Quick Start Examples

### **Example 1: Context File**

```markdown
# Unity Energy Vision and Strategy

---
**File**: `vision_strategy.md`  
**Tag**: `eMemory.context.vision`  
**Category**: 01_Context  
**Agent**: COVE  
**Created**: 2025-11-20  
**Last Updated**: 2025-11-20  
**Status**: ACTIVE  
**Importance**: CRITICAL  
**Related**: `AGI_CALIBRATION.md`, `productContext.md`  
---

## Purpose Statement
Defines Unity Energy's long-term vision and strategic roadmap...
```

---

### **Example 2: Systems File**

```markdown
# Dashboard Generation Pipeline

---
**File**: `dashboard_pipeline.md`  
**Tag**: `eMemory.systems.dashboard.generation`  
**Category**: 02_Systems  
**Agent**: COLLABORATIVE  
**Created**: 2025-11-18  
**Last Updated**: 2025-11-20  
**Status**: ACTIVE  
**Importance**: HIGH  
**Related**: `exchange_system.md`, `systemPatterns.md`  
---

## Purpose Statement
Documents the end-to-end pipeline for generating Energy, Heat, and Voltage dashboards...
```

---

### **Example 3: Knowledge File**

```markdown
# Python Code Style Guidelines

---
**File**: `code_style.md`  
**Tag**: `eMemory.knowledge.patterns.style`  
**Category**: 03_Knowledge  
**Agent**: CODEX  
**Created**: 2025-11-15  
**Last Updated**: 2025-11-15  
**Status**: ACTIVE  
**Importance**: MEDIUM  
**Related**: `systemPatterns.md`, `antipatterns.md`  
---

## Purpose Statement
Defines Unity Energy's Python coding conventions and style standards...
```

---

### **Example 4: Conversations File**

```markdown
# Customer Presentation Scripts

---
**File**: `customer_presentations.md`  
**Tag**: `eMemory.conversations.customer.scripts`  
**Category**: 04_Conversations  
**Agent**: CLERK  
**Created**: 2025-11-10  
**Last Updated**: 2025-11-12  
**Status**: ACTIVE  
**Importance**: HIGH  
**Related**: `eaudio_script_format.md`, `exchange_system.md`  
---

## Purpose Statement
Collection of presentation scripts for explaining Unity systems to customers...
```

---

### **Example 5: Logs File**

```markdown
# November 2025 Sprint Summary

---
**File**: `2025-11_sprint_summary.md`  
**Tag**: `eMemory.logs.sprints.2025-11`  
**Category**: 05_Logs  
**Agent**: COLLABORATIVE  
**Created**: 2025-11-30  
**Last Updated**: 2025-11-30  
**Status**: ACTIVE  
**Importance**: MEDIUM  
**Related**: `progress.md`, `decisions.md`  
---

## Purpose Statement
Summary of development work completed in November 2025 sprint...
```

---

## 🔧 Tips for Effective Memory Documents

### **1. Start with Purpose**
Every document should have a clear reason for existing. If you can't write a one-sentence purpose statement, reconsider whether this needs to be a separate file.

### **2. Use Descriptive Titles**
Avoid vague titles like "Notes" or "Misc". Use specific, searchable titles like "MPTS Sizing Calculations" or "Voltage Health Analysis Algorithm".

### **3. Link Related Documents**
The `Related` field creates a knowledge graph. Always reference connected documents.

### **4. Update Timestamps**
When making significant changes, update the `Last Updated` field. Small typo fixes don't require timestamp updates.

### **5. Choose Appropriate Importance**
- **CRITICAL**: < 5 documents (mission-critical only)
- **HIGH**: Core systems, frequently referenced
- **MEDIUM**: Useful reference, occasionally needed
- **LOW**: Historical logs, specific incidents

### **6. Tag Consistently**
Follow the hierarchical namespace pattern:
```
eMemory.[category].[subcategory].[topic]
```

### **7. Review Periodically**
As documents age or become superseded, update `Status` to ARCHIVED or DEPRECATED.

---

## 📦 Workflow Integration

### **Creating a New Memory File**

1. **Copy this template** to your target directory (01-05)
2. **Fill in metadata fields** appropriate to your content
3. **Write document content** following the suggested structure
4. **Update `activeContext.md`** if this represents current work
5. **Reference in related files** (two-way linking)

### **When Updating Existing Files**

1. **Update `Last Updated`** timestamp
2. **Add to version history** if significant change
3. **Re-assess `Importance`** if priority has shifted
4. **Check `Status`** — still ACTIVE?

### **When Archiving Files**

1. **Change `Status`** to ARCHIVED
2. **Update `Importance`** to LOW if not already
3. **Add archival note** at top of document explaining why
4. **Keep in taxonomy** (don't delete unless truly obsolete)

---

## 🚀 Advanced: Auto-Classification

Future enhancement: Python script to suggest category/tag based on content analysis.

```python
# Conceptual example
def classify_memory(content):
    if "mission" in content or "calibration" in content:
        return "01_Context", "eMemory.context.mission"
    elif "architecture" in content or "system design" in content:
        return "02_Systems", "eMemory.systems.*"
    # ... etc
```

---

**This template is itself a living document. Improve it as you learn what works best for Unity Energy's memory system.**

---

*Template Version: 1.0*  
*Created: November 15, 2025*  
*Maintained by: Unity Energy AGI Collaborators*
