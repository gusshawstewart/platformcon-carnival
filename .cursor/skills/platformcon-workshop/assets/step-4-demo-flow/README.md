# Step 4 — Live Demo Flow

## Setup Before You Go On Stage

- [ ] Port open in browser, logged in as your demo account
- [ ] Slack open, `#platform-requests` channel visible
- [ ] Cursor open with this repo, Port MCP connected and authenticated
- [ ] Run 1 test submission the night before to confirm the workflow executes cleanly
- [ ] Have `backup-entity.json` ready to import if the AI node is slow

---

## The Opening Line

> "Meet Marco Ribs. He's a developer on the payments team at PlatformCon-Carne. He needs an RDS database in staging. Until today, he'd open a Jira ticket and wait 3 days. Let's be Marco."

---

## Demo Run 1 — Non-Production (the satisfying one)

### Navigate to Self-Service

Go to: `app.getport.io` → Self-Service → "Create a new resource"

> "This is what Marco sees. No ticket. No Slack message. A form."

### Fill in the form

| Field | Value |
|-------|-------|
| Infrastructure | Cloud |
| Resource Type | RDS Database |
| Environment | **Staging** |
| Service | payments-service |
| Additional Requirements | Standard configuration with automated backups enabled |

> "He picks his service from the catalog — Port knows it's a Gold-tier service. That context is about to matter."

### Submit

Click "Submit Request"

> "The workflow starts. First it fetches the service context — tier, language, owner. Then it branches: this is Cloud, so it goes to the cloud AI node."

### While the AI node runs (~15–30 seconds)

> "The AI is searching GitHub right now for existing Terraform modules that match RDS PostgreSQL. It knows this is a Gold service — so it'll spec Multi-AZ, appropriate instance sizing. It's not generating a generic plan — it's generating *Marco's* plan."

### Show the completed request entity

Navigate to the new `cloud_resource_request` entity.

- **Overview tab:** Status = Approved, linked to payments-service
- **Implementation Plan tab:** Show the Terraform steps
- **Architecture tab:** Show the Mermaid diagram rendering

> "Marco doesn't need to wait for anyone. His request is in the catalog. The plan is here. The architecture is here. Auditable, searchable, linkable."

### Show Slack

Switch to Slack, `#platform-requests`

> "The Pit Crew gets a notification — not because they need to do anything for staging, but because they have visibility. One click to the PR, one click to the plan, one click to the resource."

### Show the Cloud Resource entity

Navigate to the new `cloudResource` entity — linked to payments-service.

> "And here's the resource itself in the catalog. No more spreadsheet. Port knows this RDS instance exists, what environment it's in, which service owns it."

---

## Demo Run 2 — Production (the dramatic one)

> "Now Marco needs this in production. Same form, one change."

Change Environment to **Production**, resubmit.

> "Different branch. Production goes to human approval."

Show the Slack approval message with the "View Request & Approve" button.

> "The Pit Crew gets an approval request — not a Jira notification, not an email. A Slack message with the full context and one button. The policy is in the workflow. The human makes the decision."

---

## Closing Line

> "Three days to 60 seconds. The Pit Crew didn't write any code. Marco didn't open a ticket. The AI generated the plan using their actual service context and their actual Terraform modules. Port tracked everything — the request, the plan, the approval, the resource. That's what an agentic platform looks like. Any questions?"

---

## Backup: Pre-completed entity

If the AI node times out or runs slow during the demo, import `backup-entity.json` via Port UI to show a completed request with plan and architecture already populated.

Navigate to: Port → cloud_resource_request → Import Entity
