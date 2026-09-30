# Scripts

Small programs that do the project's repetitive work. Each script does one job.

| Script | Job | Status |
|---|---|---|
| `compute_wer.py` | Compare what was said with what ASR wrote and count word errors | Ready |
| `run_whisper.py` | Transcribe recordings with Whisper | Planned |
| `run_gemini_transcribe.py` | Transcribe recordings with Gemini 3.5 Transcribe (with and without custom vocabulary) | Planned |
| `webspeech_recorder.html` | Browser page that records audio and captures Web Speech API text at the same time | Planned |
| `label_impact.py` | Label each error as None, Minimal, or Significant clinical impact | Planned |

## Try the ready script

```bash
python scripts/compute_wer.py "Um, it starts with B, like boy." "Uh, it starts with B, like boy."
# WER: 14.29%  (harmless filler change)

python scripts/compute_wer.py "It starts with B, like boy." "It starts with P, like boy."
# WER: 16.67%  (wrong first sound: clinically significant)
```

Almost the same WER, very different clinical impact. That gap is what this project measures.
