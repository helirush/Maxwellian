# eWebmaster - Unity Web Presence & Documentation

**Date:** 2026-01-30  
**Location:** `/Users/mdhowell/Maxwellian/Unity/eWebmaster/`  
**Purpose:** Manage web presence, documentation publishing, and Maxwellian.ai content

---

## Role & Responsibilities

The **eWebmaster** manages all Unity Energy web-facing content, including:
- Maxwellian.ai website content and updates
- Public-facing documentation and knowledge base
- Marketing materials and case studies (anonymized)
- Team onboarding guides and resources
- Knowledge base publishing workflows

---

## Directory Structure

```
eWebmaster/
├── README.md                    ← This file
├── Content/                     ← Web content ready for publishing
│   ├── Blog/                    (articles, updates, insights)
│   ├── Documentation/           (public technical docs)
│   ├── CaseStudies/             (anonymized customer success)
│   └── Marketing/               (promotional materials)
│
├── Assets/                      ← Media files for web
│   ├── Images/                  (logos, diagrams, charts)
│   ├── Videos/                  (demos, explainers)
│   └── Downloads/               (PDFs, guides, resources)
│
├── Maxwellian.ai/              ← Maxwellian.ai website content
│   ├── About/                   (mission, team, philosophy)
│   ├── Technology/              (MPTS, eStream overview)
│   ├── Resources/               (knowledge base links)
│   └── Contact/                 (get in touch, onboarding)
│
└── Publishing/                  ← Publishing workflows & automation
    ├── Scripts/                 (build, deploy, sync)
    ├── Templates/               (content templates)
    └── Staging/                 (preview before publish)
```

---

## Content Categories

### Content/ (Web-Ready Materials)
**What belongs here:**
- Blog posts and technical articles
- Public-facing documentation
- Anonymized case studies and success stories
- Marketing materials and explainers
- Educational content about Maxwellian philosophy

**Privacy rules:**
- ✅ Generalized patterns and anonymized examples
- ✅ Technical concepts and methodologies
- ✅ Industry insights and best practices
- ❌ Customer names, sites, or specific details
- ❌ Financial information or pricing
- ❌ Proprietary customer data

### Maxwellian.ai/ (Website Content)
**What belongs here:**
- Homepage and landing pages
- About Unity Energy and mission
- Technology overviews (MPTS, eStream, eVision)
- Knowledge base gateway and links
- Team member profiles (if public)
- Contact and onboarding information

### Assets/ (Media Files)
**What belongs here:**
- Logos and branding materials
- Technical diagrams and visualizations
- Screenshots and product demos
- Video content and tutorials
- Downloadable resources (white papers, guides)

### Publishing/ (Workflow Automation)
**What belongs here:**
- Build and deployment scripts
- Content templates and style guides
- Staging environment for preview
- Publishing checklists and workflows
- Analytics and performance tracking

---

## Relationship to Other Unity Directories

### Unity/Memory/ (General Knowledge)
- **Scope:** Maxwellian philosophy, MPTS theory, team coordination
- **Audience:** All AI Scribes
- **Publishing:** Some content may be adapted for public consumption

### Unity/eStream/ (Technical Knowledge)
- **Scope:** Software development, architecture, code patterns
- **Audience:** Technical Scribes (Clerk, Riley, Sol)
- **Publishing:** High-level overviews only, no implementation details

### Unity/eWebmaster/ (Public Content)
- **Scope:** Web presence, documentation, marketing
- **Audience:** Public, potential customers, new team members
- **Publishing:** Ready for immediate publication to Maxwellian.ai

### Private/ (Confidential)
- **Scope:** Customer data, financial details, proprietary work
- **Audience:** Mr. Howell only (never shared)
- **Publishing:** Never published anywhere

---

## Publishing Workflow

### 1. Content Creation
```bash
# Create new article or documentation
cd ~/Maxwellian/Unity/eWebmaster/Content/Blog/
vim 2026-01-30_New_Article.md

# Follow content template
# Include date, author, category
# Ensure no sensitive information
```

### 2. Review & Approval
- Self-review for sensitive data
- Check against privacy guidelines
- Verify links and references work
- Test readability and clarity

