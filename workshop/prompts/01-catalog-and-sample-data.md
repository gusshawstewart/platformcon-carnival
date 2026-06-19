You are helping me build the **catalog foundation** for the PlatformCon-Carne workshop in Port.

**Goal:** Three blueprints exist — `service`, `cloud_resource_request`, `cloudResource` — plus **six** `service` entities from sample data.

**I have this Git repository open** with the following JSON files at the **repo root** (paths relative to repo root):

### Blueprints (import each via Port Builder)

1. `step-1-catalog-foundation/service.json` — blueprint identifier **`service`**. The `tier` property (Gold / Silver / Bronze) is used later for AI sizing hints.
2. `step-1-catalog-foundation/cloud_resource_request.json` — **`cloud_resource_request`**
3. `step-1-catalog-foundation/cloudResource.json` — **`cloudResource`**

**Typical Port UI path:** **Builder** → **Blueprints** → **+ New** / **Import** (or **Import blueprint**) → paste JSON or upload file.

### Sample entities

4. After blueprints exist, create the catalog services from `sample-data/services.json`.  
   If Port only supports one entity at a time, create these six identifiers (titles and properties must match the JSON):  
   `payments-service`, `order-management`, `menu-catalog`, `delivery-tracking`, `user-profiles`, `notification-service`

**Done when:**

- All three blueprints appear in Builder.
- All six services exist and are visible in the **service** catalog.

**If something fails:** Tell me the exact Port error string and which file failed, and suggest the smallest fix (usually a property name or relation mismatch).
