---
name: platformcon-carne-request-resource
description: >-
  Run the PlatformCon-Carne "Create a new resource" workflow. Use when the user
  asks to request a cloud resource, create infrastructure, run step 4, or
  trigger the resource creation workflow.
metadata:
  title: PlatformCon-Carne — Request resource
---

# Request a cloud resource

Your only job is to start the **`request_cloud_resource`** workflow using **`trigger_workflow_run`**.

## Inputs

Use values the user provided. If they did not specify, use these workshop defaults:

- `infrastructure_type`: `Cloud`
- `cloud_resource_type`: `RDS Database`
- `environment`: `Staging`
- `service`: `payments-service` (entity identifier on blueprint `service`)
- `additional_context`: `Standard configuration with automated backups enabled`

Required trigger fields: `infrastructure_type`, `environment`, `service`.

## Steps

1. Call **`trigger_workflow_run`** with:
   - `identifier`: `request_cloud_resource`
   - `inputs`: the object above (include `cloud_resource_type` when infrastructure is Cloud)

2. Return the workflow **run identifier** and current status.

3. Optionally poll **`get_workflow_run`** until the run completes or waits for user input.

Do not walk the user through Self-Service UI clicks. Do not import sample entities. Do not smoke-test manually — trigger the workflow and report the result.
