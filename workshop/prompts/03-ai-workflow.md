You are helping me install the **AI workflow** for the PlatformCon-Carne workshop in Port.

**Goal:** The workflow in `step-3-ai-workflow/workflow.json` is **published** and **connected** to the same self-service action from step 2 (identifier in JSON: **`request_cloud_resource`**). After this step, submitting the form should start a workflow run.

**Source of truth:** Import from repo root:

- `step-3-ai-workflow/workflow.json`

**Typical Port UI path:** **Settings** → **Workflows** → **Import** (or Builder → Workflows, depending on version) → upload or paste the JSON.

**Important notes for facilitators and attendees:**

- **Workflows may be beta** in some organizations. If import is disabled, say so clearly and tell me what to ask my org admin to enable.
- This workflow includes an **INPUT** node (`human_gate_before_plan`) for early human-in-the-loop testing: after service context is fetched, a responder must **Proceed with AI plan** or **Stop run** before AI nodes run.
- **Slack** steps need secrets (`SLACK_BOT_TOKEN`, `SLACK_PLATFORM_CHANNEL`) if those nodes should succeed; other parts can still run for a demo.

**Done when:**

1. Workflow `request_cloud_resource` (or the title **Create a new resource**) appears as published.
2. The self-service action trigger is still the entry point (re-importing may replace the same identifier — that is expected in this workshop).

**Port API note:** Internal Port API calls in the JSON may use `api.getport.io`; your facilitator may use EU or other regions — ask if webhook URLs need swapping for your tenant.

After import, walk me through **one** dry run: where to open the run timeline and what “waiting for input” looks like for the INPUT node.
