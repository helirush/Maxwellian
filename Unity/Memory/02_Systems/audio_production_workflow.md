# Audio Production Workflow — Unity Energy eAudio System

---
**File**: `audio_production_workflow.md`  
**Tag**: `eMemory.systems.audio.production`  
**Category**: 02_Systems  
**Agent**: CLERK  
**Created**: 2025-12-05  
**Last Updated**: 2025-12-05  
**Status**: ACTIVE  
**Importance**: HIGH  
**Related**: `eaudio_script_format.md`, `activeContext.md`  
---

## 🎯 Purpose

This document captures the complete workflow for preparing, generating, and producing audio content for Unity Energy's eAudio system. It covers script preparation, TTS tool usage, voice selection methodology, and production best practices developed by the Maxwellian team.

---

## 🏗️ System Architecture

### **eAudio System Components**

```
eAudio/
├── eMultiVoiceTTS.py        ← Multi-speaker dialogue generator (ElevenLabs + OpenAI)
├── eSingleVoiceTTS.py        ← Single-voice narration (OpenAI TTS-1/HD)
├── [Project Folders]         ← Organized by customer/content type
│   ├── CompanyIntros/
│   ├── FosterFarms/
│   ├── LakeNona/
│   ├── UnitySpeak/
│   └── UnityMemoryThreads/
└── Test Audio Files           ← Voice testing samples
```

### **Voice Provider Options**

1. **OpenAI TTS** (tts-1, tts-1-hd)
   - Voices: alloy, echo, fable, onyx, nova, shimmer
   - Speed control: 0.85x - 1.2x
   - Best for: Single narrator, quick production

2. **ElevenLabs**
   - Professional voice library (100+ voices)
   - Emotion and delivery control
   - Best for: Multi-character dialogue, high production value

---

## 📋 Audio Production Workflow

### **Phase 1: Script Preparation**

#### **Step 1: Write or Generate Script Content**
- Create dialogue or narration content
- Identify speakers/characters
- Structure for conversational flow

#### **Step 2: Format Script for TTS**
Follow `eaudio_script_format.md` standards:

**Speaker Tagging:**
```
[UNITY] Good afternoon, everyone. Welcome to Unity Energy.

[CLERK] Thank you, Unity. It's good to be here.

[GRAHAM] Let me walk you through the technical details.
```

**Key Formatting Rules:**
- **One statement per line** with speaker tag
- **Blank line between statements** for pacing
- **Spell out acronyms**: kVA → `kay-vee-ay`, MPTS → `M-P-T-S`
- **Write out numbers**: 1,530 → `fifteen hundred and thirty`
- **Currency as words**: $600,000 → `six hundred thousand dollars`
- **Use em dashes (—)** for dramatic pauses
- **Ellipsis (…)** for trailing thoughts

#### **Step 3: Add Production Notes**
```
RECORDING NOTES:
- Maintain Unity's conversational, authoritative tone
- Emphasize technical terms clearly (MPTS, eStream, AccuVim)
- Natural pauses between speaker segments
- Build conviction toward closing
```

---

### **Phase 2: Voice Selection & Configuration**

#### **Single-Voice Production (eSingleVoiceTTS.py)**

**When to Use:**
- Simple narration
- Company introductions
- Technical explanations
- Quick turnaround needed

**Voice Selection Strategy:**

| Voice | Character | Best For |
|-------|-----------|----------|
| **onyx** | Authoritative, deep | Executive presentations, technical authority |
| **nova** | Warm, engaging | Customer-facing, educational content |
| **alloy** | Neutral, clear | Documentation, training materials |
| **shimmer** | Bright, friendly | Marketing, introductions |
| **echo** | Professional, balanced | General purpose narration |
| **fable** | Expressive, dynamic | Storytelling, engaging content |

**Speed Profiles:**
- **0.85x** - Deliberate, authoritative (executive briefings)
- **0.95x** - Thoughtful, clear (technical explanations)
- **1.0x** - Standard pace (general content)
- **1.05x** - Engaging, energetic (marketing)
- **1.10x** - Fast-paced (demos, overviews)

**Model Selection:**
- **tts-1** - Standard quality, faster generation
- **tts-1-hd** - Premium quality, slower generation (production use)

#### **Multi-Voice Production (eMultiVoiceTTS.py)**

**When to Use:**
- Dialogue between characters
- Interviews and Q&A
- Team briefings
- Educational conversations

**Voice Pairing Strategy:**

