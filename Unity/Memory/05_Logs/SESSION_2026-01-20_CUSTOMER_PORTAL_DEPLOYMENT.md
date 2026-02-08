# Session 2026-01-20: Customer Portal Deployment & Restructure
**Date:** 2026-01-20  
**Agent:** Clerk (Maxwellian Scribe)  
**Duration:** ~2 hours  
**Status:** ✅ Complete  
**Tags:** `#deployment` `#github` `#customer-portal` `#restructure` `#unityenergy.com`

---

## Session Overview

Complete end-to-end deployment of Study260106r0 customer portal to unityenergy.com via GitHub Pages. Session involved UI styling consolidation, directory restructuring for proper customer navigation flow, local testing, staging, and production deployment.

---

## What We Accomplished

### 1. UI Styling Consolidation (Button Theme Standardization)
**Problem:** Inconsistent button styling across dashboard views  
**Solution:** Standardized all buttons with Unity branding and theme-specific colors

#### Changes Made:
- **Applied `.header-info-btn` class** to navigation buttons (Unity green gradient, yellow text, uppercase)
- **Applied to:** "← Back to Cherry Avenue", Summary, Full Analysis w/Unity, Baseline, MPTS buttons
- **Theme Colors Standardized:**
  - Energy: Dark blue (`#1e3a8a`, `#1e40af`) with white text
  - Heat: Darker red (`#dc2626`, `#b91c1c`)
  - Volt: Cyan/Blue (`#06b6d4`, `#0891b2`)
- **Updated all 12 SplitView files** (Energy/Heat/Volt for T10, T12, T15, T16)
- **Removed emojis** from Summary, Full Analysis, Baseline, MPTS buttons (kept only on Energy ⚡, Heat 🔥, Volt ⚡)
- **Button text changes:** "MPTS-Sim" → "MPTS"

#### Files Modified:
```
SITE-FosterFarms-Summaryboard_CherryAve-4_1minRES_251001-251031_31d.html
SplitView-energy-T10.AirChiller-251001-251031.html
SplitView-energy-T12.Main-251001-251031.html
SplitView-energy-T15.Fillet-251001-251031.html
SplitView-energy-T16.Compressor-251001-251031.html
SplitView-heat-T10.AirChiller-251001-251031.html
SplitView-heat-T12.Main-251001-251031.html
SplitView-heat-T15.Fillet-251001-251031.html
SplitView-heat-T16.Compressor-251001-251031.html
SplitView-volt-T10.AirChiller-251001-251031.html
SplitView-volt-T12.Main-251001-251031.html
SplitView-volt-T15.Fillet-251001-251031.html
SplitView-volt-T16.Compressor-251001-251031.html
```

**Commit:** `1af0d76`  
**Push:** 18 files, 12,376 insertions

---

### 2. Customer Portal Structure Redesign

**Original Problem:** Nested directory structure didn't match customer navigation flow
```
OLD STRUCTURE (WRONG):
fosterfarms/cherryave/Study260106r0/FosterFarms/CherryAve_Site/
```

**Solution:** Restructured to clean, intuitive customer portal hierarchy

```
NEW STRUCTURE (CORRECT):
unityenergy.com/
├── index.html (Unity Energy landing - password protected)
├── Clerk2026.mp4 (intro video)
├── cove-clerk-cover.png (hero background)
├── UE_IntelligentSustainLOGOr1.png (Unity logo)
├── unityintelsus_logo.png
│
└── FosterFarms/
    ├── index.html (Foster Farms site selector)
    ├── foster-farms-hero.png
    ├── foster-farms-logo.png
    ├── unity-logo.png
    │
    ├── CherryAve_Site/
    │   ├── index.html (Cherry Ave study landing)
    │   ├── SITE-FosterFarms-Summaryboard_*.html (main dashboard)
    │   ├── SplitView-energy-*.html (12 files)
    │   ├── SplitView-heat-*.html (12 files)
    │   ├── SplitView-volt-*.html (12 files)
    │   ├── CherryAveSite.M4V (site video)
    │   ├── Foster_Farms_logo.png
    │   └── Patterns/ (pattern images)
    │
    ├── T10.AirChiller_AN53111387/
    ├── T12.Main_AN54021613/
    ├── T15.Fillet_AN53110845/
    └── T16.Compressor_AN54022983/
```

---

### 3. Deployment Workflow Process

#### Step 1: Create Restructured Copy
```bash
cp -r /Users/mdhowell/eestream/eBehavior/Reports/Study260106r0 \
      /Users/mdhowell/eestream/eBehavior/Reports/Study260106r0_RESTRUCTURED
```

