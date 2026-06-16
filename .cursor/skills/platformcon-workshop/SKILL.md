---
name: platformcon-workshop
description: >-
  Set up the PlatformCon-Carne self-service cloud resource provisioning platform
  in Port via MCP. Use when the user asks to set up, build, or configure the
  workshop, PlatformCon-Carne platform, cloud resource catalog, self-service
  action, or AI workflow.
---

# PlatformCon-Carne Workshop

Build a self-service cloud resource platform in Port: catalog → form → AI workflow → demo.

## Prerequisites

Confirm before starting:

- [Port account](https://app.getport.io/signup) (free tier works)
- Port MCP in Cursor (`https://mcp.port.io/v1` or EU: `https://mcp.port-eu.io/v1`)
- This repo open in Cursor

## How to run this skill

**One step at a time.** Do not read all step files upfront.

1. Check the progress checklist below — find the first unchecked step.
2. Read **only** that step's file from [steps/](steps/).
3. Execute that step via Port MCP (read JSON payloads from disk; do not invent schemas).
4. Summarize what was created and ask the user to continue before moving on.

### Rules

- Use identifiers exactly as specified. Do not create extra blueprints or entities.
- Before each MCP call, briefly say what you're doing and why.
- If MCP fails, offer the manual fallback from the step file, then continue.
- Check the Port MCP tool schema before calling unfamiliar tools.

## Progress

```
- [ ] Step 0 — Portal branding
- [ ] Step 1 — Catalog foundation (3 blueprints + sample services)
- [ ] Step 2 — Self-service action
- [ ] Step 3 — AI workflow
- [ ] Step 4 — Test / demo
```

| Step | Read when executing | Repo assets |
|------|---------------------|-------------|
| 0 | [steps/step-0-portal.md](steps/step-0-portal.md) | — |
| 1 | [steps/step-1-catalog.md](steps/step-1-catalog.md) | `step-1-catalog-foundation/*.json`, `sample-data/services.json` |
| 2 | [steps/step-2-action.md](steps/step-2-action.md) | `step-2-self-service-action/workflow.json` |
| 3 | [steps/step-3-workflow.md](steps/step-3-workflow.md) | `step-3-ai-workflow/workflow.json` |
| 4 | [steps/step-4-demo.md](steps/step-4-demo.md) | `step-4-demo-flow/backup-entity.json` |

## What you're building

1. Catalog of services, resource requests, and provisioned resources
2. Self-service form to submit requests
3. AI workflow that generates implementation plans
4. Conditional approval: non-production auto-approves, production goes to Slack

Background: [company-context.md](../../../company-context.md)
