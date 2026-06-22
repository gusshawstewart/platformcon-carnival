# Step 4 — Port skill (trigger resource workflow)

Attendees create a **Port skill** per [Port skills docs](https://docs.port.io/ai-interfaces/skills/). The skill's **only job** is to call workflow **`request_cloud_resource`** via **`trigger_workflow_run`**.

## Source layout

```
step-4-port-skill/
├── skill-blueprint.json
├── skill-entity.json             # Generated
└── platformcon-carne-request-resource/
    └── SKILL.md
```

```bash
python3 workshop/scripts/sync-prompt-embeds.py
```

## Attendee flow

1. Import blueprint **`skill`** (skip if it exists).
2. Create entity **`platformcon-carne-request-resource`** from `skill-entity.json`.
3. **Port AI chat:** *"Request a cloud resource for the PlatformCon-Carne workshop."*
4. Port AI loads the skill and triggers **`request_cloud_resource`**.

## Cursor + Port MCP

1. `upsert_blueprint` → `skill-blueprint.json`
2. `upsert_entity` → `skill-entity.json`
3. User asks in Port AI (or `load_skill` + `trigger_workflow_run` in Cursor)
