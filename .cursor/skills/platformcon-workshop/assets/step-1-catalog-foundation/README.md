# Step 1 — Catalog Foundation

## What We're Building

Three blueprints that form the data model for the entire platform:

| Blueprint | What It Represents |
|-----------|-------------------|
| `service` | Every microservice at PlatformCon-Carne |
| `cloud_resource_request` | Every request a developer submits |
| `cloudResource` | Every provisioned cloud resource |

Plus 6 sample service entities loaded from `../sample-data/services.json`.

## Why These Three

The `service` blueprint is the anchor — everything connects back to it. The AI needs to know *which service* is requesting a resource so it can tailor the plan to its tier and context.

The `cloud_resource_request` blueprint is the audit trail. Every request, its status, the AI-generated plan, the architecture diagram, the approval timestamp — all in one entity.

The `cloudResource` blueprint is the inventory. After provisioning, the actual resource lives here, linked to the service that owns it. No more spreadsheets.

## Relations

```
cloudResource ──used_by──→ service
cloud_resource_request ──requested_by_service──→ service
cloud_resource_request ──provisioned_resource──→ cloudResource
```

`approved_by` on `cloud_resource_request` records who approved the request (auto-approve label or approver name from Slack).

## Time

~10 minutes

## Fallback

If MCP fails, import the blueprint JSONs manually via Port UI:
- Settings → Builder → Import Blueprint
- Use the JSON files in this folder
