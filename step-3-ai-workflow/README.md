# Step 3 — AI Workflow

## What We're Building

The intelligence behind the form. A multi-step workflow that:

1. **Fetches service context** from the catalog
2. **Human-in-the-loop (INPUT node)** — optional notes, then *Proceed with AI plan* or *Stop run* (stop notifies Slack and ends that branch). Uses Port’s `INPUT` node; `numOfResponders` is **1** per path so you can test solo.
3. **Branches** on Cloud vs On-Premise
4. **Calls an AI node** to generate an implementation plan + architecture diagram
5. **Creates a request entity** in Port with the AI output
6. **Branches** on environment — Production goes to Slack for approval, everything else auto-approves
7. **Opens a PR** (non-production) and creates the cloud resource entity
8. **Notifies Slack** with links to the plan, architecture, and PR

## The AI Node

The AI node uses Claude with:
- A system prompt scoped to infrastructure architecture
- A user prompt that includes the service tier, language, environment, and requirements
- GitHub MCP to search for existing Terraform modules
- Notion MCP to find relevant runbooks
- Structured output: `implementation_plan` (markdown) + `architecture` (Mermaid diagram)

## Conditional Logic

```
trigger
  └── fetch_service_context
        └── human_gate_before_plan (INPUT — early HITL preview)
              ├── proceed → condition: Cloud or On-Premise?
              │         ├── Cloud → ai_generate_plan_cloud
              │         └── On-Premise → ai_generate_plan_onprem
              │               └── create_request
              │                     └── condition: Production?
              │                           ├── Production → slack_approval_request (STOP — human approves)
              │                           └── Non-Production → open_pr → update_catalog → slack_notify
              └── stop → slack_hitl_gate_stopped
```

## Why This Structure

The branching isn't just cosmetic — it means:
- Cloud and on-prem have different AI prompts (AWS Terraform vs VMware vSphere)
- Production changes require a human decision; non-production don't
- The policy lives in the workflow, not in someone's memory

## Time

~12 minutes

## Fallback

Import `workflow.json` via Port UI:
- Settings → Workflows → Import
- This replaces the Step 2 workflow (same identifier, adds all the nodes)
