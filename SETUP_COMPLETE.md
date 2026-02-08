# Maxwellian Knowledge Base - Setup Complete ✅

**Date:** 2026-01-16  
**Initialized by:** Clerk (AI Scribe for Mr. Howell)

---

## What We Built

### 1. Privacy-Preserving Architecture

```
/Users/mdhowell/Maxwellian/
├── .gitignore              ← Protects Personal/ and Private/ from Git
├── Unity/                  ← SHARED via GitHub → Maxwellian.ai
│   ├── .git/               (initialized, branch: main)
│   ├── .gitignore          (protects sensitive patterns)
│   ├── README_UNITY.md     (explains purpose and usage)
│   ├── Memory/             (technical documentation)
│   ├── Library/            (reference materials)
│   ├── Team/               (Scribe coordination)
│   └── Products/           (MPTS, eStream docs)
│
├── Personal/               ← PRIVATE (your workspace, never committed)
│
└── Private/                ← PRIVATE (sensitive data, never committed)
    ├── README_PRIVATE.md
    ├── CustomerFiles/      (Foster Farms, etc.)
    ├── Financial/          (pricing, contracts, ROI)
    ├── Sessions/           (work logs with customer context)
    └── Technical/          (customer-specific implementations)
```

### 2. Environment Variables (Already in .zshrc)

```bash
export MAXWELL_MEMORY="$HOME/Maxwellian/Unity/memory"
export MAXWELL_LIBRARY="$HOME/Maxwellian/Unity/memory"
export MAXWELLIAN_MEMORY="$HOME/Maxwellian/Unity/memory"
export MAXWELLIAN_LIBRARY="$HOME/Maxwellian/Unity/memory"
```

### 3. Git Protection

- ✅ Root `.gitignore` blocks `Personal/` and `Private/` directories
- ✅ Unity `.gitignore` blocks sensitive patterns (API keys, customer names, financial docs)
- ✅ Git initialized in `Unity/` with `main` branch
- ✅ Ready for GitHub remote connection

---

## What's Protected

### Never Leaves Your Machine
- Customer names, sites, contacts (Foster Farms, Cherry Ave, etc.)
- Financial details (pricing, quotes, contracts, specific ROI numbers)
- Utility bills and proprietary energy data
- Session work logs with customer identifiers
- API keys and credentials

### Shared with Team (Unity/)
- Maxwellian philosophy and electromagnetic field theory
- MPTS technology principles and sizing methodologies  
- Pattern analysis training and visual interpretation techniques
- System architecture (eStream, eVision, eBehavior)
- Generic procedures and best practices (anonymized examples only)

---

## Next Steps

### Step 1: Audit Current Content (RECOMMENDED BEFORE FIRST COMMIT)

```bash
cd /Users/mdhowell/Maxwellian/Unity
./audit_sensitive_content.sh
```

This script scans for:
- Customer names (Foster, Farms, Livingston, Cherry)
- Financial patterns ($, invoice, contract, pricing)
- Credentials (API keys, passwords)

Review flagged files and either:
1. **Generalize:** Replace "Foster Farms" with "Customer A" or "Large poultry processor"
2. **Move:** `mv Memory/file.md ../Private/CustomerFiles/`
3. **Redact:** Remove specific dollar amounts, keep methodology

### Step 2: Create GitHub Repository

```bash
# On GitHub.com:
# 1. Create new repository: UnityEnergy/Unity (or Maxwellian/Unity)
# 2. Set as Private initially (can make public later after review)
# 3. Do NOT initialize with README (we already have one)

# Connect local repo to GitHub:
cd /Users/mdhowell/Maxwellian/Unity
git remote add origin git@github.com:UnityEnergy/Unity.git

# Verify remote
git remote -v
```

### Step 3: First Commit (After Audit)

```bash
cd /Users/mdhowell/Maxwellian/Unity

# Check what will be committed
git status
git diff

# Stage files (carefully!)
git add .

# Commit with attribution
git commit -m "Initialize Unity Knowledge Base - Maxwellian Library

Foundational knowledge for Unity Energy AI Scribe team.
Includes electromagnetic field theory, MPTS technology,
pattern analysis methods, and system documentation.

Co-Authored-By: Warp <agent@warp.dev>"

# Push to GitHub
git push -u origin main
```

### Step 4: Set Up Team Access

```bash
# On GitHub.com repository settings:
# 1. Settings → Collaborators
# 2. Add Riley's GitHub username with Write access
# 3. Add Sol's GitHub username with Write access
# 4. Share clone instructions with team
```

