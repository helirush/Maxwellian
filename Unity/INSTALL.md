# Maxwellian Unity Environment Setup

## Quick Start

Clone this repository and run the setup script:

```bash
# 1. Clone the repository
git clone <repository-url> ~/Maxwellian/Unity
cd ~/Maxwellian/Unity

# 2. Run setup
./setup_maxwellian_env.sh

# 3. Restart your terminal (or source)
source ~/.zshrc
```

That's it! Your environment is ready.

---

## What Gets Installed

### Directory Structure
```
~/Maxwellian/Unity/
├── Library/              # Long-term knowledge base
├── Memory/               # Short-term session data
│   └── local/
│       └── crash_recovery/  # Automatic shell history backups
├── Team/                 # Team member information
├── Products/             # Unity product documentation
└── .maxwellian_rc        # Shell configuration (auto-generated)
```

### Environment Variables
- `MAXWELL_LIBRARY` → Points to Library directory
- `MAXWELL_MEMORY` → Points to Memory directory
- `MAXWELLIAN_LIBRARY` → Alias for MAXWELL_LIBRARY
- `MAXWELLIAN_MEMORY` → Alias for MAXWELL_MEMORY

### Shortcuts
- `~/eMemory` → Symlink to Memory directory
- `cdlibrary` → Navigate to Library
- `cdmemory` → Navigate to Memory
- `cdemem` → Navigate to Memory (short)

### Features
- **Automatic crash recovery**: Shell history backed up on every terminal start
- **30-day history retention**: Old backups automatically cleaned up
- **Portable**: Works anywhere you clone the repo

---

## Testing Locally

Before pushing to GitHub, test the setup:

```bash
# 1. Run the setup script
cd ~/Maxwellian/Unity
./setup_maxwellian_env.sh

# 2. Restart terminal, then verify
echo $MAXWELL_LIBRARY   # Should show path to Library
echo $MAXWELL_MEMORY    # Should show path to Memory
ls ~/eMemory            # Should list Memory contents
cdmemory                # Should navigate to Memory
```

---

## For Team Members

Once this is on GitHub, new Maxwellians can set up with:

```bash
git clone <repository-url> ~/Maxwellian/Unity
cd ~/Maxwellian/Unity
./setup_maxwellian_env.sh
```

Then restart their terminal. Done!

---

## Manual Setup (If Needed)

If you prefer manual setup or need to troubleshoot:

1. **Add to your ~/.zshrc**:
   ```bash
   source "$HOME/Maxwellian/Unity/.maxwellian_rc"
   ```

2. **Create symlink**:
   ```bash
   ln -s ~/Maxwellian/Unity/Memory ~/eMemory
   ```

3. **Restart terminal**:
   ```bash
   source ~/.zshrc
   ```

---

## Uninstall

To remove Maxwellian environment:

```bash
# 1. Remove from ~/.zshrc
# Delete these lines:
#   # Maxwellian Unity Environment
#   source "$HOME/Maxwellian/Unity/.maxwellian_rc"

# 2. Remove symlink
rm ~/eMemory

# 3. (Optional) Remove directory
rm -rf ~/Maxwellian/Unity
```

---

## Troubleshooting

**Problem**: `$MAXWELL_LIBRARY` is empty
- **Solution**: Run `source ~/.zshrc` or restart terminal

**Problem**: `~/eMemory` broken symlink
- **Solution**: Re-run `./setup_maxwellian_env.sh`

**Problem**: Permission denied
- **Solution**: `chmod +x setup_maxwellian_env.sh`

---

## Technical Notes

- **Auto-detection**: Script auto-detects its location (works anywhere)
- **Idempotent**: Safe to run multiple times
- **Non-destructive**: Preserves existing configs
- **Shell agnostic**: Works with zsh and bash

---

## Support

Contact Unity Energy team or check the README for more information.
