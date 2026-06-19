#!/usr/bin/env python3
"""Regenerate workshop/prompts/01–04 with JSON embedded from step-* assets (single source of truth)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROMPTS = ROOT / "workshop" / "prompts"


def fence(n: int = 3) -> str:
    return "`" * n


def main() -> None:
    s1 = (ROOT / "step-1-catalog-foundation/service.json").read_text().strip()
    s2 = (ROOT / "step-1-catalog-foundation/cloud_resource_request.json").read_text().strip()
    s3 = (ROOT / "step-1-catalog-foundation/cloudResource.json").read_text().strip()
    services = (ROOT / "sample-data/services.json").read_text().strip()

    md01 = f'''You are helping me build the **catalog foundation** for the PlatformCon-Carne workshop in Port.

**Who this is for:** New Port users. You (Port AI) only see this chat. The JSON below is **included so I can copy it** into Port without hunting files on disk.

**What I will do in Port:** Use **Builder → Blueprints → Import** (or paste JSON), then create **service** entities from the sample list. If my Port version only has a visual blueprint editor, walk me field-by-field to match the JSON **exactly** (same property identifiers and enums).

---

## 1 — Blueprint `service`

**In Port:** Import this as one blueprint (identifier must stay `service`).

{fence(3)}json
{s1}
{fence(3)}

---

## 2 — Blueprint `cloud_resource_request`

{fence(3)}json
{s2}
{fence(3)}

---

## 3 — Blueprint `cloudResource`

{fence(3)}json
{s3}
{fence(3)}

---

## 4 — Sample `service` entities

Create **six** entities on blueprint `service`. If Port has **bulk import / JSON paste**, use this array. Otherwise create each row manually using the same identifiers and properties.

{fence(3)}json
{services}
{fence(3)}

**Done when:** All three blueprints exist and all six services (`payments-service`, `order-management`, `menu-catalog`, `delivery-tracking`, `user-profiles`, `notification-service`) appear in the catalog.

**If something fails:** Explain the Port error in plain language and what to change (usually a typo in an identifier or a relation target).
'''
    (PROMPTS / "01-catalog-and-sample-data.md").write_text(md01)

    w2 = (ROOT / "step-2-self-service-action/workflow.json").read_text().strip()
    md02 = f'''You are helping me create the **self-service action** for the PlatformCon-Carne workshop in Port.

**Who this is for:** New Port users. Copy the JSON below and paste it into **Settings → Self-service → Actions → Import** (wording may vary). You do not have my disk; everything needed is **in this message**.

**Goal:** Action **Create a new resource** appears under Self-Service. Form: infrastructure type, resource types (cloud vs on-prem), environment, **service** entity picker (`service` blueprint), additional context.

---

## Action + trigger JSON (copy all of this)

{fence(3)}json
{w2}
{fence(3)}

**After import, check:** Cloud vs On-Premise toggles resource type options; **Service** is an entity field on blueprint `service`; environments include Development / Staging / Production.

**Done when:** I can open Self-Service and the form loads with no error.
'''
    (PROMPTS / "02-self-service-action.md").write_text(md02)

    w3 = (ROOT / "step-3-ai-workflow/workflow.json").read_text().strip()
    n = 5
    md03 = f'''You are helping me install the **AI workflow** for the PlatformCon-Carne workshop in Port.

**Who this is for:** New Port users. The workflow JSON is **in this message**. Paste **only the JSON** (see “How to copy” below) into **Settings → Workflows → Import** (or your Port version’s equivalent). You do not need files from disk.

**Goal:** Workflow identifier `request_cloud_resource` is **published** and wired to the same self-service action from the previous step. Submitting the form should start a run.

**Notes:**
- **Workflows may be beta** — if import is disabled, say what to ask an admin.
- **INPUT node** `human_gate_before_plan`: after service context loads, someone must click **Proceed with AI plan** or **Stop run** before AI runs.
- **Slack** nodes need secrets `SLACK_BOT_TOKEN` and `SLACK_PLATFORM_CHANNEL` to succeed; other steps may still run.
- Webhooks use `api.getport.io`; EU tenants may need URL updates per facilitator.

**After import:** Tell me where to open the **run timeline** and what **waiting for input** looks like for the INPUT step.

---

## Full workflow JSON

**How to copy:** The block below is wrapped in lines of **five** backtick characters so the workflow text can contain normal Markdown code fences. Copy **only** the JSON—everything **after** the first delimiter line and **before** the final delimiter line (do not include the backtick lines themselves).

{fence(n)}
{w3}
{fence(n)}
'''
    (PROMPTS / "03-ai-workflow.md").write_text(md03)

    backup = (ROOT / "step-4-demo-flow/backup-entity.json").read_text().strip()
    md04 = f'''You are helping me **verify** the PlatformCon-Carne workshop in Port.

**Who this is for:** New Port users. You only see this chat—I run everything in the Port UI.

**Prerequisites:** Steps 0–3 done (branding, three blueprints + services, action, workflow).

---

### A — Staging path

1. **Self-Service** → **Create a new resource**.
2. **Cloud** · **RDS Database** · **Staging** · **payments-service** · Additional requirements: `Standard configuration with automated backups enabled`.
3. Submit → open the **workflow run**.
4. If paused on **Confirm AI plan generation (HITL preview)** → **Provide inputs** → **Proceed with AI plan**.
5. Confirm a `cloud_resource_request` exists with **implementation plan** and **architecture** filled in.

### B — Production path

Same as A but **Environment: Production**. Confirm the run hits the production branch (Slack only works if secrets exist).

### C — Backup entity (optional)

If the facilitator wants a **static** request without waiting for AI, import this entity on blueprint `cloud_resource_request` (import / API / UI—whatever my Port exposes). Copy **only** the JSON between the two delimiter lines of **five** backticks (do not paste the backtick lines themselves).

{fence(n)}
{backup}
{fence(n)}

**Done when:** I have seen staging behavior and production branch behavior (or the facilitator signs off).

Optional talk track: I can open `step-4-demo-flow/README.md` in the workshop repo if I have it—otherwise ignore.
'''
    (PROMPTS / "04-demo-verification.md").write_text(md04)
    print("Updated workshop/prompts/01–04 from step-* JSON files.")


if __name__ == "__main__":
    main()
