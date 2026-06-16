# Step 4 — Test the Setup

Walk the user through verifying the platform works.

## Staging request (auto-approved)

1. Port → Self-Service → "Create a new resource"
2. Infrastructure: Cloud
3. Resource Type: RDS Database
4. Environment: **Staging**
5. Service: payments-service
6. Additional Requirements: "Standard configuration with automated backups enabled"
7. Submit and watch the workflow run
8. Verify the request entity has implementation plan and architecture diagram
9. Check Slack for auto-approve notification

## Production request (requires approval)

Repeat with Environment: **Production**. Verify Slack shows an approval request with Approve button.

## Backup

If the AI node is slow, import `step-4-demo-flow/backup-entity.json` via Port UI to show expected output.

## Demo script

For presenter notes, see `step-4-demo-flow/README.md`.

## Done when

User has seen both staging (auto-approve) and production (approval) paths work.
