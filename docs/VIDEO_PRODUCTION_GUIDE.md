# Tribit H4H: 30-Second Demo Video Production Guide

## Goal
Produce a polished 30-second, 16:9 (1920×1080) narrated product demo showing how Tribit H4H helps Habitat for Humanity project managers prepare city permit applications. Show the actual working interface where possible. Do not depict hypothetical capabilities as live features.

**Audience:** Habitat project managers, municipal permitting partners, and implementation stakeholders.
**Core message:** Upload what you already have. Tribit identifies the city-specific application steps, pre-fills supported fields, and makes missing documents and deadlines visible.

## Approved 30-second voiceover script (approximately 65 words)
> “Permitting shouldn't start with a blank form. With Tribit, Habitat project managers upload the documents they already have. The workspace organizes project details and helps pre-fill application fields. Choose a city to see its permit requirements, what’s complete, and what’s still missing. Follow the city’s submission stages and upcoming deadlines, all in one place. Tribit helps teams move from paperwork to a submission-ready packet.”

Record at a natural, clear pace; trim pauses rather than speeding up words. Avoid promising automatic approvals or guaranteed submission readiness.

## Shot-by-shot storyboard

| Time | Visual | Overlay |
| --- | --- | --- |
| 0–4s | Start on project intake screen; zoom to document upload | “Start with what you have” |
| 4–9s | Upload sample plans and existing project files; show extracted fields where implemented | “Upload → review → pre-fill” |
| 9–14s | Show city dropdown, select Westminster, and reveal city-specific checklist | “Requirements by city” |
| 14–20s | Show user-completed items with green checks and remaining items as pending | “Know what’s done and missing” |
| 20–26s | Show municipality-defined submission stages and document deadlines (only if implemented; otherwise clearly label as concept) | “See each submission stage” |
| 26–30s | End on clean Tribit dashboard with logo and URL | “Tribit H4H • A clearer path to permits” |

Green checkmarks indicate **user completion**, not municipal approval. City submission stages are based on the city's application process, not generic project phases. Any example dates or forms must be visibly marked “Illustrative” unless verified against the relevant city's current instructions.

## How to produce with Claude

1. Open the deployed Tribit H4H demo and record the workflow in a browser at 1920×1080. Use synthetic project data and dummy documents. Do not expose API keys, personal details, or real applicant records.
2. Give Claude this guide, the screen recording, and screenshots of the current interface. Ask it to reconcile the storyboard with what the app **actually does today**, and flag features that need a mockup or a “Concept preview” label.
3. Have Claude write the final narration, six shot captions, and a precise edit decision list with timecodes. Ask for a word count and a read-through estimate.
4. Capture each shot with a clean cursor path. Prefer real UI recordings. Use still screenshots with slow crops only where necessary. Avoid invented UI screens presented as product footage.
5. Assemble in a video editor (e.g. CapCut, Descript, Premiere, or Canva). Claude supplies the script and editing plan; it does not by itself export a finished video unless a connected video-generation/editing capability is available.
6. Add voiceover, captions, subtle transitions, and royalty-cleared or original background audio. Keep background music quieter than speech.
7. Export H.264 MP4, 1920×1080, 30 fps, approximately 30 seconds. Review on mobile and desktop.

## Copy-paste Claude production prompt

```text
You are the creative director and editor for a 30-second Tribit H4H product demo.

Audience: Habitat for Humanity project managers and city permitting partners.
Goal: Demonstrate the actual turnkey workflow, not an abstract AI pitch.
Use the attached current app screenshots/recording and this VIDEO_PRODUCTION_GUIDE.md as source material.

Deliver:
1. A 30-second narration script with exact estimated duration and word count.
2. A six-shot edit decision list with start/end timestamps, real UI actions, crop/zoom notes, and on-screen text.
3. A subtitle file in SRT format.
4. An editor-ready assembly checklist and a final quality-control checklist.
5. A list of any shots that are not currently supported by the live application, with safer alternatives or clear “Concept preview” labels.

Show: upfront document upload, extraction/pre-fill when actually available, city selection (Westminster example), municipality-specific checklist, green user-completion checks, missing documents, and city-defined submission stages/deadlines.

Do not imply that a green check is city approval. Do not invent permit requirements, filing dates, automation, or working screens. Do not show sensitive documents or credentials. Use a calm, practical tone. End with the Tribit H4H name and live demo URL.
```

## Suggested asset list

- `video/assets/intake.png` — intake and document upload
- `video/assets/prefill.png` — extracted project details (if working)
- `video/assets/city-checklist.png` — Westminster city selection and checklist
- `video/assets/completion.png` — user completion indicators
- `video/assets/stages.png` — municipal filing stages/deadlines
- `video/assets/end-card.png` — branded end card
- `video/tribit-h4h-demo-30s.mp4` — final exported video

These are suggested output paths, not a claim that assets already exist.

## Acceptance checklist

- Runtime is 28–32 seconds; narration fits without rushing.
- Every shown interaction matches the deployed demo, or is explicitly labeled a concept.
- User completion and municipal approval are never conflated.
- City-specific rules and dates are checked before being shown as factual.
- No secrets, applicant PII, or confidential plans appear.
- Captions remain readable at mobile size; final URL is visible for at least two seconds.
- Video makes the workflow understandable with the sound muted.

**Demo:** https://ritwikntrehan.github.io/Tribit-H4H-claude/  
**API:** https://tribit-h4h-api.onrender.com (not a user-facing video destination)
