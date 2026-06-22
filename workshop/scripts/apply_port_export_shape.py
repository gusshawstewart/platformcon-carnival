#!/usr/bin/env python3
"""Align workflow.json under the Cursor skill assets with a Port UI export (shape + ordering)."""

from __future__ import annotations

import json
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WF = (
    ROOT
    / ".cursor"
    / "skills"
    / "platformcon-workshop"
    / "assets"
    / "step-3-ai-workflow"
    / "workflow.json"
)


def main() -> None:
    data = json.loads(WF.read_text())

    # Preserve Slack mrkdwn template (escaped JQ) from current file before restructuring bodies
    hitl_mrkdwn = None
    for n in data["nodes"]:
        if n["identifier"] == "slack_hitl_gate_stopped":
            for blk in n["config"]["body"]["blocks"]:
                if blk.get("type") == "section" and isinstance(blk.get("text"), dict):
                    hitl_mrkdwn = blk["text"]["text"]
            break
    assert hitl_mrkdwn is not None

    data["category"] = None

    nodes = data["nodes"]

    # fetch_service_context → api.port.io + Port API auth
    for n in nodes:
        if n["identifier"] == "fetch_service_context":
            n["config"]["url"] = (
                "https://api.port.io/v1/blueprints/service/entities/{{ .outputs[\"trigger\"].service }}"
            )
            n["config"]["headers"] = {
                "Authorization": "Bearer {{ .secrets.PORT_CLIENT_SECRET }}"
            }
            vars_ = n["variables"]
            vars_["service_tier"] = "{{ .result.response.entity.properties.tier }}"
            vars_["service_title"] = "{{ .result.response.entity.title }}"

    # Move slack_hitl_gate_stopped to immediately after open_pr_with_coding_agent (Port export order)
    slack_hitl = next(n for n in nodes if n["identifier"] == "slack_hitl_gate_stopped")
    nodes = [n for n in nodes if n["identifier"] != "slack_hitl_gate_stopped"]
    idx = next(i for i, n in enumerate(nodes) if n["identifier"] == "open_pr_with_coding_agent")
    nodes.insert(idx + 1, slack_hitl)
    data["nodes"] = nodes

    # Trigger: null title/icon/description; property key order like Port export
    tr = next(n for n in data["nodes"] if n["identifier"] == "trigger")
    props = tr["config"]["userInputs"]["properties"]
    order = [
        "service",
        "environment",
        "additional_context",
        "cloud_resource_type",
        "infrastructure_type",
        "onprem_resource_type",
    ]
    tr["config"]["userInputs"]["properties"] = OrderedDict((k, props[k]) for k in order)
    tr["title"] = None
    tr["icon"] = None
    tr["description"] = None

    # create_request mapping.properties order (Port export)
    cr = next(n for n in data["nodes"] if n["identifier"] == "create_request")
    m = cr["config"]["mapping"]["properties"]
    order_cr = [
        "status",
        "environment",
        "architecture",
        "requested_at",
        "resource_type",
        "additional_context",
        "implementation_plan",
        "infrastructure_type",
    ]
    cr["config"]["mapping"]["properties"] = OrderedDict((k, m[k]) for k in order_cr)

    # update_cloud_resource_in_port properties order (Port export)
    uc = next(n for n in data["nodes"] if n["identifier"] == "update_cloud_resource_in_port")
    mp = uc["config"]["mapping"]["properties"]
    order_u = ["kind", "link", "region", "status", "environment"]
    uc["config"]["mapping"]["properties"] = OrderedDict((k, mp[k]) for k in order_u)

    # AI nodes: expanded outputSchema shape (multiline-style objects)
    for aid in ("ai_generate_plan_cloud", "ai_generate_plan_onprem"):
        ai = next(n for n in data["nodes"] if n["identifier"] == aid)
        sch = ai["config"]["outputSchema"]
        sch["properties"] = {
            "architecture": {"type": "string"},
            "implementation_plan": {"type": "string"},
        }

    # Slack bodies: top-level text + blocks + channel last (Port export)
    approve = next(n for n in data["nodes"] if n["identifier"] == "slack_approval_request")
    b = approve["config"]["body"]
    ch = b["channel"]
    approve["config"]["body"] = {
        "text": b["text"],
        "blocks": b["blocks"],
        "channel": ch,
    }
    # header block: text object before type (Port export key order)
    hdr = approve["config"]["body"]["blocks"][0]
    if hdr.get("type") == "header" and "text" in hdr:
        t = hdr["text"]
        approve["config"]["body"]["blocks"][0] = {"text": t, "type": "header"}

    hitl = next(n for n in data["nodes"] if n["identifier"] == "slack_hitl_gate_stopped")
    hitl["config"]["body"] = {
        "text": "Resource request — stopped before AI plan (human gate)",
        "blocks": [
            {
                "text": {
                    "text": hitl_mrkdwn,
                    "type": "mrkdwn",
                },
                "type": "section",
            }
        ],
        "channel": "{{ .secrets.SLACK_PLATFORM_CHANNEL }}",
    }

    nonp = next(n for n in data["nodes"] if n["identifier"] == "slack_nonprod_notification")
    bn = nonp["config"]["body"]
    chn = bn["channel"]
    nonp["config"]["body"] = {"text": bn["text"], "blocks": bn["blocks"], "channel": chn}
    h2 = nonp["config"]["body"]["blocks"][0]
    if h2.get("type") == "header" and "text" in h2:
        t2 = h2["text"]
        nonp["config"]["body"]["blocks"][0] = {"text": t2, "type": "header"}

    # actions blocks: Port export uses url / text / type / style order on buttons — normalize buttons in slack_nonprod
    actions = nonp["config"]["body"]["blocks"][-1]
    if actions.get("type") == "actions":
        new_elements = []
        for el in actions["elements"]:
            if el.get("type") != "button":
                new_elements.append(el)
                continue
            nb = OrderedDict()
            if "url" in el:
                nb["url"] = el["url"]
            nb["text"] = el["text"]
            nb["type"] = el["type"]
            if "style" in el:
                nb["style"] = el["style"]
            new_elements.append(dict(nb))
        actions["elements"] = new_elements

    # actions in slack_approval
    act2 = approve["config"]["body"]["blocks"][-1]
    if act2.get("type") == "actions":
        new_el2 = []
        for el in act2["elements"]:
            if el.get("type") != "button":
                new_el2.append(el)
                continue
            nb = OrderedDict()
            if "url" in el:
                nb["url"] = el["url"]
            nb["text"] = el["text"]
            nb["type"] = el["type"]
            if "style" in el:
                nb["style"] = el["style"]
            new_el2.append(dict(nb))
        act2["elements"] = new_el2

    # Every node: description, links, verbose (Port export)
    for n in data["nodes"]:
        n["description"] = None
        n["links"] = []
        n["verbose"] = False

    # Connections: description null on each edge
    for c in data["connections"]:
        c["description"] = None

    # Root key order like Port export (category after description)
    data = OrderedDict(
        [
            ("identifier", data["identifier"]),
            ("title", data["title"]),
            ("icon", data["icon"]),
            ("description", data["description"]),
            ("category", data.get("category")),
            ("allowAnyoneToViewRuns", data["allowAnyoneToViewRuns"]),
            ("nodes", data["nodes"]),
            ("connections", data["connections"]),
        ]
    )

    WF.write_text(json.dumps(data, indent=2) + "\n")
    print("Updated", WF)


if __name__ == "__main__":
    main()
