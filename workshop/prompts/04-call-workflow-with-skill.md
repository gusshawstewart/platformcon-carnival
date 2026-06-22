You are helping me finish the **PlatformCon-Carne workshop** by creating a **Port skill** that triggers the resource creation workflow.

**Who this is for:** New Port users working in **Port AI** chat. The JSON below is **included so I can copy it** into Port without hunting files on disk.

**What we are doing** ([Port skills docs](https://docs.port.io/ai-interfaces/skills/)):

1. Create the **`skill` blueprint** in the data model (skip if your org already has one).
2. Create a **custom skill entity** whose only job is to call workflow **`request_cloud_resource`** via **`trigger_workflow_run`**.
3. Open **Port AI** and ask to request a resource — Port AI loads the skill and starts the workflow for you.

**Prerequisites:** Steps 0–3 complete (branding, catalog, action, workflow **`request_cloud_resource`** published).

---

## 1 — Blueprint `skill`

**In Port:** **Builder → Blueprints → Import** (or paste JSON). Skip this section if blueprint **`skill`** already exists.

```json
{
  "identifier": "skill",
  "title": "Skill",
  "icon": "Learn",
  "schema": {
    "properties": {
      "description": {
        "title": "Description",
        "type": "string",
        "description": "What the skill does and when the model should use it"
      },
      "instructions": {
        "title": "Instructions",
        "type": "string",
        "format": "markdown",
        "description": "Step-by-step instructions for the AI to follow"
      },
      "references": {
        "title": "References",
        "type": "array",
        "description": "Reference documents for the skill",
        "items": {
          "type": "object",
          "properties": {
            "path": {
              "type": "string",
              "description": "Resource path (e.g., references/common-errors.md)"
            },
            "content": {
              "type": "string",
              "description": "The file content"
            },
            "description": {
              "type": "string",
              "description": "Optional description of the resource"
            }
          },
          "required": ["path", "content"],
          "additionalProperties": false
        }
      },
      "assets": {
        "title": "Assets",
        "type": "array",
        "description": "Asset files (templates, configs) for the skill",
        "items": {
          "type": "object",
          "properties": {
            "path": {
              "type": "string",
              "description": "Asset path (e.g., assets/mapping-template.yaml)"
            },
            "content": {
              "type": "string",
              "description": "The file content"
            },
            "description": {
              "type": "string",
              "description": "Optional description of the asset"
            }
          },
          "required": ["path", "content"],
          "additionalProperties": false
        }
      },
      "location": {
        "type": "string",
        "title": "Location",
        "description": "The target directory where the skill will be created on the machine.",
        "default": "global",
        "enum": ["global", "project"],
        "enumColors": {
          "global": "lightGray",
          "project": "lightGray"
        }
      }
    },
    "required": ["description", "instructions", "location"]
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {}
}
```

---

## 2 — Skill entity `platformcon-carne-request-resource`

**In Port:** Open the catalog page for blueprint **`skill`** → **New entity** (or entity JSON import). **Select all the text in the JSON box below**, copy, and paste.

```json
{
  "identifier": "platformcon-carne-request-resource",
  "title": "PlatformCon-Carne \u2014 Request resource",
  "properties": {
    "description": "Run the PlatformCon-Carne \"Create a new resource\" workflow. Use when the user asks to request a cloud resource, create infrastructure, run step 4, or trigger the resource creation workflow.",
    "instructions": "# Request a cloud resource\n\nYour only job is to start the **`request_cloud_resource`** workflow using **`trigger_workflow_run`**.\n\n## Inputs\n\nUse values the user provided. If they did not specify, use these workshop defaults:\n\n- `infrastructure_type`: `Cloud`\n- `cloud_resource_type`: `RDS Database`\n- `environment`: `Staging`\n- `service`: `payments-service` (entity identifier on blueprint `service`)\n- `additional_context`: `Standard configuration with automated backups enabled`\n\nRequired trigger fields: `infrastructure_type`, `environment`, `service`.\n\n## Steps\n\n1. Call **`trigger_workflow_run`** with:\n   - `identifier`: `request_cloud_resource`\n   - `inputs`: the object above (include `cloud_resource_type` when infrastructure is Cloud)\n\n2. Return the workflow **run identifier** and current status.\n\n3. Optionally poll **`get_workflow_run`** until the run completes or waits for user input.\n\nDo not walk the user through Self-Service UI clicks. Do not import sample entities. Do not smoke-test manually \u2014 trigger the workflow and report the result.",
    "location": "global"
  }
}
```

**Check:** Entity **`platformcon-carne-request-resource`** appears on the **Skill** catalog page.

---

## 3 — Call the skill from Port AI chat

1. Open **Port AI** (in-product chat).
2. Send a message such as:

   > Request a cloud resource for the PlatformCon-Carne workshop.

3. Port AI should **load** skill **`platformcon-carne-request-resource`** and call **`trigger_workflow_run`** on workflow **`request_cloud_resource`** with the workshop defaults (Cloud · RDS Database · Staging · payments-service) unless you specified other values.
4. Confirm you receive a **workflow run id** and can open the run in Port.

**Done when:** Skill entity exists and Port AI successfully triggered **`request_cloud_resource`**.

Presenter notes (optional): [step-4-demo-flow/README.md](../../.cursor/skills/platformcon-workshop/assets/step-4-demo-flow/README.md) in this repo.
