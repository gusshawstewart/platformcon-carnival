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
2. **INPUT node (human gate)** — after context load, one responder can proceed or stop before any AI work (`human_gate_before_plan`; early feature — validate in Port before demoing)
3. Branch: Cloud vs On-Premise plan generation
4. AI generates Terraform plan + Mermaid architecture
5. Create `cloud_resource_request` entity with plan output
6. Branch: Production → Slack approval; non-production → auto-approve
7. Slack notifications with links to plan, architecture, and PR

## Done when

Workflow is published and linked to the Step 2 action trigger.

## Fallback

Port UI → Workflows → Import — use `step-3-ai-workflow/workflow.json`.
