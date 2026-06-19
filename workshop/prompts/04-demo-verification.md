This is **Step 4 — smoke test your build** for **you as an attendee** (after steps 0–3).

**What this step is for:** Prove the catalog, self-service form, and workflow work end-to-end. You will run one **staging** request (non-production path) and one **production** request (approval path), and check the results in Port (and Slack, if your org configured it).

**Optional Port AI:** Paste this file into Port AI if you want a **checklist-style coach** while you work. Port AI cannot use Port for you — **you** still do every click in the browser (Self-Service, workflow run, **Authorize AI to draft a plan**, entity pages).

**Prerequisites:** Branding done, blueprints + sample services loaded, action imported, workflow imported (steps 0–3).

---

### A — Staging path (what you should see)

1. In Port, open **Self-Service** → **Create a new resource**.
2. Submit: **Cloud** · **RDS Database** · **Staging** · **payments-service** · Additional requirements: `Standard configuration with automated backups enabled`.
3. Open the **workflow run**. If it pauses on **Authorize AI to draft a plan** → **Provide inputs** → **Yes — generate draft plan with AI**.
4. Confirm a **resource request** entity (blueprint `cloud_resource_request`) appears with **implementation plan** and **architecture** filled in (entity page / tabs, depending on your layout).
5. If Slack is configured for your org, check the channel for an **auto-approved** style message.

### B — Production path (what you should see)

Repeat **A**, but set **Environment** to **Production**. Confirm the run follows the **production** branch (e.g. Slack approval message with links — only if secrets exist).

### C — Backup sample (optional)

If **AI is slow** or you want to **see example plan text without waiting for the AI node**, you or a facilitator can import this ready-made entity on blueprint **`cloud_resource_request`** using Port’s entity import (or equivalent). **Select all the text in the sample JSON box below**, copy, and paste into that import flow.

`````
{
  "identifier": "staging-payments-service-rds-database",
  "title": "RDS Database for Payments Service",
  "blueprint": "cloud_resource_request",
  "properties": {
    "status": "Approved",
    "environment": "Staging",
    "resource_type": "RDS Database",
    "infrastructure_type": "Cloud",
    "additional_context": "Standard configuration with automated backups enabled",
    "requested_at": "2025-06-01T10:00:00Z",
    "approved_at": "2025-06-01T10:00:45Z",
    "approved_by": "Auto-approved (Non-Production)",
    "pr_url": "https://github.com/platformcon-carne/terraform-modules/pull/1",
    "implementation_plan": "## RDS PostgreSQL Implementation Plan\n\n**Service:** Payments Service (Gold Tier)\n**Environment:** Staging\n**Module:** `terraform-modules/rds-postgresql`\n\n### Steps\n\n1. **Reference existing module**\n```hcl\nmodule \"payments_rds\" {\n  source = \"../modules/rds-postgresql\"\n  \n  identifier     = \"payments-staging\"\n  instance_class = \"db.t3.medium\"\n  engine_version = \"15.4\"\n  \n  multi_az               = false  # staging\n  backup_retention_period = 7\n  storage_encrypted      = true\n  \n  tags = {\n    Service     = \"payments-service\"\n    Environment = \"staging\"\n    ManagedBy   = \"terraform\"\n    RequestId   = \"staging-payments-service-rds-database\"\n  }\n}\n```\n\n2. **Apply via CI/CD**\n   - PR opened against `main` branch\n   - Terraform plan reviewed automatically\n   - Merge triggers `terraform apply` in staging account\n\n3. **Post-provisioning**\n   - Connection string written to AWS Secrets Manager\n   - CloudWatch alarms created for CPU, connections, storage\n   - Port entity updated to `Active` status",
    "architecture": "```mermaid\nflowchart TB\n    subgraph VPC[\"Staging VPC (eu-west-1)\"]\n        subgraph App[\"Application Tier\"]\n            Service[\"Payments Service\\n(Go / Gold Tier)\"]\n        end\n        Service -->|\"5432\"| DB[(\"RDS PostgreSQL\\ndb.t3.medium\")]\n    end\n    subgraph Monitoring\n        CW[\"CloudWatch\\nAlarms\"]\n        PI[\"Performance\\nInsights\"]\n    end\n    DB --> CW\n    DB --> PI\n```"
  },
  "relations": {
    "requested_by_service": "payments-service"
  }
}
`````

**Done when:** You have personally completed **A** and **B** in Port (or you and a facilitator have walked through the same checks together at your table).

Presenter notes (optional): [step-4-demo-flow/README.md](../../.cursor/skills/platformcon-workshop/assets/step-4-demo-flow/README.md) in this repo.
