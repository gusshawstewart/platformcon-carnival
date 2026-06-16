# Step 3 — AI Workflow

Create the workflow that processes requests end-to-end.

## Action

```
upsert_workflow
```

Read the full payload from: `step-3-ai-workflow/workflow.json`

For workflow structure guidance, you may call Port MCP `load_skill` with `name: "workflows"` if needed.

## Workflow stages

1. Fetch service context (tier, owner, language)
2. Branch: Cloud vs On-Premise plan generation
3. AI generates Terraform plan + Mermaid architecture
4. Create `cloud_resource_request` entity with plan output
5. Branch: Production → Slack approval; non-production → auto-approve
6. Slack notifications with links to plan, architecture, and PR

## Done when

Workflow is published and linked to the Step 2 action trigger.

## Fallback

Port UI → Workflows → Import — use `step-3-ai-workflow/workflow.json`.
