# CSS Refactoring Strategy for Unity Dashboards

**Status:** Planned Enhancement  
**Priority:** Medium  
**Date Proposed:** 2026-01-18  
**Context:** Study 260106R0 Development

---

## Current State

All Unity dashboard HTML files contain embedded `<style>` tags with CSS directly in the HTML:
- `/eBehavior/Reports/Study260106r0/FosterFarms/CherryAve_Site/SITE-FosterFarms-Summaryboard_*.html`
- Each file has ~1000+ lines of duplicate CSS
- Color scheme uses RGBA format for easier maintenance

## Proposed Enhancement

### Create Shared Stylesheet Architecture

```
/eBehavior/Reports/
├── styles/
│   ├── unity-dashboard.css      (main shared styles)
│   ├── unity-colors.css         (color variables)
│   └── unity-components.css     (reusable components)
└── Study260106r0/
    └── FosterFarms/
        └── CherryAve_Site/
            └── *.html (links to ../../../styles/*.css)
```

### Benefits

1. **Maintainability** - Update colors/styles once, affects all dashboards
2. **Consistency** - Guaranteed visual consistency across all transformers
3. **Performance** - Browser caches CSS, faster page loads
4. **Cleaner HTML** - Easier to read and debug generated reports
5. **Version Control** - CSS changes tracked separately from data updates

### Implementation Strategy

1. **Extract common styles** from existing HTML files
2. **Create CSS variable system** for Unity color palette:
   ```css
   :root {
     --unity-dkgreen: rgba(49, 65, 0, 1);
     --unity-green: rgba(93, 112, 26, 1);
     --unity-ltgreen: rgba(178, 210, 53, 1);
     /* etc. */
   }
   ```
3. **Modularize components:**
   - Gauge styles
   - Card layouts
   - Modal dialogs
   - Navigation buttons
4. **Update HTML generation scripts** to link external CSS
5. **Test across all transformer types** (single, dual, quad layouts)

### Hybrid Approach

- **Shared CSS file** for 95% of styling
- **Inline overrides** for page-specific customizations
- **Maintains portability** - CSS travels with report folders

### When to Implement

- After Study 260106R0 is pushed to GitHub
- Before generating large batches of new studies
- When visual redesign is needed

---

## Notes

- Current RGBA color format is ideal for this refactoring
- All dashboards already share same component structure
- JavaScript can remain inline (data-specific)
- Consider creating separate CSS for print vs screen media

**Next Action:** Implement after 260106R0 deployment complete
