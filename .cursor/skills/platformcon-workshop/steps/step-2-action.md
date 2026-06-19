# Step 2 — Self-Service Action

Create the form that replaces Jira tickets.

## Action

```
upsert_action
```

Read the full payload from: `.cursor/skills/platformcon-workshop/assets/step-2-self-service-action/workflow.json`

Do not modify the JSON unless the user asks to customize.

## Key form behavior

- Cloud vs On-Premise shows different resource type options
- Service field is an entity picker from the catalog
- Environment is colour-coded (dev/staging/prod)

## Done when

"Create a new resource" action appears in Port Self-Service.

## Fallback

Port UI → Settings → Actions → Import — use `.cursor/skills/platformcon-workshop/assets/step-2-self-service-action/workflow.json`.
