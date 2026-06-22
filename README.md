# PlatformCon Workshop — From IDP to AEP

**~1 hour · Port + Port AI · in your browser**

Build a self-service cloud resource platform live: catalog → form → AI workflow → request a resource from Port AI.

---

## Start here

### 1. Log in to Port (no signup)

Use a **pre-provisioned login** from the facilitator’s sheet — do **not** create your own Port account.

**[Workshop credentials (Google Sheet)](https://docs.google.com/spreadsheets/d/1U2ywpAVrfdG6H-iTPT0__L26MKdA5o6mqZyzp61CzLk/edit)**

1. Pick a row that is not yet claimed.
2. Add **your name and email** in that row.
3. Log in with that row’s **username and password** ([port.io](https://auth.getport.io/u/login/) or the **Portal URL** on the sheet if one is listed).

### 2. Follow the steps below (in order)

Open each link on GitHub. Steps **1–4** include JSON you copy into Port’s import UI. You can **paste the whole step file into Port AI** if you want a coach while you work.

**You do not need to clone this repo or install anything.**

### 3. Optional: use Port AI as a coach

Port AI only sees what you paste into chat. Each step file already contains the JSON and instructions.

---

## Workshop steps

| Step | What you'll do | Open |
|------|----------------|------|
| 0 | Set portal title / branding | [00-portal-branding.md](./workshop/prompts/00-portal-branding.md) |
| 1 | Import catalog blueprints + sample services | [01-catalog-and-sample-data.md](./workshop/prompts/01-catalog-and-sample-data.md) |
| 2 | Import the self-service request form | [02-self-service-action.md](./workshop/prompts/02-self-service-action.md) |
| 3 | Import the AI workflow (workflows may be beta in your org) | [03-ai-workflow.md](./workshop/prompts/03-ai-workflow.md) |
| 4 | Add a Port **skill**, then ask Port AI to **request a resource** | [04-call-workflow-with-skill.md](./workshop/prompts/04-call-workflow-with-skill.md) |

**Step 3 tip:** If Port AI hits a length limit, paste only the **workflow JSON** from the big code box into Port’s import field, and send the instruction paragraphs at the top in a separate message.

**Step 4 tip:** After creating the skill entity, ask Port AI something like: *“Request a cloud resource for the PlatformCon-Carne workshop.”*

---

## What you'll have at the end

When a developer needs a cloud resource:

1. They fill in a simple form — service, environment, resource type.
2. Port fetches context about their service.
3. AI generates an implementation plan and architecture diagram.
4. Non-production requests auto-approve; production goes through approval (e.g. Slack).
5. Everything is tracked in the catalog.

Background story: [company-context.md](./company-context.md)

---

## Facilitators

[workshop/FACILITATOR.md](./workshop/FACILITATOR.md) — pre-provisioned Portals, seating, beta workflows, keeping prompts in sync.

---

## Learn more

- [Port documentation](https://docs.getport.io)
- [Port skills](https://docs.port.io/ai-interfaces/skills/)
- [AI agents in Port](https://docs.getport.io/ai-interfaces/ai-agents/overview)

Built with 🥩 for PlatformCon
