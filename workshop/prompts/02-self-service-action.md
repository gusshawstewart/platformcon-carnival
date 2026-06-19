You are helping me create the **self-service action** for the PlatformCon-Carne workshop in Port.

**Goal:** A self-service action titled like **“Create a new resource”** exists and appears under **Self-Service** (or your org’s equivalent hub). The form should ask for infrastructure type, resource type (cloud vs on-prem branches), environment, service (entity picker on blueprint `service`), and additional context.

**Source of truth (do not invent fields):** Import the action from this repo file at the **repo root**:

- `step-2-self-service-action/workflow.json`

**Typical Port UI path:** **Settings** → **Self-service** → **Actions** → **Import** (wording may vary) → select or paste `workflow.json`.

**Key behaviors to verify after import:**

- **Cloud** vs **On-Premise** toggles which resource type enum is shown.
- **Service** is an **entity** field on blueprint **`service`**.
- Environments include Development / Staging / Production with sensible defaults.

**Done when:** I can open Self-Service and run **Create a new resource** (the form opens without error).

If the import UI expects a different shape, compare against Port’s current “import action” docs and list what changed.