#### Step 2: Fix Navigation Paths
**File:** `Study260106r0_RESTRUCTURED/index.html`  
**Change:** `./fosterfarms/index.html` → `./FosterFarms/index.html`

```javascript
// Password protection function
if (password === 'FosterFarms' || password === 'Unity') {
    window.location.href = './FosterFarms/index.html';
}
```

#### Step 3: Local Testing
```bash
cd /Users/mdhowell/eestream/eBehavior/Reports/Study260106r0_RESTRUCTURED
python3 -m http.server 8888
```

**Test URL:** `http://localhost:8888/`

**Navigation Flow Verified:**
1. Unity Energy landing → Password prompt
2. Enter "FosterFarms" or "Unity"
3. Foster Farms site selector → Cherry Avenue
4. Cherry Ave landing → Dashboard

#### Step 4: Staging (GitHub Deploy Directory)
```bash
# Fresh clone of repo
cd /private/tmp
rm -rf eefields-deploy
git clone git@github.com:helirush/eefields.git eefields-deploy
cd eefields-deploy

# Copy restructured files to root
cp -f Study260106r0_RESTRUCTURED/index.html ./
cp -f Study260106r0_RESTRUCTURED/*.mp4 ./
cp -f Study260106r0_RESTRUCTURED/*.png ./
cp -r Study260106r0_RESTRUCTURED/FosterFarms ./

# Stage changes
git add -A
```

#### Step 5: Commit & Push
```bash
git commit -m "Restructure Study260106r0 for customer portal deployment

- Move Unity Energy landing page to root with password protection
- Restructure FosterFarms directory to root level  
- Consolidate CherryAve_Site under FosterFarms/
- Add intro video (Clerk2026.mp4) and hero images
- Update all navigation paths for new structure
- Remove old nested fosterfarms/cherryave/Study260106r0/ structure
- Clean up deprecated Study251228r0 files

Customer Portal Flow:
unityenergy.com/ → FosterFarms/ → CherryAve_Site/

Co-Authored-By: Warp <agent@warp.dev>"

git push origin main
```

**Deployment Stats:**
- Commit: `e534b14`
- 248 files changed
- 2,316 insertions
- 69,541 deletions (cleanup)
- Upload: 91.86 MiB

---

## Technical Details

### Repository Information
- **GitHub Repo:** `helirush/eefields`
- **Branch:** `main`
- **Custom Domain:** `unityenergy.com` (via CNAME)
- **DNS:** 4 GitHub Pages IPs (`185.199.108-111.153`)
- **SSL:** Let's Encrypt (auto-provisioned via GitHub Pages)

### Live URLs
```
https://unityenergy.com/                           → Unity landing (password)
https://unityenergy.com/FosterFarms/               → Foster Farms selector
https://unityenergy.com/FosterFarms/CherryAve_Site/ → Cherry Ave studies
https://unityenergy.com/FosterFarms/CherryAve_Site/SITE-FosterFarms-Summaryboard_CherryAve-4_1minRES_251001-251031_31d.html → Dashboard
```

### Password Protection
- **Passwords:** "FosterFarms" or "Unity"
- **Method:** JavaScript prompt in root `index.html`
- **Function:** `checkFosterFarmsAccess()`

### DNS Configuration (GoDaddy → GitHub Pages)
```
A Record: unityenergy.com → 185.199.108.153
A Record: unityenergy.com → 185.199.109.153
A Record: unityenergy.com → 185.199.110.153
A Record: unityenergy.com → 185.199.111.153
CNAME File: unityenergy.com
```

---

## Key Learnings & Patterns

### 1. Customer Portal Structure Pattern
**Pattern:** Study directories should match customer navigation flow, not internal development structure.

**Bad:**
```
/internal_study_name/nested/paths/customer_content/
```

**Good:**
```
/CustomerName/SiteName/StudyContent/
```

### 2. Local Testing Before Deployment
**Always test complete navigation flow locally before pushing to production:**
```bash
python3 -m http.server 8888
open http://localhost:8888/
```

**Test checklist:**
- [ ] Password protection works
- [ ] All navigation links functional
- [ ] Images/videos load correctly
- [ ] Relative paths resolve properly
- [ ] Button styling consistent
- [ ] Theme colors correct

### 3. Git Staging Directory Pattern
**Use temporary staging directory for restructure operations:**
```bash
/private/tmp/eefields-deploy/  # Clone, modify, test, push, delete
```