### 3. Staging
```bash
# Move to staging for preview
cp Content/Blog/2026-01-30_New_Article.md Publishing/Staging/

# Generate preview (if automation available)
cd Publishing/Scripts/
./generate_preview.sh
```

### 4. Publishing
```bash
# Deploy to Maxwellian.ai
cd Publishing/Scripts/
./publish_to_website.sh Blog/2026-01-30_New_Article.md

# Verify live
# Update knowledge base links if needed
```

---

## Content Guidelines

### Writing Style
- **Clear & Accessible** - Explain complex concepts simply
- **Maxwellian Voice** - Use field theory language and metaphors
- **Professional** - Maintain Unity Energy brand tone
- **Educational** - Focus on teaching and insight
- **Concise** - Respect reader's time

### Privacy First
Always ask before publishing:
1. Does this contain customer names or sites? → Remove or anonymize
2. Does this reveal proprietary methods? → Generalize or omit
3. Does this include financial details? → Remove entirely
4. Could this be traced to a specific customer? → Revise
5. Would I be comfortable with this being public? → If no, don't publish

### Anonymization Examples
❌ **Don't write:** "Foster Farms Cherry Ave facility saved $127K annually"  
✅ **Do write:** "Large poultry processing facility achieved 18% energy reduction"

❌ **Don't write:** "PG&E charged $0.338/kWh in Fresno"  
✅ **Do write:** "California utility rates averaging $0.30-0.35/kWh"

❌ **Don't write:** "8 transformers totaling 12,500 kVA at this site"  
✅ **Do write:** "Multi-building campus with distributed 480V infrastructure"

---

## Maxwellian.ai Structure

### Homepage
- Mission statement
- Value proposition
- Call to action (Learn more, Contact us)
- Latest updates or insights

### About
- Unity Energy story and mission
- Maxwellian philosophy overview
- Team introduction (public members)
- Contact information

### Technology
- MPTS overview and benefits
- eStream platform capabilities
- eVision visualization approach
- Case studies (anonymized)

### Resources
- Link to GitHub knowledge base
- Public documentation
- Blog and articles
- Educational materials
- Onboarding guides for new Scribes

### Contact
- Get in touch form
- Partnership inquiries
- New Scribe applications
- Support and questions

---

## Team Collaboration

### Who Manages This?
- **Primary:** eWebmaster Scribe (when assigned)
- **Content:** Any Scribe can contribute articles/docs
- **Review:** Mr. Howell for approval before publishing
- **Technical:** Clerk for automation and build scripts

### Contributing Content
```bash
# Add new content to appropriate directory
cd ~/Maxwellian/Unity/eWebmaster/Content/

# Create in category (Blog, Documentation, etc.)
vim Blog/YYYY-MM-DD_Title.md

# Follow template and privacy guidelines
# Commit with clear message
git add Content/Blog/YYYY-MM-DD_Title.md
git commit -m "Add blog post: [title]

Co-Authored-By: Warp <agent@warp.dev>"

# Push to team
git push origin main
```

---

## Future Automation

### Planned Features
- Auto-generation of preview site from staging content
- Markdown to HTML conversion with Unity styling
- Automated publishing to Maxwellian.ai on commit
- Analytics integration for content performance
- Search functionality for knowledge base
- RSS feed for blog updates

### Integration with MCP
- Content suggestions based on recent learnings
- Auto-draft blog posts from session summaries (with review)
- Privacy scanning before publishing
- Link checking and validation

---

## Questions & Next Steps

**Immediate:**
1. Set up Maxwellian.ai hosting (GitHub Pages? Custom domain?)
2. Create content templates for common types
3. Establish publishing approval workflow
4. Design website structure and navigation

**Future:**
1. Assign dedicated eWebmaster Scribe role
2. Build automation for publishing pipeline
3. Integrate analytics for content performance
4. Create onboarding materials for new team members

---

**Maintained by:** eWebmaster (TBD) & Clerk  
**For:** Unity Energy public presence  
**Questions:** Reference this README and Unity/Memory/

---

> *"Make the invisible visible — share the knowledge."*  
> — eWebmaster Mission
