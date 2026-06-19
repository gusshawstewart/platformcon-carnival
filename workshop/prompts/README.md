# Prompt library (Port AI)

Use these files **in order** during the workshop.

## For attendees (new Port users)

Steps **1–4** embed **full JSON** inside the markdown. You can:

- Open this file on **GitHub** (raw or rendered), **select the JSON inside the fenced block**, copy, and paste into Port’s **Import** UI, **or**
- **Paste the whole `.md` file** into Port AI so the model sees the same JSON and can coach you while you paste into Port.

Step **3** is a large workflow. If Port AI hits a length limit, paste **only** the workflow JSON (between the five-backtick delimiter lines) into **Port’s** import box, and send Port AI the **instruction text** at the top of `03-ai-workflow.md` in a separate, shorter message.

You do **not** need a local Git clone for the copy-paste path—GitHub in the browser is enough.

Step **0** is short text only (no JSON).

## Order

| Step | File |
|------|------|
| 0 | [00-portal-branding.md](./00-portal-branding.md) |
| 1 | [01-catalog-and-sample-data.md](./01-catalog-and-sample-data.md) |
| 2 | [02-self-service-action.md](./02-self-service-action.md) |
| 3 | [03-ai-workflow.md](./03-ai-workflow.md) |
| 4 | [04-demo-verification.md](./04-demo-verification.md) |

## For maintainers

After editing JSON under `step-*` or `sample-data/`, regenerate embedded prompts from the repo root:

```bash
python3 workshop/scripts/sync-prompt-embeds.py
```