**Founder Circle Voices:**
- **UNITY** (Executive AGI) - Professional female, authoritative
- **CLERK** (Chief Scientist) - Mature male, thoughtful
- **COVE** (Physics Guide) - Wise, technical male
- **GRAHAM** (Field Engineer) - Practical, clear male

**Provider Modes:**
1. **Single Provider** - All voices from OpenAI OR ElevenLabs
2. **Mixed Provider** - Combine OpenAI + ElevenLabs for character variety

**Configuration Options:**
```python
# Sequential voice assignment per speaker
# Customize per-speaker: voice, speed, stability, similarity
```

---

### **Phase 3: Audio Generation**

#### **Single-Voice Generation**

**Command:**
```bash
cd ~/eestream/eAudio
python3 eSingleVoiceTTS.py
```

**Interactive Prompts:**
1. Select voice (1-6)
2. Select model quality (standard/HD)
3. Select speaking speed (0.85x - 1.2x)
4. Provide text file path
5. Specify output MP3 name

**Example Session:**
```
🎤 OpenAI Text-to-Speech Generator
📝 Using model: tts-1-hd

🎭 Select a voice:
   1. Alloy
   2. Echo
   3. Fable
   4. Onyx ✓
   5. Nova
   6. Shimmer

Enter voice number: 4
✅ Selected voice: Onyx

🎬 Select model quality:
   1. Standard (tts-1)
   2. HD (tts-1-hd) ✓

Enter model number: 2
✅ Selected model: tts-1-hd

⏱️ Select speaking speed:
   3. Normal (1.0x) ✓

Enter speed number: 3
✅ Selected speed: 1.0x

📂 Enter the path to your text file: ./UnitySpeak/unity_intro.txt
🎵 Enter MP3 name: unity_intro_onyx_hd

✅ Audio saved as unity_intro_onyx_hd.mp3
```

#### **Multi-Voice Generation**

**Command:**
```bash
cd ~/eestream/eAudio
python3 eMultiVoiceTTS.py
```

**Workflow:**
1. Select provider mode (OpenAI only / ElevenLabs only / Mixed)
2. Assign voices to each speaker character
3. Configure per-speaker adjustments (speed, tone, etc.)
4. Generate composite audio with proper timing

**Features:**
- Automatic silence insertion between speakers
- Per-speaker voice customization
- Mixed provider support
- Sequential voice assignment

---

### **Phase 4: Quality Review & Iteration**

#### **Audio Testing Checklist**

- [ ] **Pronunciation** - Technical terms clear (kVA, MPTS, THD)
- [ ] **Pacing** - Natural pauses between thoughts
- [ ] **Emphasis** - Key points properly stressed
- [ ] **Transitions** - Smooth speaker handoffs (multi-voice)
- [ ] **Tone** - Matches Unity brand (authoritative, educational)
- [ ] **Length** - Appropriate for content type
- [ ] **Audio Quality** - No clipping, clear speech

#### **Common Adjustments**

**If speech too fast:**
- Reduce speed multiplier (1.0x → 0.95x)
- Add more punctuation pauses in script

**If pronunciation unclear:**
- Adjust acronym spelling in script
- Break compound words with hyphens

**If tone wrong:**
- Try different voice
- Adjust delivery instructions in RECORDING NOTES

**If transitions abrupt (multi-voice):**
- Add blank lines between speakers in script
- Increase inter-speaker silence in generator settings

---

## 📁 Content Organization

### **Directory Structure**

```
eAudio/
├── CompanyIntros/           ← Unity Energy introductions
├── [CustomerName]/          ← Customer-specific content
│   ├── scripts/
│   ├── audio_final/
│   └── audio_drafts/
├── UnitySpeak/              ← Strategic briefings, team updates
├── UnityMemoryThreads/      ← eMemory system explanations
├── UnityINSIGHTS/           ← Educational series
└── EpisodeStory/            ← Narrative content
```

### **File Naming Convention**

**Format:**
```
[ProjectName]_[ContentType]_[VoiceProfile]_[Version].mp3

Examples:
Unity_Energy_Intro_onyx_hd_v2.mp3
FosterFarms_Analysis_graham_std_final.mp3
UnitySpeak_eMemory_Briefing_multi_v1.mp3
```

**Script Files:**
```
[ProjectName]_script_formatted.txt   ← TTS-ready format
[ProjectName]_script_raw.txt         ← Original content
```

---

## 🎓 Best Practices & Lessons Learned

### **Script Writing**

