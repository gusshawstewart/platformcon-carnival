# Step 3 — AI Workflow

Create the workflow that processes requests end-to-end. The workflow writes `approved_by` and links `provisioned_resource` on `cloud_resource_request` at runtime — upsert that blueprint **in parallel** with the workflow so those fields exist before the first run.

## Workflow secrets

Before the first run, add these workflow secrets (Settings → Workflows → `request_cloud_resource` → Secrets):

| Secret | Value |
|--------|--------|
| `PORT_CLIENT_ID` | Port API client ID (from your org credentials) |
| `PORT_CLIENT_SECRET` | Port API client secret (plain UUID — **not** used as a Bearer token directly) |
| `SLACK_BOT_TOKEN` | Optional — Slack nodes fail without it |
| `SLACK_PLATFORM_CHANNEL` | Optional — Slack channel ID |

The workflow exchanges `PORT_CLIENT_ID` + `PORT_CLIENT_SECRET` for a JWT in node **`get_port_token`**, then passes that token to **`fetch_service_context`**. Do not put the raw client secret in an `Authorization` header.

EU tenants: change `https://api.port.io` to `https://api.port.eu.io` in both `get_port_token` and `fetch_service_context` if needed.

## 3a — Patch `cloud_resource_request` blueprint

```
upsert_blueprint
```

Read the full payload from: `.cursor/skills/platformcon-workshop/assets/step-1-catalog-foundation/cloud_resource_request.json`

Must include (added for this workflow):

- Property `approved_by` — set by auto-approve and production approval paths
- Relation `provisioned_resource` → `cloudResource` — set by `link_request_to_resource`

If Step 1 already created this blueprint, this upsert merges the missing fields; identifiers must match exactly.

## 3b — Upsert workflow

```
upsert_workflow
```

Read the full payload from: `.cursor/skills/platformcon-workshop/assets/step-3-ai-workflow/workflow.json`

The workflow has **15 nodes**. Run this call in parallel with 3a when possible.

For workflow structure guidance, you may call Port MCP `load_skill` with `name: "workflows"` if needed.

## Workflow stages

1. **Get Port API token** — `POST /v1/auth/access_token` with client credentials
2. Fetch service context (tier, owner, language) using the JWT
3. **INPUT node (human gate)** — after context load, one responder authorizes **running the AI to draft** an implementation plan (`human_gate_before_plan`), or cancels the run before any AI work.
4. Branch: Cloud vs On-Premise plan generation
5. AI generates Terraform plan + Mermaid architecture
6. Create `cloud_resource_request` entity with plan output
7. Branch: Production → Slack approval; non-production → auto-approve
8. Slack notifications with links to plan, architecture, and PR

## Done when

`cloud_resource_request` has `approved_by` and `provisioned_resource`; workflow `request_cloud_resource` is published and linked to the Step 2 action trigger; workflow secrets include `PORT_CLIENT_ID` and `PORT_CLIENT_SECRET`.

## Fallback

Port UI → Builder → edit blueprint `cloud_resource_request` (add `approved_by` property and `provisioned_resource` relation to `cloudResource`).

Port UI → Workflows → Import — use `.cursor/skills/platformcon-workshop/assets/step-3-ai-workflow/workflow.json`.

Add secrets `PORT_CLIENT_ID` and `PORT_CLIENT_SECRET` on the workflow before testing.
