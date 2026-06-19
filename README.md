# From IDP to AEP: Building an AI-Enhanced Platform

**PlatformCon Workshop** · ~1 hour · Port (primary) · optional Cursor for facilitators

---

## Live session (most attendees)

**You do not need Cursor.** Use the workshop path:

- **[workshop/README.md](./workshop/README.md)** — start here  
- **[workshop/prompts/](./workshop/prompts/)** — prompts for **Port AI** with **embedded JSON** (GitHub in a browser is enough; no local clone required for copy-paste)  
- Facilitators: **[workshop/FACILITATOR.md](./workshop/FACILITATOR.md)** — pre-provisioned Portals, seating, beta / onboarding notes  

Pre-provisioned Port organizations and credentials are **outside this repo** (you maintain those separately).

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

## How to set this up

### Path A — Workshop / live session (recommended)

1. Use the **Port organization** your facilitator assigned (see [workshop/FACILITATOR.md](./workshop/FACILITATOR.md)).
2. Clone or download this repo so you have the JSON files locally:
```bash
git clone https://github.com/YOUR_ORG/platformcon-carne.git
cd platformcon-carne
```
3. Follow **[workshop/README.md](./workshop/README.md)** and the numbered prompts under **[workshop/prompts/](./workshop/prompts/)**.

### Path B — Cursor + Port MCP (optional)

For facilitators or attendees who already use **Cursor** with MCP:

1. Clone this repo (same as above).
2. Configure the Port MCP in `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "port": {
      "url": "https://mcp.port.io/v1"
    }
  }
}
```
> EU region: use `https://mcp.port-eu.io/v1` — check at https://app.getport.io/settings/credentials

3. Restart Cursor and authenticate when prompted.

4. Open this repo in Cursor, open the AI chat, and say:  
   **"Set up the PlatformCon-Carne cloud resource provisioning platform"**

The agent skill at [`.cursor/skills/platformcon-workshop/SKILL.md`](./.cursor/skills/platformcon-workshop/SKILL.md) runs the same steps as the workshop prompts.

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

- [Workshop path (attendees)](./workshop/README.md) · [Facilitator notes](./workshop/FACILITATOR.md) · [Prompt library](./workshop/prompts/)
- [Port Documentation](https://docs.getport.io)
- [Port MCP Setup](https://docs.getport.io/guides-and-tutorials/setup-port-mcp)
- [AI Agents in Port](https://docs.getport.io/ai-interfaces/ai-agents/overview)
- [Port Free Tier](https://app.getport.io/signup)

---

Built with 🥩 for PlatformCon
