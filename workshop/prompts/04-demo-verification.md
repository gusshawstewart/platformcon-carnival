You are helping me **verify** the PlatformCon-Carne workshop in Port.

**Who this is for:** New Port users. You only see this chat—I run everything in the Port UI.

**Prerequisites:** Steps 0–3 done (branding, three blueprints + services, action, workflow).

---

### A — Staging path

1. **Self-Service** → **Create a new resource**.
2. **Cloud** · **RDS Database** · **Staging** · **payments-service** · Additional requirements: `Standard configuration with automated backups enabled`.
3. Submit → open the **workflow run**.
4. If paused on **Authorize AI to draft a plan** → **Provide inputs** → **Yes — generate draft plan with AI**.
5. Confirm a `cloud_resource_request` exists with **implementation plan** and **architecture** filled in.

### B — Production path

Same as A but **Environment: Production**. Confirm the run hits the production branch (Slack only works if secrets exist).

### C — Backup entity (optional)

If the facilitator wants a **static** request without waiting for AI, import this entity on blueprint `cloud_resource_request` (import / API / UI—whatever my Port exposes). Copy **only** the JSON between the two delimiter lines of **five** backticks (do not paste the backtick lines themselves).

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

**Done when:** I have seen staging behavior and production branch behavior (or the facilitator signs off).

Optional talk track: I can open `step-4-demo-flow/README.md` in the workshop repo if I have it—otherwise ignore.
