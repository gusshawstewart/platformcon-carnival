# From IDP to AEP: Building an AI-Enhanced Platform

**PlatformCon Workshop** · 1 hour · Port + Cursor

---

## What We're Building

A self-service cloud resource provisioning system that evolves from a basic catalog to a fully agentic platform — built live, step by step.

By the end, when a developer needs a new cloud resource:

1. They fill in a simple form — service, environment, resource type
2. Port **fetches context** about their service automatically
3. An AI agent **generates an implementation plan + architecture diagram** using their GitHub and Notion context
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

## How to Set This Up

**You need:**
- A [Port account](https://app.getport.io/signup) (free tier works)
- [Cursor](https://cursor.sh) with MCP support

**Setup:**
1. Clone this repo:
```
git clone https://github.com/YOUR_ORG/platformcon-carne-workshop
cd platformcon-carne-workshop
```

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

3. Restart Cursor and authenticate when prompted

4. Open this repo in Cursor, open the AI chat, and say:
   **"Set up the PlatformCon-Carne cloud resource provisioning platform"**

The skill at `.cursor/skills/platformcon-workshop/SKILL.md` guides the agent through each step.

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

- [Port Documentation](https://docs.getport.io)
- [Port MCP Setup](https://docs.getport.io/guides-and-tutorials/setup-port-mcp)
- [AI Agents in Port](https://docs.getport.io/ai-interfaces/ai-agents/overview)
- [Port Free Tier](https://app.getport.io/signup)

---

Built with 🥩 for PlatformCon
