# ClearCue: Clinically-Aware Speech Recognition for the VOICE AI Virtual Patient

**CS 7980 Research Capstone · Northeastern University · Fall 2026**

| | |
|---|---|
| **Student** | Akash Chandru (chandrasekharantha.a@northeastern.edu) |
| **Project PI** | Ilmi Yoon |
| **Course Professor** | Tehmina Amjad |

---

## What this project is about

[VOICE](#related-work) is an AI virtual patient that speech-language pathology (SLP) students talk to out loud. VOICE turns each student's speech into text with automatic speech recognition (ASR), and the AI patient responds to that text.

When ASR mishears a student, the patient responds to words the student never said. For example, a phonemic cue like *"It starts with B, like boy"* heard as *"It starts with P"* gives the patient the wrong first sound.

The usual way to measure ASR is **word error rate (WER)**, which counts wrong words. But WER treats every wrong word the same, so it can't tell a harmless error from one that changes clinical meaning.

**This project asks:**
1. Which ASR errors in VOICE-style clinical speech actually change the clinical meaning of what students say?
2. Can newer ASR tools reduce those errors compared with VOICE's current setup?

## Systems compared

| System | Role |
|---|---|
| Web Speech API (browser) | Current VOICE baseline |
| OpenAI Whisper | Open-source comparison |
| Google Gemini 3.5 Transcribe | Newer model, including custom vocabulary biasing |

## Approach

1. **Build a test corpus** of VOICE-style clinical phrases (prompts and Semantic → Phonemic → Model cues), recorded by consenting speakers with different accents.
2. **Transcribe** every recording with each system.
3. **Measure** WER for each system.
4. **Label clinical impact** of each error as None, Minimal, or Significant, following Ellis et al. (2026), with SLP faculty validating a subset.
5. **Test improvements** such as custom vocabulary, then compare accuracy, clinical impact, latency, and cost.

The full plan is in [`docs/Project_Charter_Akash_Chandru_ClearCue.docx`](docs/Project_Charter_Akash_Chandru_ClearCue.docx).

## Repository structure

```
clearcue-cs7980/
├── README.md          ← this file
├── docs/              ← project charter, weekly reports, slides, final report
├── corpus/            ← test phrases (recordings are kept out of the repo)
├── scripts/           ← code to run ASR systems and compute errors
├── results/           ← comparison tables, charts, and error examples
├── requirements.txt   ← Python packages
├── .env.example       ← template for API keys (copy to .env, never commit .env)
└── .gitignore         ← files that must never be committed
```

## Getting started

```bash
git clone <this-repo-url>
cd clearcue-cs7980
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # then add your own API keys to .env
```

Quick test of the WER script:

```bash
python scripts/compute_wer.py "it starts with b like boy" "it starts with p like boy"
```

## Deliverables

| # | Deliverable | Location | Status |
|---|---|---|---|
| 1 | Clinical ASR test corpus | `corpus/` | In progress |
| 2 | Clinical-impact evaluation toolkit | `scripts/` | Planned |
| 3 | ASR benchmark and recommendation report | `results/`, `docs/` | Planned |
| 4 | Prototype integration (stretch goal) | Separate sandbox | Planned |

## Schedule

| Phase | Dates | Focus |
|---|---|---|
| Team, review, scope | Sep 14 – Sep 28 | Join VOICE team, choose topic |
| Charter and kick-off | Sep 28 – Oct 5 | Project charter, repo setup |
| Define | Oct 5 – Oct 16 | Review prior VOICE ASR work, design corpus |
| Measure | Oct 12 – Oct 30 | Record corpus, run all systems, compute WER |
| Analyze | Oct 26 – Nov 13 | Clinical-impact labeling, speaker comparison |
| Improve | Nov 9 – Nov 25 | Custom vocabulary tests, sandbox prototype |
| Control | Nov 23 – Dec 4 | Re-test, latency and cost check, documentation |
| Close out | Dec 1 – Dec 11 | Final report and presentation |

## Progress log

- **Week 7 (Sep 21):** Joined the VOICE team; attended first research meeting.
- **Week 8 (Sep 28):** Presented research interests; drafted project charter; created this repo.

## Data and privacy rules

- **No API keys in the repo.** Keys live only in `.env`, which is ignored by git.
- **No audio recordings in the repo** unless the speaker has agreed and the PI has approved.
- **No VOICE production code or data** is copied here. VOICE is referenced, not included.
- **No data from students in courses or from people with aphasia** is collected in this project.

## Related work

- Hu, Y., et al. (2026). "A Safe First Step": Design and evaluation of an emotionally expressive AI virtual patient for clinical simulation in speech-language pathology training. Research Square. https://doi.org/10.21203/rs.3.rs-8588902/v1
- Ellis, Z., et al. (2026). WER is unaware: Assessing how ASR errors distort clinical understanding in patient facing dialogue. IWSDS 2026. arXiv:2511.16544
- Radford, A., et al. (2023). Robust speech recognition via large-scale weak supervision (Whisper). ICML 2023.
- Google (2026). Gemini 3.5 Transcribe model documentation. https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe

The full reference list is in the project charter.
