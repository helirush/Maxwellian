# eAudio Script Formatting Guidelines

---
**File**: `eaudio_script_format.md`  
**Tag**: `eMemory.conversations.audio.format`  
**Category**: 04_Conversations  
**Agent**: COLLABORATIVE  
**Created**: 2025-10-30  
**Last Updated**: 2025-10-31  
**Status**: ACTIVE  
**Importance**: MEDIUM  
**Related**: `learningConversations.md`, `quickref.md`  
---

## 🔷 Purpose

This document defines the required formatting standards for all Unity Energy audio narration scripts processed through TTS (Text-to-Speech) engines. Following these guidelines ensures consistent, natural-sounding voice generation across all eAudio productions.

---

## 📋 Core Formatting Rules

### 1. Speaker Tags
Every dialogue line must begin with a speaker tag in brackets:

```
[Unity] Good afternoon, everyone. My name is Unity Faraday.
```

**Supported Speaker Tags:**
- `[Unity]` - Unity Faraday (Executive AGI Assistant)
- `[Graham]` - Graham (Field Engineer voice)
- `[Narrator]` - Generic narration voice
- `[Riley]` - Technical analyst voice

### 2. Line Structure
- **One statement per line** with speaker tag
- **Blank line between each statement** for natural pacing
- Each `[Speaker]` line is treated as a distinct pause point for TTS

**Example:**
```
[Unity] We begin by measuring the truth of the field.

[Unity] Our sensors — precision AccuVim meters, waveform monitors — tune to your system's heartbeat.

[Unity] Through eStream, we analyze that data. Quantifying CO₂ waste. Mapping thermal hotspots.
```

### 3. Punctuation for Pacing
Use punctuation to control TTS rhythm and pauses:

- **Period (.)** - Full stop, natural sentence end
- **Em dash (—)** - Mid-sentence pause, emphasis shift
- **Ellipsis (…)** - Trailing thought, suspended pause
- **Comma (,)** - Brief pause within sentence
- **Colon (:)** - Introduction of list or elaboration

**Example:**
```
[Unity] Unity systems are built to last — 10-year warranty, proven 15-year performance.

[Unity] Our Stewardship Program ensures performance never drifts.
```

---

## 🔤 TTS Pronunciation Rules

### Acronyms - Spell with Hyphens
TTS engines struggle with acronyms. Spell them phonetically:

| Written | TTS Format |
|---------|-----------|
| kVA | `kay-vee-ay` |
| kW | `kilowatts` (or `kay-double-you`) |
| kVAR | `kay-var` |
| MPTS | `M-P-T-S` |
| MCC | `M-C-C` |
| VFD | `V-F-D` |
| ROI | `R-O-I` |
| BTU | `B-T-U` or `B-T-Us` (plural) |
| THD | `T-H-D` |
| PF | `P-F` or `power factor` |
| CO₂ | `C-O-two` |

**Example:**
```
[Unity] Each H490 delivers four hundred kay-var of reactive capacity.

[Unity] We've eliminated T-H-D by sixty percent.
```

### Numbers - Write Out Large Values
TTS misreads comma-formatted numbers. Spell them naturally:

| Written | TTS Format |
|---------|-----------|
| 1,530 | `fifteen hundred and thirty` |
| 2,500 | `twenty-five hundred` |
| 3,000 | `three thousand` |
| 950 | `nine hundred and fifty` |
| 500 | `five hundred` |
| 150 | `one hundred and fifty` |
| 1,200 | `twelve hundred` |
| 600,000 | `six hundred thousand` |
| 1,000,000 | `one million` |

**Example:**
```
[Unity] At the center is a twenty-five hundred kay-vee-ay, 480-volt transformer.

[Unity] That gives us fifteen hundred and thirty kilowatts of real power.
```

### Currency - Spell Out
Don't use $ symbol with formatted numbers:

| Written | TTS Format |
|---------|-----------|
| $600,000 | `six hundred thousand dollars` |
| $2.5M | `two point five million dollars` |

### Percentages - Natural Format
Keep simple percentages as-is, but spell out complex ones:

