# Transcription and Tool Selection

Use this reference only when the task requires acquiring media, generating a transcript, or configuring a transcription path.

## Decision order

1. Verify that the planned source exposes the **actual teaching content**, not only a syllabus, description, lecture titles, platform comments, or search snippets.
2. Check for official transcript/captions before downloading media.
3. If a faithful text source exists, skip ASR unless the user explicitly wants an ASR comparison.
4. If the course is free but content access requires login, ask the learner to complete the normal login before proceeding; do not substitute outline-based synthesis for inaccessible lectures.
5. If ASR is necessary, inspect existing agent/runtime capabilities before installing anything.
6. Prefer local ASR when privacy, repeated use, or near-zero marginal cost matters and the hardware can run it reasonably.
7. Prefer an existing cloud/file ASR when one-off convenience matters more than local setup, or local hardware is inadequate.
8. If neither path is currently available, propose the smallest setup that fits the user's OS and hardware.

If the learner explicitly asks for a video/lecture summary, a transcript/caption source, permitted ASR, or direct audio/video inspection must cover the lecture speech itself. Do not downgrade the task to summarizing slides or an outline without saying so and obtaining the learner's agreement.

## Automation preference

Interpret "one click" as minimizing repeated learner actions, not literally requiring a graphical button.

If the agent can execute commands and manage files, build the repeatable path itself: accept the course URL/file, obtain permitted sources, perform any required media conversion, run transcription, and pass the resulting text into synthesis. Make first-run dependency/model setup the only exceptional step, subject to the host's permission rules.

If the agent cannot execute locally, recommend the smallest GUI fallback that can ingest the original video directly and export a transcript. Do not make the learner manually extract audio when the chosen tool can accept video.

## Capability selection

Do not depend on a specific vendor. Choose a transcription engine that provides as many of these as the task requires:

- source language and accent/dialect support;
- long-file or chunked long-form transcription;
- timestamps;
- punctuation and inverse text normalization;
- context prompt or hotword support for technical vocabulary;
- speaker separation for multi-speaker lectures;
- local CPU/GPU execution if privacy or cost requires it.

Representative local families include Qwen ASR models and Whisper-compatible runtimes such as Whisper, whisper.cpp, or faster-whisper. These are examples, not mandatory dependencies. If installing or recommending a model, verify its current official documentation, license, hardware requirements, and supported languages rather than relying on version-specific facts stored in this skill.

## Hardware-aware fallback

- Strong compatible GPU: prefer a higher-accuracy local model that fits available memory.
- Modest GPU: prefer a smaller/quantized local model or efficient runtime.
- CPU-only: prefer an efficient CPU runtime and smaller model; warn if a long lecture is likely to take substantial time.
- Restricted machine or mobile-only workflow: prefer an existing file-transcription service or platform transcript rather than forcing local deployment.

Do not make the learner choose model parameters they do not need to understand. Pick a sensible default and expose the tradeoff only when it materially affects speed, cost, or accuracy.

## Media handling

Treat container conversion as an internal step. If the ASR accepts the original video format, send it directly. If it requires audio, use an available media tool such as FFmpeg to extract or resample audio automatically.

Preserve the original file. Write derived audio/transcript to a separate working path when the environment supports files.

For remote sources, prefer official downloadable media. Do not use downloader tooling to bypass access restrictions or source terms.

For Bilibili or another public video platform, first verify that the playlist/source is complete enough for the planned course scope and prefer an official/authorized upload. Public visibility does not itself grant download or reuse rights. Do not use downloader tooling on a clearly unauthorized reupload; resolve a lawful source or use a legitimately obtained user-supplied file instead.

## Transcript quality

Keep a source-language transcript before translation. When accuracy matters:

1. collect course title, lecture title, instructor, topic, and glossary terms as ASR context if the engine supports it;
2. inspect low-confidence or suspicious segments around proper nouns, acronyms, numbers, equations, and code;
3. cross-check suspicious text against slides/notes;
4. preserve timestamps for later verification;
5. never repair uncertain content by inventing what the lecturer "probably" meant.

For STEM material, speech often omits symbols visible on screen. Recover equations and diagrams from official notes/slides or selective key frames rather than reconstructing them solely from ASR.

## Cost behavior

For repeated study, compare marginal cost rather than headline subscription price:

- official transcript: usually no model cost;
- local ASR: one-time setup/model download, near-zero marginal inference cost;
- cloud ASR: minimal setup, usage-based cost;
- LLM synthesis: usually text-only and much cheaper than full audio/video understanding.

Do not quote current prices from memory. If the user is making a cost decision, check the provider's current official pricing.
