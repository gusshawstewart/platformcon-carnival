# From IDP to AEP: Building an AI-Enhanced Platform

**PlatformCon Workshop** · ~1 hour · Port + Port AI

---

## Live session (attendees)

Start here:

- **[workshop/README.md](./workshop/README.md)** — how to run the session in the browser  
- **[workshop/prompts/](./workshop/prompts/)** — copy-paste prompts with **embedded JSON** for Port (GitHub in a browser is enough)  

### Workshop logins (attendees)

**You do not sign up or create your own Port account for this session.** Use a **pre-provisioned login** from the facilitator’s sheet:

**[Workshop credentials (Google Sheet)](https://docs.google.com/spreadsheets/d/1U2ywpAVrfdG6H-iTPT0__L26MKdA5o6mqZyzp61CzLk/edit)**

1. Open the sheet (access may be **restricted until the event day**—ask the facilitator if it is locked).
2. Pick a **free row** that still has empty **name / email** columns (wording may vary slightly in the sheet).
3. Add **your name and email** in that row so others know the seat is taken.
4. Use the **username and password** on that same row to **log in to Port** (and the **Portal URL** if the sheet includes one).

Details and facilitator notes: [workshop/README.md](./workshop/README.md) · [workshop/FACILITATOR.md](./workshop/FACILITATOR.md).

---

## What We're Building

A self-service cloud resource provisioning system that evolves from a basic catalog to a fully agentic platform — built live, step by step.

By the end, when a developer needs a new cloud resource:

1. They fill in a simple form — service, environment, resource type
2. Port **fetches context** about their service automatically
3. An AI agent **generates an implementation plan + architecture diagram** from the catalog context and the request details (no workshop dependency on GitHub or Notion MCP inside the workflow)
4. For non-production: **auto-approved**, PR opened, Slack notified
5. For production: **approval request sent to Slack**, one click to approve
6. The resource is tracked in the catalog — linked to the service that owns it

No tickets. No waiting. No tribal knowledge. Just good data, good prompts, and good actions.

---

## The Scenario

We're building for **PlatformCon-Carne** 🥩 — a fictional platform engineering team at a fast-growing food delivery company.

Their pain: developers open Jira tickets to request cloud resources. The platform team spends half their week provisioning RDS databases, S3 buckets, and EC2 instances. Nothing is tracked. Nobody knows what exists where.

Today, we fix that.

See [company-context.md](./company-context.md) for the full backstory.

---

## How to run the workshop

1. **Claim a row** in the **[workshop credentials sheet](https://docs.google.com/spreadsheets/d/1U2ywpAVrfdG6H-iTPT0__L26MKdA5o6mqZyzp61CzLk/edit)** (add your name and email), then **log in with that row’s username and password**—**no self-service signup** for this workshop.
2. Open **[workshop/README.md](./workshop/README.md)** and the numbered files under **[workshop/prompts/](./workshop/prompts/)** (on GitHub or after a clone). Follow steps **0 → 4** in order.
3. Optionally paste each prompt into **Port AI** for a guided checklist while you click in Port.

Cloning the repo is **optional** for attendees—the prompts already contain the JSON to import.

---

## The Journey

```
No visibility  →  Catalog  →  Self-Service Action  →  AI Workflow  →  Demo
   (chaos)        (see)           (act)               (automate)    (wow)
```

| Step | What We Build | What It Enables |
|------|--------------|-----------------|
| 0 | Portal branding | Make it ours |
| 1 | Catalog — 3 blueprints, sample data | Visibility — see all services and resources |
| 2 | Self-service action form | Developers request resources without tickets |
| 3 | AI workflow — plan, approve, notify | AI generates the plan, port tracks everything |
| 4 | Live demo | Watch a developer request an RDS database end-to-end |

---

## Key Concepts

**Why does the AI need a catalog?** The AI node can only reason about what it can see. The catalog is its world model — services, their tiers, their owners. Without it, the AI is generating generic plans. With it, it generates plans tailored to *this* service, *this* team, *this* environment.

**Why UPSERT_ENTITY?** The workflow writes directly back to the catalog — no external webhooks needed for the core loop. The request entity, the resource entity, the approval status — all tracked in Port, auditable, searchable.

**Why conditional branching?** Production and non-production have different risk profiles. The workflow encodes that policy automatically — developers don't need to know the rules, they just fill in the form.

**Human in the loop?** Always. The AI recommends. The human approves production changes. Same actions, same audit trail.

---

## Resources

- [Workshop (attendees)](./workshop/README.md) · [Facilitator notes](./workshop/FACILITATOR.md) · [Prompt library](./workshop/prompts/)
- [Workshop credentials (Google Sheet)](https://docs.google.com/spreadsheets/d/1U2ywpAVrfdG6H-iTPT0__L26MKdA5o6mqZyzp61CzLk/edit) — claim a row; **no signup** for the live session
- [Port Documentation](https://docs.getport.io)
- [AI Agents in Port](https://docs.getport.io/ai-interfaces/ai-agents/overview)
- [Port Free Tier](https://app.getport.io/signup) — **not** required for this workshop if you use a sheet login above

### Facilitators:
- **Facilitators:** [workshop/FACILITATOR.md](./workshop/FACILITATOR.md) — pre-provisioned Portals, seating, beta / onboarding  
---

### Optional: Cursor + Port MCP

If you use **[Cursor](https://cursor.com)** and want the agent to drive Port via MCP, configure the [Port MCP](https://docs.getport.io/guides-and-tutorials/setup-port-mcp) (`https://mcp.port.io/v1`, or EU `https://mcp.port-eu.io/v1`), then use the skill at [`.cursor/skills/platformcon-workshop/SKILL.md`](./.cursor/skills/platformcon-workshop/SKILL.md). Authoring JSON for that path lives under [`.cursor/skills/platformcon-workshop/assets/`](./.cursor/skills/platformcon-workshop/assets/). **Most workshop participants only need Port + [workshop/prompts/](./workshop/prompts/).**

---

Built with 🥩 for PlatformCon
