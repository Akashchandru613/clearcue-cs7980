# Corpus: test phrases

`test_phrases.csv` is the list of phrases speakers will read aloud to test each ASR system.
Think of it as flashcards for the "listening robots."

**Status: DRAFT.** Review this list with the VOICE team and SLP faculty before recording.

## Columns

| Column | Meaning |
|---|---|
| `id` | Phrase ID (P01, P02, ...) |
| `section` | VOICE assessment task: object_naming, word_fluency, sentence_completion, responsive_speech, or general |
| `utterance_type` | assessment_prompt, semantic_cue, phonemic_cue, model_cue, supportive, instruction, or clarification |
| `target` | The word the patient is supposed to produce (blank if none) |
| `text` | The exact words the speaker should say (this is the reference transcript) |

## Notes

- Object naming targets (book, ball, knife, cup, safety pin) and the Book cue wording follow the VOICE
  Object Naming task shown in the team's IUI 2027 submission (Fig. 2). Other cues are drafts.
- Phonemic cues matter most for this project: a single misheard letter can change their clinical meaning.

## Recordings

Recordings go in `corpus/recordings/`, which is listed in `.gitignore` so audio is never uploaded.
Only record speakers who have agreed, and follow the PI's guidance on storing audio.
Suggested file naming: `S01_P03.wav` (speaker 01, phrase P03).
