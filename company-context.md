# PlatformCon-Carne — Company Context

## The Company

**PlatformCon-Carne** is a fast-growing food delivery platform specialising in premium meat and BBQ delivery across Europe. Founded in 2019, they've scaled from a single city to 14 countries in 5 years.

Engineering headcount: ~120 developers, 4 platform engineers.

## The Platform Team

The platform team is called **The Pit Crew** (yes, they lean into the BBQ theme).

Members:
- **Alex Brasero** — Platform Lead (that's you, presenting today)
- **Sam Chimichurri** — SRE
- **Jordan Asado** — Infrastructure
- **Priya Smoke** — Developer Experience

## The Problem

PlatformCon-Carne's developers open Jira tickets every time they need a cloud resource. The Pit Crew handles ~15 resource requests per week.

A typical request looks like:
> *"Hey, I need an RDS PostgreSQL instance for the payments service in staging. Standard config, automated backups. Thanks"*

The Pit Crew then:
1. Checks what environment the service runs in
2. Checks what tier the service is (Gold? Silver?) to size the instance correctly
3. Looks up if there's an existing Terraform module for this
4. Provisions it manually or writes the Terraform
5. Updates a spreadsheet (yes, a spreadsheet) with what exists where
6. Replies to the Jira ticket

Average time: **3 days**. Developer frustration: **high**. Spreadsheet accuracy: **questionable**.

## The Services

| Service | Tier | Owner | Language |
|---------|------|-------|----------|
| payments-service | Gold | payments-team | Go |
| order-management | Gold | orders-team | Python |
| menu-catalog | Silver | catalog-team | Node.js |
| delivery-tracking | Silver | logistics-team | Go |
| user-profiles | Bronze | platform-team | Python |
| notification-service | Bronze | platform-team | Node.js |

## Today's Demo Scenario

**Developer:** Marco Ribs from the payments team  
**Request:** RDS PostgreSQL database for `payments-service` in staging  
**Requirements:** Standard config, automated backups  
**Expected outcome:** Auto-approved (non-production), PR opened, Slack notification with implementation plan and architecture diagram

Marco should go from "I need a database" to "here's your PR and your resource is being tracked in Port" in under 60 seconds.

## The Terraform Repo

`github.com/platformcon-carne/terraform-modules` — contains standard modules for RDS, S3, EC2, EKS, ElastiCache, and on-premise resources.

## The Slack Channel

`#platform-requests` — where all resource request notifications land.
