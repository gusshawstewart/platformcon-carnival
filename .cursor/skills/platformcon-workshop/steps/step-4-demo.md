# Step 4 — Port skill (request resource)

**Audience:** Attendees after steps 0–3. Create a **Port skill** that triggers workflow **`request_cloud_resource`**.

## 1. Create the `skill` blueprint

If blueprint **`skill`** is missing, import [`../assets/step-4-port-skill/skill-blueprint.json`](../assets/step-4-port-skill/skill-blueprint.json).

## 2. Create the skill entity

Upsert on blueprint **`skill`** from [`../assets/step-4-port-skill/skill-entity.json`](../assets/step-4-port-skill/skill-entity.json).

Identifier: **`platformcon-carne-request-resource`**

## 3. Use in Port AI chat

User message example:

> Request a cloud resource for the PlatformCon-Carne workshop.

Port AI loads the skill and calls **`trigger_workflow_run`** with:

| Input | Default |
|-------|---------|
| `infrastructure_type` | Cloud |
| `cloud_resource_type` | RDS Database |
| `environment` | Staging |
| `service` | payments-service |
| `additional_context` | Standard configuration with automated backups enabled |

## Done when

- Skill entity exists
- **`request_cloud_resource`** workflow run was triggered (run id returned)

Presenter notes: [`../assets/step-4-demo-flow/README.md`](../assets/step-4-demo-flow/README.md)
