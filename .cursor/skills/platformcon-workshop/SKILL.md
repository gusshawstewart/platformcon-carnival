---
name: platformcon-workshop
description: >-
  Set up the PlatformCon-Carne self-service cloud resource provisioning platform
  in Port via MCP. Use when the user asks to set up, build, or configure the
  workshop, PlatformCon-Carne platform, cloud resource catalog, self-service
  action, or AI workflow. JSON payloads live under this skill's assets/ folder.
  For live sessions in Port only, prefer workshop/prompts/ over this skill.
---

# PlatformCon-Carne Workshop

Build a self-service cloud resource platform in Port: catalog → form → AI workflow → demo.

**Live sessions (Port in browser):** point attendees to [workshop/README.md](../../../workshop/README.md) and [workshop/prompts/](../../../workshop/prompts/); facilitators to [workshop/FACILITATOR.md](../../../workshop/FACILITATOR.md). **Workshop logins:** attendees claim a row in the [credentials sheet](https://docs.google.com/spreadsheets/d/1U2ywpAVrfdG6H-iTPT0__L26MKdA5o6mqZyzp61CzLk/edit) (name + email) and use that row’s username/password—**no Port signup** for that path. This skill is for **Cursor + Port MCP** automation; authoring JSON is under [assets/](assets/).

## Prerequisites

Confirm before starting:

- [Port account](https://app.getport.io/signup) (free tier works)
- Port MCP in Cursor (`https://mcp.port.io/v1` or EU: `https://mcp.port-eu.io/v1`)
- This repo open in Cursor

## How to run this skill

**One step at a time.** Do not read all step files upfront.

1. Check the progress checklist below — find the first unchecked step.
2. Read **only** that step's file from [steps/](steps/).
3. Execute that step via Port MCP (read JSON payloads from [assets/](assets/); do not invent schemas).
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
- [ ] Step 4 — Port `skill` blueprint + request-resource skill (triggers workflow)
```

| Step | Read when executing | Repo assets |
|------|---------------------|-------------|
| 0 | [steps/step-0-portal.md](steps/step-0-portal.md) | — |
| 1 | [steps/step-1-catalog.md](steps/step-1-catalog.md) | [assets/step-1-catalog-foundation/](assets/step-1-catalog-foundation/) · [assets/sample-data/services.json](assets/sample-data/services.json) |
| 2 | [steps/step-2-action.md](steps/step-2-action.md) | [assets/step-2-self-service-action/workflow.json](assets/step-2-self-service-action/workflow.json) |
| 3 | [steps/step-3-workflow.md](steps/step-3-workflow.md) | [assets/step-3-ai-workflow/workflow.json](assets/step-3-ai-workflow/workflow.json) |
| 4 | [steps/step-4-demo.md](steps/step-4-demo.md) | [assets/step-4-port-skill/skill-blueprint.json](assets/step-4-port-skill/skill-blueprint.json) · [assets/step-4-port-skill/skill-entity.json](assets/step-4-port-skill/skill-entity.json) (from [SKILL.md](assets/step-4-port-skill/platformcon-carne-request-resource/SKILL.md)) |

## What you're building

1. Catalog of services, resource requests, and provisioned resources
2. Self-service form to submit requests
3. AI workflow that generates implementation plans
4. Conditional approval: non-production auto-approves, production goes to Slack

Background: [company-context.md](../../../company-context.md)
