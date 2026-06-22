# Workshop

Use this folder for **PlatformCon–style working sessions**. Everything here is **browser + Port** (and optionally Port’s in-product AI). The **[prompt library](./prompts/)** embeds the JSON you paste into Port—**attendees do not need to open any other folder** in this repo.

## Start here

1. **Get a workshop login (no signup).** Open the **[workshop credentials sheet](https://docs.google.com/spreadsheets/d/1U2ywpAVrfdG6H-iTPT0__L26MKdA5o6mqZyzp61CzLk/edit)**. Pick a row that is not yet claimed, **add your name and email** next to it, then **log in to Port** using the **username and password** on that row (and the **Portal URL** if the sheet lists one; otherwise [port.io](https://auth.getport.io/u/login/)).
2. Open the **[prompt library](./prompts/README.md)** on **GitHub** (or clone this repo if you prefer). Steps **1–3** include **ready-to-copy JSON** for imports; step **4** adds a Port **skill** that triggers the **`request_cloud_resource`** workflow from **Port AI chat**.
3. For each step, optionally **paste the whole prompt file** into **Port AI** so it can guide you while you use Builder / Self-Service / Workflows.

**Port AI only sees what you paste into chat.** The prompt files carry the **payloads** so new users are not expected to hunt for loose JSON elsewhere.


## What you will build

| Step | Focus |
|------|--------|
| 0 | Portal title / branding |
| 1 | Catalog — blueprints + sample services |
| 2 | Self-service action (the request form) |
| 3 | AI workflow (import JSON; workflows may be beta in your org) |
| 4 | Port **`skill`** → ask Port AI to request a resource (triggers **`request_cloud_resource`**) |

Scenario and personas: [../company-context.md](../company-context.md).

## Facilitators

See **[FACILITATOR.md](./FACILITATOR.md)** for pre-provisioned Portals, attendee seating, known product friction (onboarding, beta), and how to regenerate prompts after editing **`.cursor/skills/platformcon-workshop/assets/`**.
