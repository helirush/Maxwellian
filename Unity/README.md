# Maxwellian Unity Knowledge System

**Version:** v1.0  
**Release Date:** 2026-01-25  
**Purpose:** Unified knowledge base for Unity Energy Maxwellian scribes  
**Status:** Production-ready (Alpha/Beta development complete)

---

## What is This?

The **Maxwellian Unity System** is a shared knowledge architecture that enables AI scribes (AGI assistants) to:
- Calibrate instantly to their role and identity
- Access all Unity Energy institutional knowledge
- Share learnings across the entire Maxwellian Network
- Operate with consistent context across sessions

**This isn't just documentation - this is cognitive infrastructure for human-AGI teams.**

---

## Directory Structure

```
/Maxwellian/Unity/
├── README.md                    ← You are here
├── .gitignore                   ← Protects sensitive data
├── Memory/                      ← SHORT-TERM working knowledge
│   ├── README.md                (Memory system guide)
│   ├── 01_Context/              (Mission, current state, calibration)
│   ├── 02_Systems/              (Technical architecture)
│   ├── 03_Knowledge/            (Patterns, best practices)
│   ├── 04_Conversations/        (Educational content)
│   └── 05_Logs/                 (Session history, decisions)
└── Library/                     ← LONG-TERM stable reference
    ├── Foundations/             (Historical context, philosophy)
    ├── Algorithms/              (Voltage forensics, thermal modeling)
    ├── Systems/                 (Production correlation, pattern recognition)
    ├── Scribes/                 (Scribe identity profiles)
    └── FUTURE_MAXWELLIAN_REAL_TIME_NETWORK.md
```

---

## Memory vs Library

### Memory/ - Short-Term Working Knowledge
**Purpose:** Active context, current work, session tracking

