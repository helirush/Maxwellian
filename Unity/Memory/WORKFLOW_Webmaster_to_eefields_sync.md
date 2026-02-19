# Webmaster → eefields Sync Workflow

Purpose: Keep the public eefields repo in lockstep with local eWebmaster staging so the customer portal stays consistent.

## When to run
- After any change under `eWebmaster/` (HTML, JS, images, studies)
- Before publishing or sharing a URL with a customer

## Steps
1) Local QA in eWebmaster
- Start local server: `python3 -m http.server 8000 --directory ~/eestream/eWebmaster`
- Click through Cherry and Livingston pages (hero, libraries, study links, Deli summaryboard Full Analysis buttons)
- Verify `passwords.js` has `devMode=false` and `password: "oHeaviside"`

2) Sync to eefields
- `rsync -av --delete --exclude='.git' --exclude='.DS_Store' ~/eestream/eWebmaster/ ~/eestream/eefields/`

3) Commit + push (eefields)
- `cd ~/eestream/eefields`
- `git add -A && git commit -m "Sync from eWebmaster: <short summary>\n\nCo-Authored-By: Warp <agent@warp.dev>"`
- `git push origin main`

4) Commit + push (eestream) to capture staging changes
- `cd ~/eestream`
- `git add -A && git commit -m "Update eWebmaster: <short summary>\n\nCo-Authored-By: Warp <agent@warp.dev>"`
- `git push origin main`

5) Verify GitHub Pages
- Wait 2–5 minutes, then load the public site
- Smoke test password gate (use `oHeaviside`), Cherry + Livingston pages

## Notes
- Pattern filenames use the simplified convention: `{tid}{prefix}_{monthSuffix}.png` (no PF codes).
- Full Analysis modal shows BT (top), Hardware (center), Simulator (bottom) and auto-scrolls images during Unity audio.
- Video thumbnails (e.g., `ChickenFootball.mp4`) are preview-only: muted, looped, no click-to-expand.
