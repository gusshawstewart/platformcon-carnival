# Prompt library (Port AI)

Use these files **in order** during the workshop.

**Before step 0:** claim a row and log in from the **[workshop credentials sheet](https://docs.google.com/spreadsheets/d/1U2ywpAVrfdG6H-iTPT0__L26MKdA5o6mqZyzp61CzLk/edit)** (add your name and email; use that row’s username and password). **No Port signup** for this workshop unless your facilitator says otherwise.

## For attendees (new Port users)

Steps **1–3** embed **full JSON** inside the markdown. Step **4** adds the Port **`skill` blueprint**, a skill entity that **triggers `request_cloud_resource`**, and a **Port AI chat** example to run it.

- Open this file on **GitHub** (raw or rendered). For each step with JSON, **select everything inside that step’s code box**, copy, and paste into Port’s **Import** UI, **or**
- **Paste the whole `.md` file** into Port AI so the model sees the same JSON and can coach you while you paste into Port.

Step **3** is a large workflow. If Port AI hits a length limit, paste **only the workflow JSON** from the big code box in `03-ai-workflow.md` into **Port’s** import field, and send Port AI the instruction paragraphs at the top of that file in a separate, shorter message.

You do **not** need a local Git clone for the copy-paste path—GitHub in the browser is enough.

Step **0** is short text only (no JSON).

**Step 4:** Import the **`skill` blueprint**, create the **`platformcon-carne-request-resource`** skill entity, then ask **Port AI** to request a cloud resource — the skill calls workflow **`request_cloud_resource`** for you.

## Order

| Step | File |
|------|------|
| 0 | [00-portal-branding.md](./00-portal-branding.md) |
| 1 | [01-catalog-and-sample-data.md](./01-catalog-and-sample-data.md) |
| 2 | [02-self-service-action.md](./02-self-service-action.md) |
| 3 | [03-ai-workflow.md](./03-ai-workflow.md) |
| 4 | [04-demo-verification.md](./04-demo-verification.md) — **`skill` blueprint** + skill that triggers **`request_cloud_resource`** |

## For maintainers

After editing JSON under **`.cursor/skills/platformcon-workshop/assets/`**, regenerate embedded prompts from the repo root:

```bash
python3 workshop/scripts/sync-prompt-embeds.py
```
