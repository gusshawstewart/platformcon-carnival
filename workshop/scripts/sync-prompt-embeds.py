#!/usr/bin/env python3
"""Regenerate workshop/prompts/01–04 and the Port step-4 skill entity JSON from step-* assets."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROMPTS = ROOT / "workshop" / "prompts"
# JSON sources live with the Cursor skill (Port-in-browser attendees use embedded prompts, not these paths)
ASSETS = ROOT / ".cursor" / "skills" / "platformcon-workshop" / "assets"
STEP4 = ASSETS / "step-4-port-skill"
SKILL_DIR = STEP4 / "platformcon-carne-request-resource"


def fence(n: int = 3) -> str:
    return "`" * n


def parse_skill_md(skill_dir: Path) -> dict:
    """Parse Agent Skills SKILL.md frontmatter + body (see Port skills docs)."""
    content = skill_dir.joinpath("SKILL.md").read_text()
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not match:
        raise ValueError(f"Invalid SKILL.md in {skill_dir}: missing YAML frontmatter")

    frontmatter: dict = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.endswith(":") and ">" not in line:
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            frontmatter[key.strip()] = value.strip().strip("'\"")
        elif line.startswith(">"):
            frontmatter.setdefault("description", "")
            frontmatter["description"] += line.lstrip("> ").strip() + " "

    # Multi-line description via yaml block scalar (---\ndescription: >-\n  line...)
    desc_match = re.search(
        r"^description:\s*>-?\s*\n((?:[ \t]+.+\n?)+)",
        match.group(1),
        re.MULTILINE,
    )
    if desc_match:
        frontmatter["description"] = " ".join(
            ln.strip() for ln in desc_match.group(1).splitlines()
        ).strip()

    metadata_title_match = re.search(
        r"^metadata:\s*\n\s*title:\s*(.+)$", match.group(1), re.MULTILINE
    )
    title = (
        metadata_title_match.group(1).strip().strip("'\"")
        if metadata_title_match
        else frontmatter.get("name", "Skill")
    )

    return {
        "identifier": frontmatter["name"],
        "title": title,
        "description": frontmatter["description"].strip(),
        "instructions": match.group(2).strip(),
    }


def read_skill_assets(skill_dir: Path) -> list[dict]:
    assets_dir = skill_dir / "assets"
    if not assets_dir.is_dir():
        return []
    items: list[dict] = []
    for file_path in sorted(assets_dir.rglob("*")):
        if file_path.is_file():
            rel = file_path.relative_to(assets_dir)
            items.append(
                {
                    "path": f"assets/{rel.as_posix()}",
                    "content": file_path.read_text(),
                }
            )
    return items


def build_skill_entity(skill_dir: Path) -> dict:
    parsed = parse_skill_md(skill_dir)
    properties: dict = {
        "description": parsed["description"],
        "instructions": parsed["instructions"],
        "location": "global",
    }
    assets = read_skill_assets(skill_dir)
    if assets:
        properties["assets"] = assets
    return {
        "identifier": parsed["identifier"],
        "title": parsed["title"],
        "properties": properties,
    }


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
- The fetch-service webhook uses **`https://api.port.io`** for the Port API and needs secret **`PORT_CLIENT_SECRET`** (Bearer token) in workflow secrets. Slack deep links still use `app.getport.io`; change if your tenant uses a different app host.

**After import:** Tell me where to open the **run timeline** and what **waiting for input** looks like for the INPUT step.

---

## Full workflow JSON

{fence(n)}
{w3}
{fence(n)}
'''
    (PROMPTS / "03-ai-workflow.md").write_text(md03)

    skill_blueprint = (STEP4 / "skill-blueprint.json").read_text().strip()
    skill_entity_obj = build_skill_entity(SKILL_DIR)
    skill_entity = json.dumps(skill_entity_obj, indent=2)
    skill_identifier = skill_entity_obj["identifier"]
    (STEP4 / "skill-entity.json").write_text(skill_entity + "\n")

    md04 = f'''You are helping me finish the **PlatformCon-Carne workshop** by creating a **Port skill** that triggers the resource creation workflow.

**Who this is for:** New Port users working in **Port AI** chat. The JSON below is **included so I can copy it** into Port without hunting files on disk.

**What we are doing** ([Port skills docs](https://docs.port.io/ai-interfaces/skills/)):

1. Create the **`skill` blueprint** in the data model (skip if your org already has one).
2. Create a **custom skill entity** whose only job is to call workflow **`request_cloud_resource`** via **`trigger_workflow_run`**.
3. Open **Port AI** and ask to request a resource — Port AI loads the skill and starts the workflow for you.

**Prerequisites:** Steps 0–3 complete (branding, catalog, action, workflow **`request_cloud_resource`** published).

---

## 1 — Blueprint `skill`

**In Port:** **Builder → Blueprints → Import** (or paste JSON). Skip this section if blueprint **`skill`** already exists.

{fence(3)}json
{skill_blueprint}
{fence(3)}

---

## 2 — Skill entity `{skill_identifier}`

**In Port:** Open the catalog page for blueprint **`skill`** → **New entity** (or entity JSON import). **Select all the text in the JSON box below**, copy, and paste.

{fence(3)}json
{skill_entity}
{fence(3)}

**Check:** Entity **`{skill_identifier}`** appears on the **Skill** catalog page.

---

## 3 — Call the skill from Port AI chat

1. Open **Port AI** (in-product chat).
2. Send a message such as:

   > Request a cloud resource for the PlatformCon-Carne workshop.

3. Port AI should **load** skill **`{skill_identifier}`** and call **`trigger_workflow_run`** on workflow **`request_cloud_resource`** with the workshop defaults (Cloud · RDS Database · Staging · payments-service) unless you specified other values.
4. Confirm you receive a **workflow run id** and can open the run in Port.

**Done when:** Skill entity exists and Port AI successfully triggered **`request_cloud_resource`**.

Presenter notes (optional): [step-4-demo-flow/README.md](../../.cursor/skills/platformcon-workshop/assets/step-4-demo-flow/README.md) in this repo.
'''
    (PROMPTS / "04-demo-verification.md").write_text(md04)
    print("Updated workshop/prompts/01–04 from step-* JSON files.")


if __name__ == "__main__":
    main()