### Step 5: Team Member Setup (For Riley, Sol, etc.)

```bash
# Clone the Unity knowledge base
mkdir -p ~/Maxwellian
cd ~/Maxwellian
git clone git@github.com:UnityEnergy/Unity.git

# Verify environment variables in their .zshrc
echo $MAXWELL_MEMORY      # Should point to ~/Maxwellian/Unity/Memory
echo $MAXWELLIAN_LIBRARY  # Should point to ~/Maxwellian/Unity/Memory

# If not set, add to their .zshrc:
export MAXWELL_MEMORY="$HOME/Maxwellian/Unity/memory"
export MAXWELL_LIBRARY="$HOME/Maxwellian/Unity/memory"
export MAXWELLIAN_MEMORY="$HOME/Maxwellian/Unity/memory"
export MAXWELLIAN_LIBRARY="$HOME/Maxwellian/Unity/memory"
```

### Step 6: Warp MCP Memory Configuration

Verify that Warp's Memory MCP is reading from the correct location:

```bash
# Check current MCP Memory storage location
# (This requires checking Warp's MCP settings - may need GUI)

# The Memory MCP should read from:
# /Users/mdhowell/Maxwellian/Unity/Memory

# If it's using a different location, we may need to:
# 1. Update MCP configuration
# 2. Or create symlink from MCP location to our Memory directory
```

---

## MCP Integration

### Current State
- ✅ Memory MCP installed and working (confirmed via knowledge graph read)
- ❓ Need to verify it's reading from `/Users/mdhowell/Maxwellian/Unity/Memory`

### How It Works
When you start a new Warp thread:
1. AI Scribe should read Memory MCP knowledge graph
2. Establishes baseline awareness from shared knowledge
3. Applies context throughout the conversation
4. Before thread closes, asks if anything should be captured to memory

### Thread Initialization Rule
Add to Warp rules or AI instructions:
```
Upon thread initialization:
1. Read Memory MCP knowledge graph
2. Establish baseline awareness
3. Apply Maxwellian context to all work

Before thread exit:
1. Ask user: "Should I capture anything from this session to memory?"
2. If yes, document key learnings/decisions
```

---

## Publishing to Maxwellian.ai

Once the baseline is solid and reviewed:

1. **Make Repository Public** (on GitHub)
2. **Update Maxwellian.ai** to link to the knowledge base
3. **Add Documentation Badge** to README
4. **Create Onboarding Guide** for new Scribes

The website will serve as the entry point, GitHub hosts the actual knowledge, and each Scribe clones it locally for MCP access.

---

## Maintenance

### Regular Audits
```bash
cd /Users/mdhowell/Maxwellian/Unity
./audit_sensitive_content.sh
```

Run this periodically to catch any accidentally committed sensitive data.

### Contributing New Knowledge
```bash
# Create/edit files in Unity/Memory/
vim Memory/NEW_LEARNING.md

# Check what changed
git status
git diff

# Commit with clear message
git add Memory/NEW_LEARNING.md
git commit -m "Add [topic] - [brief description]

Co-Authored-By: Warp <agent@warp.dev>"

# Share with team
git push origin main
```

### Team Synchronization
Each Scribe should regularly:
```bash
cd ~/Maxwellian/Unity
git pull origin main
```

This keeps everyone's baseline knowledge synchronized.

---

## Security Checklist

- ✅ `.gitignore` protects `Personal/` and `Private/`
- ✅ Unity `.gitignore` blocks sensitive patterns
- ✅ Audit script available to scan for leaks
- ✅ README documents what belongs where
- ⏳ Audit current Memory/ files before first commit
- ⏳ Verify MCP Memory reads from correct location
- ⏳ Test with team member before wide rollout

---

## Questions & Next Actions

**For Mr. Howell:**

1. **Review Privacy Architecture** - Does this structure meet your requirements?
2. **Run Audit** - Execute `./audit_sensitive_content.sh` and review findings
3. **Move Sensitive Files** - Relocate customer-specific docs to Private/
4. **GitHub Setup** - Create repository (public or private initially?)
5. **MCP Verification** - Check if Memory MCP reads from Unity/Memory/
6. **Team Rollout** - When to give Riley/Sol access?

**Priority:** Run the audit script first before making any commits.

---

**Setup completed by:** Clerk  
**For questions:** Reference this document and Memory MCP knowledge graph  
**Next session:** Review audit results and prepare first commit

---

> *"The field was broken. We restore it."*  
> — The Maxwellian Mission
