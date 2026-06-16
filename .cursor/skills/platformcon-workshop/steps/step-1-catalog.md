# Step 1 — Catalog Foundation

Create three blueprints, then load sample service entities. The catalog is the AI's world model.

## 1a — `service` blueprint

```
upsert_blueprint
```

Read payload from: `step-1-catalog-foundation/service.json`

The `tier` property drives AI sizing — Gold services get production-grade resources.

## 1b — `cloud_resource_request` blueprint

```
upsert_blueprint
```

Read payload from: `step-1-catalog-foundation/cloud_resource_request.json`

## 1c — `cloudResource` blueprint

```
upsert_blueprint
```

Read payload from: `step-1-catalog-foundation/cloudResource.json`

## 1d — Sample services

```
upsert_entity
```

Read entities from: `sample-data/services.json` (6 services)

Identifiers: `payments-service`, `order-management`, `menu-catalog`, `delivery-tracking`, `user-profiles`, `notification-service`

## Done when

All three blueprints exist and all six service entities are in the catalog.

## Fallback

Port UI → Builder → Import Blueprint — use the JSON files in `step-1-catalog-foundation/`.

For entities: import from `sample-data/services.json`.