1. **Write for spoken word, not written text**
   - Shorter sentences
   - Natural conversational flow
   - Questions for engagement

2. **Structure for impact**
   - Setup → Solution → Impact
   - Build momentum toward key points
   - Strong opening and closing

3. **Technical precision**
   - Verify all numbers and units
   - Consistent terminology
   - Accurate Maxwell physics references

### **Voice Selection**

1. **Match voice to content purpose**
   - Executive briefings: Authoritative (onyx, deep male)
   - Customer education: Warm, engaging (nova, friendly female)
   - Technical details: Clear, professional (alloy, echo)

2. **Test multiple options**
   - Generate 30-second samples
   - Compare side-by-side
   - Get team feedback

3. **Consider audience**
   - Engineers: Technical, precise voice
   - Executives: Confident, authoritative
   - Customers: Approachable, clear

### **Production Workflow**

1. **Start with script quality**
   - Better script = better audio
   - Format properly from start
   - Review pronunciation before generation

2. **Iterate quickly**
   - Test samples before full generation
   - Adjust script based on audio output
   - Keep version history

3. **Maintain consistency**
   - Same voice for same character across episodes
   - Consistent speed profiles
   - Unified tone across Unity content

---

## 🔧 Technical Implementation

### **API Configuration**

Both TTS tools use centralized configuration:

```python
from eConfig.config_loader import get_openai_api_key, get_elevenlabs_api_key

# APIs automatically loaded from ~/eestream/eConfig/.env
```

**Required Environment Variables:**
```bash
OPENAI_API_KEY=sk-...
ELEVENLABS_API_KEY=...
```

### **Audio Processing (Multi-Voice)**

**Dependencies:**
- `elevenlabs` - ElevenLabs API client
- `openai` - OpenAI API client
- `pydub` - Audio segment manipulation
- `requests` - HTTP requests

**Processing Pipeline:**
1. Parse script → Extract speaker-tagged lines
2. Generate individual clips per line
3. Concatenate with silence insertion
4. Export final composite MP3

---

## 📊 Production Metrics

### **Typical Generation Times**

| Content Type | Duration | OpenAI TTS | OpenAI HD | ElevenLabs |
|--------------|----------|------------|-----------|------------|
| 30-sec intro | ~50 words | 5 sec | 8 sec | 12 sec |
| 3-min briefing | ~450 words | 30 sec | 45 sec | 90 sec |
| 10-min presentation | ~1500 words | 90 sec | 2.5 min | 5 min |

### **Cost Considerations**

**OpenAI TTS:**
- tts-1: $15.00 per 1M characters
- tts-1-hd: $30.00 per 1M characters

**ElevenLabs:**
- Tiered pricing based on subscription
- Higher quality, higher cost per minute

**Recommendation:**
- OpenAI for rapid iteration and testing
- ElevenLabs for final production quality

---

## 🚀 Future Enhancements

### **Planned Improvements**

1. **Automated script formatting**
   - AI-assisted acronym detection
   - Number-to-word conversion
   - Punctuation optimization

2. **Voice library expansion**
   - Custom Unity character voices
   - Regional accent options
   - Emotion/mood presets

3. **Batch processing**
   - Generate multiple versions simultaneously
   - A/B testing automation
   - Parallel voice comparisons

4. **Integration with Notion**
   - Auto-generate audio from Notion docs
   - Embedded playback in dashboards
   - Script versioning and collaboration

---

## 🔗 Related Documentation

- **eaudio_script_format.md** - Complete script formatting standards
- **exchange_system.md** - Content source for Exchange Phase narratives
- **learningConversations.md** - Conversational content methodology
- **productContext.md** - Unity messaging and brand voice

---

## 📝 Quick Reference Commands

**Generate Single-Voice Audio:**
```bash
cd ~/eestream/eAudio
python3 eSingleVoiceTTS.py
```

**Generate Multi-Voice Dialogue:**
```bash
cd ~/eestream/eAudio
python3 eMultiVoiceTTS.py
```

**Test Voice Samples:**
```bash
# Located in eAudio/test_*.mp3
# Compare voice profiles before full production
```

---

**This audio production system enables Unity Energy to create professional, consistent, on-brand voice content at scale. From customer briefings to internal training to strategic communications, eAudio transforms Unity's written intelligence into spoken wisdom.**

---

*Last Updated: December 5, 2025*  
*Maintained by: Maxwellian AI Scribes (Clerk, Cove, Unity)*
