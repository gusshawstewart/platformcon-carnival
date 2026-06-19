You are helping me **verify** the PlatformCon-Carne workshop setup end-to-end in Port.

**Prerequisites:** Steps 0–3 complete (branding, catalog, action, workflow published).

---

### A — Staging path (auto-approved branch)

1. Open **Self-Service** → **Create a new resource** (or the workshop action title).
2. Fill the form:
   - **Infrastructure:** Cloud  
   - **Resource type:** RDS Database  
   - **Environment:** Staging  
   - **Service:** `payments-service`  
   - **Additional requirements:** `Standard configuration with automated backups enabled`
3. **Submit** and open the **workflow run**.
4. If the run pauses on **Confirm AI plan generation (HITL preview)** — open **Provide inputs**, then choose **Proceed with AI plan**.
5. **Verify:** A `cloud_resource_request` entity exists with **implementation plan** and **architecture** populated (check entity page tabs if present).
6. **Slack:** If configured, confirm an auto-approve style notification arrived.

---

### B — Production path (approval branch)

Repeat the same form with **Environment: Production**.

**Verify:** Slack (if secrets exist) shows an **approval / review** style message with links back to the request in Port. If Slack is not configured, confirm the workflow branch still reached the production path (run graph / node status).

---

### C — Backup if AI is slow

If the facilitator asks for a static example entity, import **`step-4-demo-flow/backup-entity.json`** via the Port UI (Builder → appropriate blueprint → import entity, or equivalent).

---

**Done when:** I have personally seen both **staging** and **production** behavior (or the facilitator has signed off with the same checklist).

Optional presenter narrative: see `step-4-demo-flow/README.md` in the repo.
