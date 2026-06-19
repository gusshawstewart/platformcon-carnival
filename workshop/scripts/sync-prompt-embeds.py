#!/usr/bin/env python3
"""Regenerate workshop/prompts/01–04 with JSON embedded from step-* assets (single source of truth)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROMPTS = ROOT / "workshop" / "prompts"
# JSON sources live with the Cursor skill (Port-in-browser attendees use embedded prompts, not these paths)
ASSETS = ROOT / ".cursor" / "skills" / "platformcon-workshop" / "assets"


def fence(n: int = 3) -> str:
    return "`" * n


def main() -> None:
    s1 = (ASSETS / "step-1-catalog-foundation/service.json").read_text().strip()
    s2 = (ASSETS / "step-1-catalog-foundation/cloud_resource_request.json").read_text().strip()
    s3 = (ASSETS / "step-1-catalog-foundation/cloudResource.json").read_text().strip()
    services = (ASSETS / "sample-data/services.json").read_text().strip()

    md01 = f'''You are helping me build the **catalog foundation** for the PlatformCon-Carne workshop in Port.

**Who this is for:** New Port users. You (Port AI) only see this chat. The JSON below is **included so I can copy it** into Port without hunting files on disk.

**What I will do in Port:** Use **Builder → Blueprints → Import** (or paste JSON), then create **service** entities from the sample list. For each numbered section, **select all the text inside that JSON box**, copy, and paste into Port’s import. If my Port version only has a visual blueprint editor, walk me field-by-field to match the JSON **exactly** (same property identifiers and enums).

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

    w2 = (ASSETS / "step-2-self-service-action/workflow.json").read_text().strip()
    md02 = f'''You are helping me create the **self-service action** for the PlatformCon-Carne workshop in Port.

**Who this is for:** New Port users. You do not need files on disk—the JSON is **in the box below**.

In Port, open **Settings → Self-service → Actions → Import** (wording may vary). **Select all the text in that JSON box**, copy, and paste into the import field.

**Goal:** Action **Create a new resource** appears under Self-Service. Form: infrastructure type, resource types (cloud vs on-prem), environment, **service** entity picker (`service` blueprint), additional context.

---

## Action + trigger JSON

{fence(3)}json
{w2}
{fence(3)}

**After import, check:** Cloud vs On-Premise toggles resource type options; **Service** is an entity field on blueprint `service`; environments include Development / Staging / Production.

**Done when:** I can open Self-Service and the form loads with no error.
'''
    (PROMPTS / "02-self-service-action.md").write_text(md02)

    w3 = (ASSETS / "step-3-ai-workflow/workflow.json").read_text().strip()
    n = 5
    md03 = f'''You are helping me install the **AI workflow** for the PlatformCon-Carne workshop in Port.

**Who this is for:** New Port users. The full workflow definition is **in the JSON box below**. In Port, open **Settings → Workflows → Import** (or your Port version’s equivalent). **Select all the text inside that box**, copy, and paste into the import field. You do not need files from disk.

**Goal:** Workflow identifier `request_cloud_resource` is **published** and wired to the same self-service action from the previous step. Submitting the form should start a run.

**Notes:**
- **Workflows may be beta** — if import is disabled, say what to ask an admin.
- **INPUT node** `human_gate_before_plan`: after service context loads, someone chooses **Yes — generate draft plan with AI** or **No — cancel run** before any AI step runs. That authorizes **running the AI to draft a plan**, not approving the final infrastructure change.
- **AI nodes** use `tools: []` and **no `mcpServers`** so the workshop does not require GitHub or Notion MCP server entities in Port.
- **Slack** nodes need secrets `SLACK_BOT_TOKEN` and `SLACK_PLATFORM_CHANNEL` to succeed; other steps may still run.
- The fetch-service webhook uses **`https://api.port.io`** for the Port API. Slack deep links still use `app.getport.io`; change if your tenant uses a different app host.

**After import:** Tell me where to open the **run timeline** and what **waiting for input** looks like for the INPUT step.

---

## Full workflow JSON

{fence(n)}
{w3}
{fence(n)}
'''
    (PROMPTS / "03-ai-workflow.md").write_text(md03)

    backup = (ASSETS / "step-4-demo-flow/backup-entity.json").read_text().strip()
    md04 = f'''This is **Step 4 — smoke test your build** for **you as an attendee** (after steps 0–3).

**What this step is for:** Prove the catalog, self-service form, and workflow work end-to-end. You will run one **staging** request (non-production path) and one **production** request (approval path), and check the results in Port (and Slack, if your org configured it).

**Optional Port AI:** Paste this file into Port AI if you want a **checklist-style coach** while you work. Port AI cannot use Port for you — **you** still do every click in the browser (Self-Service, workflow run, **Authorize AI to draft a plan**, entity pages).

**Prerequisites:** Branding done, blueprints + sample services loaded, action imported, workflow imported (steps 0–3).

---

### A — Staging path (what you should see)

1. In Port, open **Self-Service** → **Create a new resource**.
2. Submit: **Cloud** · **RDS Database** · **Staging** · **payments-service** · Additional requirements: `Standard configuration with automated backups enabled`.
3. Open the **workflow run**. If it pauses on **Authorize AI to draft a plan** → **Provide inputs** → **Yes — generate draft plan with AI**.
4. Confirm a **resource request** entity (blueprint `cloud_resource_request`) appears with **implementation plan** and **architecture** filled in (entity page / tabs, depending on your layout).
5. If Slack is configured for your org, check the channel for an **auto-approved** style message.

### B — Production path (what you should see)

Repeat **A**, but set **Environment** to **Production**. Confirm the run follows the **production** branch (e.g. Slack approval message with links — only if secrets exist).

### C — Backup sample (optional)

If **AI is slow** or you want to **see example plan text without waiting for the AI node**, you or a facilitator can import this ready-made entity on blueprint **`cloud_resource_request`** using Port’s entity import (or equivalent). **Select all the text in the sample JSON box below**, copy, and paste into that import flow.

{fence(n)}
{backup}
{fence(n)}

**Done when:** You have personally completed **A** and **B** in Port (or you and a facilitator have walked through the same checks together at your table).

Presenter notes (optional): [step-4-demo-flow/README.md](../../.cursor/skills/platformcon-workshop/assets/step-4-demo-flow/README.md) in this repo.
'''
    (PROMPTS / "04-demo-verification.md").write_text(md04)
    print("Updated workshop/prompts/01–04 from step-* JSON files.")


if __name__ == "__main__":
    main()