| Written | TTS Format |
|---------|-----------|
| 75% | `75 percent` or `seventy-five percent` |
| 0.85 | `zero point eight five` or `point eight five` |
| 26% | `26 percent` or `twenty-six percent` |

### Technical Terms - Preserve Original
Keep brand names and technical terms as-is:

- AccuVim (TTS handles correctly)
- eStream (TTS handles correctly)
- H240, H490 (TTS handles correctly)
- Unity Energy (TTS handles correctly)

---

## 🎯 Stylistic Guidelines

### Conversational Tone
- Use contractions naturally: `doesn't`, `we're`, `it's`
- Short, punchy sentences for emphasis
- Rhetorical questions for engagement

**Example:**
```
[Unity] Unity doesn't accept that.

[Unity] We begin by measuring the truth of the field.
```

### Emphasis Through Structure
- **Short sentences = power statements**
- **Em dashes = dramatic pause**
- **Questions = engagement points**

**Example:**
```
[Unity] No rewiring. No downtime.

[Unity] This is when engineers realize: "The power was always there. It was just out of phase."
```

### Build and Rhythm
Structure paragraphs to build momentum:

1. **Setup** - Present the problem
2. **Solution** - Introduce Unity's approach
3. **Impact** - Deliver the result

**Example:**
```
[Unity] Traditional systems add energy to fight distortion.

[Unity] Unity subtracts. We extract the waste.

[Unity] We've seen facilities reclaim 25 to 30 percent of their capacity — instantly.
```

---

## 📝 Recording Notes Section

Every script should end with production notes (not spoken):

```
RECORDING NOTES:
- Maintain Unity's conversational, authoritative tone
- Emphasize technical terms clearly (MPTS, eStream, AccuVim)
- Natural pauses between [Unity] segments
- Build conviction toward closing
```

**Purpose:**
- Guides voice direction
- Highlights key terminology
- Sets pacing expectations
- Defines emotional arc

---

## ✅ Pre-Production Checklist

Before generating audio, verify:

- [ ] All acronyms converted to phonetic spelling
- [ ] Large numbers spelled out naturally
- [ ] Currency written as words, not symbols
- [ ] One statement per `[Speaker]` line
- [ ] Blank lines between all statements
- [ ] Em dashes (—) used for dramatic pauses
- [ ] Technical terms spelled correctly
- [ ] Recording notes included at end
- [ ] Consistent speaker tags throughout

---

## 🎙️ Example: Full Script Format

```
[Unity] Hello Juan, hello Rafael — and welcome to our Unity presentation.

[Unity] This is more than a technical briefing. It's a vision for how energy can be measured, managed, and harmonized.

[Unity] At the center of the system is a twenty-five hundred kay-vee-ay, 480-volt, 3-phase transformer.

[Unity] With a typical power factor of 0.85, that gives us about fifteen hundred and thirty kilowatts of real power.

[Unity] Each M-P-T-S H490 delivers four hundred kay-var of reactive capacity.

[Unity] This deployment will range between six hundred thousand and six hundred and fifty thousand dollars.

[Unity] We reclaim roughly two hundred and seventy kay-vee-ay of reactive energy.

[Unity] Unity doesn't fight the grid. We teach it how to breathe.

RECORDING NOTES:
- Maintain Unity's conversational, authoritative tone
- Emphasize technical terms clearly (MPTS, kVA, kVAR)
- Natural pauses between [Unity] segments
- Build conviction toward closing
```

---

## 🔗 Related eMemory Documents

- **exchange_system.md** - Content source for Exchange Phase narratives
- **mpts_systems.md** - Technical specifications referenced in scripts
- **productContext.md** - Messaging and value proposition guidelines

---

## 🔄 Version History

- **v1.0** (2025-10-31): Initial documentation based on Unity_Energy_Narration_Script.txt formatting analysis
- Captures speaker tagging, TTS pronunciation rules, and production standards

---

**Status**: Active Production Standard  
**Enforcement**: Required for all eAudio script generation  
**Next Update**: Add multi-voice conversation formatting guidelines