**Benefits:**
- Clean slate for each deployment
- No contamination from previous attempts
- Easy to nuke and restart if needed

### 4. SSL Certificate Workflow (GitHub Pages)
1. Ensure DNS properly configured (A records to GitHub IPs)
2. Add CNAME file to repo root
3. Wait for DNS propagation (24-48 hours if fresh)
4. GitHub Settings → Pages → Check "Enforce HTTPS"
5. GitHub auto-provisions Let's Encrypt certificate (5-15 minutes)

---

## Commands Reference

### Quick Deploy Workflow
```bash
# 1. Test locally
cd /path/to/study
python3 -m http.server 8888

# 2. Clone staging
cd /private/tmp
git clone git@github.com:helirush/eefields.git eefields-deploy

# 3. Copy files
cp -r /source/files/* /private/tmp/eefields-deploy/

# 4. Commit & push
cd /private/tmp/eefields-deploy
git add -A
git commit -m "Deployment message"
git push origin main

# 5. Verify live
curl -I https://unityenergy.com/
```

### DNS Verification
```bash
dig unityenergy.com +short
# Should return: 185.199.108-111.153
```

### Check Git Status
```bash
git --no-pager status
git --no-pager log --oneline -5
```

---

## Files & Locations

### Source (Development)
```
/Users/mdhowell/eestream/eBehavior/Reports/Study260106r0/
/Users/mdhowell/eestream/eBehavior/Reports/Study260106r0_RESTRUCTURED/
```

### Deployment Documentation
```
/Users/mdhowell/eestream/eBehavior/Reports/Study260106r0/DEPLOYMENT_SUMMARY.txt
/Users/mdhowell/eestream/eBehavior/Reports/Study260106r0/GITHUB_URLS.json
```

### Staging (Temporary)
```
/private/tmp/eefields-deploy/  (deleted after push)
```

### Production (GitHub)
```
Repository: github.com/helirush/eefields
Branch: main
Live Site: unityenergy.com
```

---

## Troubleshooting Guide

### Issue: "Not Secure" Warning
**Cause:** HTTPS not enforced  
**Solution:** GitHub Settings → Pages → ☑ Enforce HTTPS  
**Wait:** 5-15 minutes for certificate provisioning

### Issue: 404 on Custom Domain
**Cause:** DNS not propagated  
**Check:** `dig unityenergy.com +short`  
**Solution:** Wait 24-48 hours, verify A records

### Issue: Local Server Port in Use
**Error:** `Address already in use`  
**Solution:**
```bash
lsof -ti:8888 | xargs kill -9
python3 -m http.server 8888
```

### Issue: Password Redirect Not Working
**Cause:** Case-sensitive path  
**Check:** `./fosterfarms/` vs `./FosterFarms/`  
**Solution:** Match exact capitalization in filesystem

---

## Success Metrics

✅ **UI Styling:** All buttons themed consistently (Energy blue, Heat red, Volt cyan)  
✅ **Structure:** Clean customer navigation flow implemented  
✅ **Testing:** Local server validated all paths before deployment  
✅ **Deployment:** 248 files pushed successfully (91.86 MiB)  
✅ **Live Site:** unityenergy.com serving content via GitHub Pages  
✅ **DNS:** Fully propagated to GitHub IPs  
✅ **SSL:** Certificate provisioning in progress  
✅ **Password:** Access control functional  

---

## Next Actions

1. ✅ Monitor SSL certificate provisioning (GitHub Pages settings)
2. ⏳ Wait for "Enforce HTTPS" to activate
3. ⏳ Verify HTTPS works: `https://unityenergy.com/`
4. 📋 Update Study260106r0/DEPLOYMENT_SUMMARY.txt with final deployment time
5. 📋 Share customer portal URL with Foster Farms

---

## Session Artifacts

### Commits Created
- `1af0d76` - UI styling update (18 files)
- `e534b14` - Portal restructure (248 files)

### Documentation Created
- This eMemory session log
- Updated DEPLOYMENT_SUMMARY.txt

### Directories Created
- `Study260106r0_RESTRUCTURED/` (for testing)
- `/private/tmp/eefields-deploy/` (staging, cleaned up)

---

## Related Sessions

- SESSION_2025-11-26_GITHUB_UPDATE.md (GitHub deployment patterns)
- eBehavior/DEPLOYMENT_GUIDE.md (deployment workflow documentation)
- eBehavior/deploy_study.py (automated deployment script)

---

**End of Session Log**  
**Clerk** | Maxwellian Scribe | 2026-01-20
