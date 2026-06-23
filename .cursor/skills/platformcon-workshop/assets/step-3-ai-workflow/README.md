# Step 3 — AI Workflow

## What We're Building

The intelligence behind the form. A multi-step workflow that:

1. **Gets a Port API token** from client credentials (`get_port_token`)
2. **Fetches service context** from the catalog
3. **Human-in-the-loop (INPUT node)** — authorizes **whether Port may run the AI** to draft an implementation plan (not approval of the final change). Optional notes; **Yes — generate draft plan with AI** continues the run, **No — cancel run** stops before AI and can notify Slack. `numOfResponders` is **1** per path for workshop use.
4. **Branches** on Cloud vs On-Premise
5. **Calls an AI node** to generate an implementation plan + architecture diagram
6. **Creates a request entity** in Port with the AI output
7. **Branches** on environment — Production goes to Slack for approval, everything else auto-approves
8. **Opens a PR** (non-production) and creates the cloud resource entity
9. **Notifies Slack** with links to the plan, architecture, and PR

## The AI Node

The AI node uses Claude with:
- A system prompt scoped to infrastructure architecture
- A user prompt that includes the service tier, language, environment, and requirements
- Structured output: `implementation_plan` (markdown) + `architecture` (Mermaid diagram)

No external MCP tools are required for this workshop workflow; the model answers from the request and catalog context only.

## Conditional Logic

```
trigger
  └── get_port_token (POST /v1/auth/access_token)
        └── fetch_service_context
              └── human_gate_before_plan (INPUT — authorize AI draft only)
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
