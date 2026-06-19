# Workshop (live session path)

Use this folder for **PlatformCon–style working sessions** where attendees may not have Cursor. Everything here is **browser + Port** (and optionally Port’s in-product AI), plus JSON assets already in this repo.

## Start here

1. **Log in** to the Port organization your facilitator assigned (see [FACILITATOR.md](./FACILITATOR.md) if you are running the session).
2. Open the **[prompt library](./prompts/README.md)** on **GitHub** (or clone this repo if you prefer). Steps **1–4** include **ready-to-copy JSON** in the page—paste it into Port’s import dialogs; you do not need to hunt separate files.
3. For each step, optionally **paste the whole prompt file** into **Port AI** so it can guide you while you use Builder / Self-Service / Workflows.

**Port AI only sees what you paste into chat.** The prompt files carry the **payloads** so new users are not expected to upload loose JSON from disk.

You do **not** need Cursor or the Port MCP to complete the workshop using this path.

## What you will build

| Step | Focus |
|------|--------|
| 0 | Portal title / branding |
| 1 | Catalog — blueprints + sample services |
| 2 | Self-service action (the request form) |
| 3 | AI workflow (import JSON; workflows may be beta in your org) |
| 4 | Run through staging + production demo scenarios |

Scenario and personas: [../company-context.md](../company-context.md).

## Facilitators

See **[FACILITATOR.md](./FACILITATOR.md)** for pre-provisioned Portals, attendee seating, and known product friction (onboarding, beta).

## Optional: Cursor + MCP

If you **do** use Cursor with Port MCP, the agent skill at [`.cursor/skills/platformcon-workshop/SKILL.md`](../.cursor/skills/platformcon-workshop/SKILL.md) automates the same steps. That path is optional and aimed at facilitators or attendees who already use Cursor.
