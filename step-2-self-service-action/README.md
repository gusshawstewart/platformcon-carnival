# Step 2 — Self-Service Action

## What We're Building

The form that replaces the Jira ticket.

A self-service action called **"Create a new resource"** that lets any developer request a cloud or on-premise resource directly from Port.

## Key Form Features

- **Conditional fields** — pick Cloud, see cloud resource types; pick On-Premise, see VM types
- **Service picker** — shows real entities from the catalog (not a free-text field)
- **Environment colour coding** — green (dev), yellow (staging), red (production)
- **Additional context** — free text for special requirements

## What Happens When Submitted

The form triggers the workflow in Step 3. Nothing happens visually yet — that's the next step.

## Time

~10 minutes

## Fallback

Import `workflow.json` via Port UI:
- Settings → Workflows → Import
