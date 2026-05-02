# PDF Summarizer with Claude

Summarize any PDF in 5 lines using the Claude API. A 30-line Python script — my first AI build, exploring what production AI feels like beyond the Claude.ai interface.

## Demo

![PDF Summarizer Demo](docs/screenshot.png)

## What it does

```bash
python summarise.py yourfile.pdf
```

Reads a PDF, extracts the text, sends it to Claude with a tight summarization prompt, prints a 5-line summary.

## Why I built it

I'd been building agentic copilots for Fortune-500 clients — but always with engineers handling the LLM plumbing. I wanted to feel the friction myself: context windows, token limits, prompt design, the gap between Claude.ai (which feels magical) and the API (which feels like real work).

This is the simplest possible "RAG" pattern — stuffed prompt over a single document — that taught me the foundations before scaling up.

## Quick start

1. Clone this repo
2. Install dependencies:
```bash
   pip install anthropic pypdf python-dotenv
```
3. Create a `.env` file in the project root:

Set your `ANTHROPIC_API_KEY` in the script before running.

4. Run:
```bash
   python summarise.py yourfile.pdf
```

## How it works

1. Reads PDF using `pypdf`
2. Extracts and concatenates text from all pages
3. Truncates to 8000 chars (context window safety)
4. Sends to Claude with instruction "Summarize this in exactly 5 lines"
5. Prints the response

## Design choices

- **8000-char input cap** — stays inside Claude's context window. Production RAG would chunk and retrieve instead of stuffing.
- **`max_tokens=300`** — caps output cost without truncating useful summaries.
- **"Exactly 5 lines"** — prompt specificity matters; tighter than "summarize."

## Tech stack

Python 3.11 · Anthropic SDK · pypdf · python-dotenv

## What I learned

- Why "exactly 5 lines" produces tighter output than "summarize"
- Why production RAG chunks documents instead of stuffing the context window
- The real difference between using Claude.ai and shipping with the API

## What's next

- **Q&A version** ([pdf-qa-claude](https://github.com/AdarshShrivastava1102/pdf-qa-claude)) — extends summarization to multi-turn document Q&A
- Add chunking + embeddings for documents larger than 8000 chars
- Build evaluation harness to test summary quality systematically

## Author
Adarsh Shrivastava — [LinkedIn](https://linkedin.com/in/adarsh-p110293) · [GitHub](https://github.com/AdarshShrivastava1102)