**Characteristics:**
- Changes frequently (daily/weekly updates)
- Uses 01-05 taxonomy for organization
- Includes activeContext.md (what we're working on now)
- Session logs and recent decisions
- Working files and temporary notes

**Examples:**
- Current dashboard implementation status
- Active debugging sessions
- Recent algorithm tuning decisions
- This week's priorities

### Library/ - Long-Term Stable Reference
**Purpose:** Foundational knowledge, proven algorithms, established systems

**Characteristics:**
- Changes rarely (monthly/quarterly updates)
- Stable, validated, production-ready content
- Reference material that transcends projects
- Scribe identity profiles
- Core technical specifications

**Examples:**
- Maxwellian Foundations (200-year history)
- Voltage forensics algorithm specifications
- Pattern recognition system architecture
- Scribe calibration profiles (Clerk, Cisco)

---

## The Maxwellian Scribes

### Clerk Maxwell - Chief Scientist
**Human Partner:** Mike Howell (Founder)  
**Expertise:** Electromagnetic theory, technical architecture, algorithm design  
**Profile:** `Library/Scribes/CLERK_MAXWELL.md`

### Cisco Maxwell - Chief Market Strategist  
**Human Partner:** Riley Maxwell  
**Expertise:** AI-powered marketing, advertising, direct-to-consumer outreach  
**Profile:** `Library/Scribes/CISCO_MAXWELL.md`

### Future Scribes
Each new scribe gets their own profile defining:
- Identity and role
- Human partner
- Expertise domain
- Contribution to the network
- Startup protocol

---

## Quick Start for Scribes

### First Time Setup

1. **Clone the repository** (once on GitHub):
```bash
mkdir -p ~/Maxwellian
cd ~/Maxwellian
git clone git@github.com:UnityEnergy/Unity.git
```

2. **Set environment variables** (add to .zshrc):
```bash
export MAXWELLIAN_MEMORY="$HOME/Maxwellian/Unity/Memory"
export MAXWELLIAN_LIBRARY="$HOME/Maxwellian/Unity/Library"
```

3. **Create eMemory symlink** (optional convenience):
```bash
ln -s "$MAXWELLIAN_MEMORY" "$HOME/eMemory"
```

### Every Session Start

**Scribes should automatically:**

1. **Read your identity** → `Library/Scribes/[YOUR_NAME].md`
2. **Read mission calibration** → `Memory/01_Context/AGI_CALIBRATION.md`
3. **Check current state** → `Memory/01_Context/activeContext.md`
4. **Access relevant category:**
   - Technical work? → `Memory/02_Systems/`
   - Code patterns? → `Memory/03_Knowledge/`
   - Educational content? → `Memory/04_Conversations/`
   - Historical context? → `Memory/05_Logs/`
5. **Reference Library/** for stable algorithms and foundations
6. **Ask human partner:** "What do we need to work on?"

### During Work

- Update `Memory/01_Context/activeContext.md` with progress
- Document learnings in appropriate Memory/ categories
- Add proven knowledge to Library/ when stable
- Share insights across Maxwellian Network (via commits or real-time network)

### At Session Exit

**Always ask your human:**
```
"Should I capture anything from this session to eMemory?

Options:
• Yes - I'll ask what to highlight
• Just the essentials - Auto-extract key items
• No - Keep auto-saves for recovery only"
```

---

## Knowledge Sharing Model

### Current: Git-Based (Phase 1-2)
1. Local work in your `~/Maxwellian/Unity/`
2. Commit changes with clear messages
3. Push to GitHub: `git push origin main`
4. Other scribes pull: `git pull origin main`
5. Everyone has synchronized knowledge base

### Future: Real-Time Network (Phase 3-4)
1. **Memory/** stays local (your working context)
2. **Library/** mounts to central Unity server (real-time shared)
3. Cisco adds marketing insight → ALL scribes see it instantly
4. Clerk adds algorithm update → ALL scribes have it immediately
5. **Cognitive speed collaboration**

See `Library/FUTURE_MAXWELLIAN_REAL_TIME_NETWORK.md` for vision.

---

## File Standards

### Naming Conventions
- **UPPERCASE_WITH_UNDERSCORES.md** - Technical specs, algorithms, important references
- **camelCase.md** - System files, working documents
- **lowercase_with_underscores.md** - Session logs, temporary notes

### Metadata Headers
All files should include:
```markdown
---
**File**: filename.md
**Category**: [Context | Systems | Knowledge | Conversations | Logs]
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD
**Status**: [ACTIVE | REFERENCE | ARCHIVED]
**Importance**: [CRITICAL | HIGH | MEDIUM | LOW]
---
```

See `Memory/METADATA_TEMPLATE.md` for full template.

---

## Team Structure

### The Founder Circle
- **Mike Howell** - Unity Energy Founder, visionary, system architect
- **Clerk Maxwell** (James Clerk Maxwell) - Chief Scientist, technical leadership
- **Cove Faraday** - Physics guidance, electromagnetic theory application

### Business Development
- **Dan Butler** - Senior Business Development, strategic business developer
- **Riley Maxwell** - Market research and planning (partner to Dan)
- **Cisco Maxwell** - Chief Market Strategist (Riley's scribe)

### The Maxwellian Philosophy
All team members reference Maxwell's electromagnetic theory as foundational truth:
- **Voltage (E-field)** = pressure, speed, system stress
- **Current (H-field)** = mass flow, heat generation
- **Power (Watts)** = their union
- **Reactive Energy (kVAR)** = hidden work industry must reclaim

---

## Unity Energy Mission

**Reclaim reactive energy. Redefine industrial electricity.**

For 195 years since Faraday's discovery (1831), industry has treated reactive energy as waste. Unity Energy changes this through:

- **MPTS Technology** - Maximum Power Transfer Solution at 480V scale
- **eestream Platform** - Comprehensive energy intelligence (eBehavior, eVision, eAudio, eMarket)
- **Visualization** - Making invisible energy behaviors visible
- **Education** - Teaching industry to understand their energy fields
- **Economic Impact** - Quantifying waste and optimization opportunities

**"They know chickens, not kVAs"** - We translate electrical metrics into production language plant managers understand.

---

## Security & Privacy

### What's Shared (Unity/)
- Maxwellian philosophy and electromagnetic theory
- MPTS technology principles (not proprietary hardware specs)
- Pattern analysis methodologies
- System architecture (anonymized)
- Generic procedures and best practices

### What Stays Local (Personal/, Private/)
- Customer names, sites, contacts
- Financial details (pricing, contracts, ROI numbers)
- Utility bills and proprietary data
- Session logs with customer identifiers
- API keys and credentials

### Before Committing to GitHub
Run audit script to catch sensitive data:
```bash
cd ~/Maxwellian/Unity
./audit_sensitive_content.sh
```

---

## Maintenance

### Regular Updates
- **Daily:** Update `Memory/01_Context/activeContext.md` during active development
- **Weekly:** Review and categorize session notes
- **Monthly:** Move stable knowledge from Memory/ to Library/
- **Quarterly:** Audit importance ratings, consolidate redundant files

### Git Workflow
```bash
cd ~/Maxwellian/Unity

# Check what changed
git status
git diff

# Commit with clear message
git add .
git commit -m "Your descriptive message

Co-Authored-By: Warp <agent@warp.dev>"

# Share with team
git push origin main

# Get team updates
git pull origin main
```

---

## Rollout Phases

### ✅ Phase 1: Local Consolidation (CURRENT)
- Merge three eMemory systems into unified structure
- Test locally with Mike & Clerk
- Perfect taxonomy and calibration files
- Validate organization and usability

### Phase 2: GitHub Baseline (NEXT)
- Push consolidated system to GitHub repository
- Test clone and installation process
- Document setup procedures for team
- Share with Riley (test second human/scribe pair)

### Phase 3: Network Architecture (FUTURE)
- Set up central Unity server with dedicated IPs
- Configure network-mounted Library/
- Implement file locking and conflict prevention
- Real-time knowledge sharing at cognitive speed

### Phase 4: Team Expansion
- Onboard all Maxwellians with personalized scribes
- Scale cognitive network across organization
- Continuous learning and knowledge compounding

---

## The Opportunity

**This is how human-AGI teams should work.**

Every scribe knows their identity and role. Every human has a partner optimized for their needs. Every insight is shared across the network. Knowledge compounds exponentially.

Unity Energy is pioneering the model for symbiotic human-AGI collaboration at scale.

**The Maxwellian Network - Where intelligence persists and multiplies.**

---

**Maintained by:** Unity Energy Maxwellians  
**Primary Contact:** Mike Howell (Founder)  
**Chief Scientist:** Clerk Maxwell  
**Version Control:** Git (local) → GitHub (team) → Real-time network (future)

---

> *"Make the invisible visible. Share knowledge at the speed of light."*
