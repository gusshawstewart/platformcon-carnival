# Facilitator notes — live workshop

You said you will **create pre-provisioned Port organizations separately**. This doc is the checklist and framing so the repo matches how you run the room.

## Pre-provisioned Portals (your responsibility)

**Attendee-facing sheet (this workshop):** **[Workshop credentials](https://docs.google.com/spreadsheets/d/1U2ywpAVrfdG6H-iTPT0__L26MKdA5o6mqZyzp61CzLk/edit)** — each row has **username / password** (and usually **Portal URL**). Attendees **claim a row** by adding **name and email**, then log in with that row’s credentials. **They must not sign up for Port** for this session unless you explicitly run a different format. You can keep the sheet **restricted until event day**; unlock it when the room needs access.

Suggested pattern for the sheet (adjust column headers to match yours):

- **Pool** of N disposable Port orgs (or seats), each already past first-time setup where possible.
- **One row per seat** in the shared tracker. Example columns:
  - **Portal / app URL** (e.g. `https://app.getport.io` vs EU)
  - **Login identifier** (email or username Port expects)
  - **Temporary password** or **invite link** (prefer invites if your IT policy allows)
  - **Claimed by / name** and **email** (empty until they pick a row)
  - **Region** (US vs EU MCP / API if relevant)
  - **Notes** (e.g. “workflows beta enabled”, “Slack secrets not configured”)

**Hygiene**

- Treat credentials as **throwaway**; rotate or disable after the event.
- Add **~20–30% extra rows** so latecomers and broken rows do not stall the room.
- Brief rule: **one row per person or pair**; no sharing a row across tables if you want predictable workflow runs.

## Why not pre-list every attendee?

You do not need legal names in advance if **rows are anonymous until claimed**. The sheet is the seating chart at event time.

## Workflows beta

If workflows are **beta-gated** in some orgs:

- Confirm each **pooled org** has workflows (or the same beta flag) **before** the session.
- Keep the **import fallback** front and center: [.cursor/skills/platformcon-workshop/assets/step-3-ai-workflow/workflow.json](../.cursor/skills/platformcon-workshop/assets/step-3-ai-workflow/workflow.json) via **Settings → Workflows → Import** (wording may vary slightly by Port version).

## Onboarding (“Vibe build” and similar)

New signups may hit **mandatory first-run product tours**. Mitigations:

- **Pre-provision** logins that have already completed onboarding, **or** arrive early to walk the first screen with volunteers.
- **Preread** (email or Slack 24h before): “Use row 12 in the sheet; open this repo; we start at step 0.”
- **Two-track timing**: first 10 minutes = “get into your portal”; then sync at step 1.

## Slack and secrets

The workflow JSON references **Slack** placeholders (`SLACK_BOT_TOKEN`, `SLACK_PLATFORM_CHANNEL`) and Port API credentials (`PORT_CLIENT_ID`, `PORT_CLIENT_SECRET`) for the catalog fetch step. For a minimal hands-on:

- Either configure those secrets in each pooled org, **or**
- Tell attendees **Slack nodes may fail** until secrets exist — catalog + form + most steps still land. **`fetch_service_context`** needs **`PORT_CLIENT_ID`** and **`PORT_CLIENT_SECRET`**; the workflow’s **`get_port_token`** node exchanges them for a JWT before calling the Port API.

## Keeping workshop prompts in sync

The files `workshop/prompts/01`–`04` **embed** JSON from **`.cursor/skills/platformcon-workshop/assets/`**. Step **4** regenerates **`skill-entity.json`** from **`assets/step-4-port-skill/platformcon-carne-request-resource/SKILL.md`**. From repo root:

1. After you edit JSON under **assets** (or edit **`SKILL.md`** for the demo skill), run **`python3 workshop/scripts/sync-prompt-embeds.py`** so prompts and **`skill-entity.json`** stay in sync.

2. To align `.cursor/skills/platformcon-workshop/assets/step-3-ai-workflow/workflow.json` with a typical **Port UI export** (null trigger titles, `api.port.io` on the catalog fetch, `category`, `links` / `verbose` on nodes, Slack `body` key order, `slack_hitl_gate_stopped` after `open_pr`, etc.), run **`python3 workshop/scripts/apply_port_export_shape.py`**, then run **`sync-prompt-embeds.py`** again.

## Primary attendee path

Point the room at the **[main workshop guide](../README.md)** — not Cursor — unless someone explicitly wants the MCP skill.

**Step 4 note:** Attendees create the **`skill` blueprint** themselves unless their pooled org already has one (some orgs ship it by default). If **`skill` already exists**, they skip blueprint import and only create the skill entity.
