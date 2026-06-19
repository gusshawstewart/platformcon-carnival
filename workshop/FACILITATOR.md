# Facilitator notes — live workshop

You said you will **create pre-provisioned Port organizations separately**. This doc is the checklist and framing so the repo matches how you run the room.

## Pre-provisioned Portals (your responsibility)

Suggested pattern:

- **Pool** of N disposable Port orgs (or seats), each already past first-time setup where possible.
- **One row per seat** in a shared tracker (Google Sheet or internal doc). Example columns:
  - **Portal / app URL** (e.g. `https://app.getport.io` vs EU)
  - **Login identifier** (email or username Port expects)
  - **Temporary password** or **invite link** (prefer invites if your IT policy allows)
  - **Claimed by** (attendee name — empty until they pick a row)
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
- Keep the **import fallback** front and center: [../step-3-ai-workflow/workflow.json](../step-3-ai-workflow/workflow.json) via **Settings → Workflows → Import** (wording may vary slightly by Port version).

## Onboarding (“Vibe build” and similar)

New signups may hit **mandatory first-run product tours**. Mitigations:

- **Pre-provision** logins that have already completed onboarding, **or** arrive early to walk the first screen with volunteers.
- **Preread** (email or Slack 24h before): “Use row 12 in the sheet; open this repo; we start at step 0.”
- **Two-track timing**: first 10 minutes = “get into your portal”; then sync at step 1.

## Slack and secrets

The workflow JSON references **Slack** placeholders (`SLACK_BOT_TOKEN`, `SLACK_PLATFORM_CHANNEL`). For a minimal hands-on:

- Either configure those secrets in each pooled org, **or**
- Tell attendees **Slack nodes may fail** until secrets exist — catalog + form + most steps still land.

## Primary attendee path

Point the room at **[workshop/README.md](./README.md)** and the **[prompts](./prompts/README.md)** — not Cursor — unless someone explicitly wants the MCP skill.

## Keeping workshop prompts in sync

The files `workshop/prompts/01`–`04` **embed** the same JSON as `step-*` / `sample-data/`. From repo root:

1. After you edit JSON under `step-*` / `sample-data/`, run **`python3 workshop/scripts/sync-prompt-embeds.py`** so the prompt files pick up the changes.

2. To align `step-3-ai-workflow/workflow.json` with a typical **Port UI export** (null trigger titles, `api.port.io` on the catalog fetch, `category`, `links` / `verbose` on nodes, Slack `body` key order, `slack_hitl_gate_stopped` after `open_pr`, etc.), run **`python3 workshop/scripts/apply_port_export_shape.py`**, then run **`sync-prompt-embeds.py`** again.
