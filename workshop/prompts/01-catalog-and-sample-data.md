You are helping me build the **catalog foundation** for the PlatformCon-Carne workshop in Port.

**Who this is for:** New Port users. You (Port AI) only see this chat. The JSON below is **included so I can copy it** into Port without hunting files on disk.

**What I will do in Port:** Use **Builder → Blueprints → Import** (or paste JSON), then create **service** entities from the sample list. For each numbered section, **select all the text inside that JSON box**, copy, and paste into Port’s import. If my Port version only has a visual blueprint editor, walk me field-by-field to match the JSON **exactly** (same property identifiers and enums).

---

## 1 — Blueprint `service`

**In Port:** Import this as one blueprint (identifier must stay `service`).

```json
{
  "identifier": "service",
  "title": "Service",
  "icon": "Microservice",
  "schema": {
    "properties": {
      "tier": {
        "title": "Service Tier",
        "type": "string",
        "enum": ["Gold", "Silver", "Bronze"],
        "enumColors": {
          "Gold": "yellow",
          "Silver": "lightGray",
          "Bronze": "orange"
        }
      },
      "language": {
        "title": "Language",
        "type": "string",
        "enum": ["Go", "Python", "Node.js", "Java"]
      },
      "owner_team": {
        "title": "Owner Team",
        "type": "string"
      },
      "repository_url": {
        "title": "Repository",
        "type": "string",
        "format": "url"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

---

## 2 — Blueprint `cloud_resource_request`

```json
{
  "identifier": "cloud_resource_request",
  "title": "Cloud Resource Request",
  "icon": "NewPage",
  "schema": {
    "properties": {
      "status": {
        "title": "Status",
        "type": "string",
        "enum": ["Pending Approval", "Approved", "Rejected", "Provisioning", "Provisioned"],
        "enumColors": {
          "Pending Approval": "yellow",
          "Approved": "blue",
          "Rejected": "red",
          "Provisioning": "turquoise",
          "Provisioned": "green"
        }
      },
      "resource_type": {
        "title": "Resource Type",
        "type": "string"
      },
      "environment": {
        "title": "Environment",
        "type": "string",
        "enum": ["Development", "Staging", "Production"],
        "enumColors": {
          "Development": "green",
          "Staging": "yellow",
          "Production": "red"
        }
      },
      "infrastructure_type": {
        "title": "Infrastructure",
        "type": "string",
        "enum": ["Cloud", "On-Premise"]
      },
      "implementation_plan": {
        "title": "Implementation Plan",
        "type": "string",
        "format": "markdown"
      },
      "architecture": {
        "title": "Architecture Diagram",
        "type": "string",
        "format": "markdown"
      },
      "requested_at": {
        "title": "Requested At",
        "type": "string",
        "format": "date-time"
      },
      "approved_at": {
        "title": "Approved At",
        "type": "string",
        "format": "date-time"
      },
      "approved_by": {
        "title": "Approved By",
        "type": "string"
      },
      "pr_url": {
        "title": "Terraform PR",
        "type": "string",
        "format": "url"
      },
      "additional_context": {
        "title": "Additional Requirements",
        "type": "string"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {
    "requested_by_service": {
      "title": "Requested By Service",
      "target": "service",
      "required": false,
      "many": false
    },
    "provisioned_resource": {
      "title": "Provisioned Resource",
      "target": "cloudResource",
      "required": false,
      "many": false
    }
  }
}
```

---

## 3 — Blueprint `cloudResource`

```json
{
  "identifier": "cloudResource",
  "title": "Cloud Resource",
  "icon": "Cloud",
  "schema": {
    "properties": {
      "kind": {
        "title": "Resource Kind",
        "type": "string"
      },
      "status": {
        "title": "Status",
        "type": "string",
        "enum": ["Provisioning", "Active", "Deprecated"],
        "enumColors": {
          "Provisioning": "yellow",
          "Active": "green",
          "Deprecated": "lightGray"
        }
      },
      "region": {
        "title": "Region",
        "type": "string"
      },
      "environment": {
        "title": "Environment",
        "type": "string"
      },
      "link": {
        "title": "Console Link",
        "type": "string",
        "format": "url"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {
    "used_by": {
      "title": "Used By Service",
      "target": "service",
      "required": false,
      "many": false
    }
  }
}
```

---

## 4 — Sample `service` entities

Create **six** entities on blueprint `service`. If Port has **bulk import / JSON paste**, use this array. Otherwise create each row manually using the same identifiers and properties.

```json
[
  {
    "identifier": "payments-service",
    "title": "Payments Service",
    "blueprint": "service",
    "properties": {
      "tier": "Gold",
      "language": "Go",
      "owner_team": "payments-team",
      "repository_url": "https://github.com/platformcon-carne/payments-service"
    }
  },
  {
    "identifier": "order-management",
    "title": "Order Management",
    "blueprint": "service",
    "properties": {
      "tier": "Gold",
      "language": "Python",
      "owner_team": "orders-team",
      "repository_url": "https://github.com/platformcon-carne/order-management"
    }
  },
  {
    "identifier": "menu-catalog",
    "title": "Menu Catalog",
    "blueprint": "service",
    "properties": {
      "tier": "Silver",
      "language": "Node.js",
      "owner_team": "catalog-team",
      "repository_url": "https://github.com/platformcon-carne/menu-catalog"
    }
  },
  {
    "identifier": "delivery-tracking",
    "title": "Delivery Tracking",
    "blueprint": "service",
    "properties": {
      "tier": "Silver",
      "language": "Go",
      "owner_team": "logistics-team",
      "repository_url": "https://github.com/platformcon-carne/delivery-tracking"
    }
  },
  {
    "identifier": "user-profiles",
    "title": "User Profiles",
    "blueprint": "service",
    "properties": {
      "tier": "Bronze",
      "language": "Python",
      "owner_team": "platform-team",
      "repository_url": "https://github.com/platformcon-carne/user-profiles"
    }
  },
  {
    "identifier": "notification-service",
    "title": "Notification Service",
    "blueprint": "service",
    "properties": {
      "tier": "Bronze",
      "language": "Node.js",
      "owner_team": "platform-team",
      "repository_url": "https://github.com/platformcon-carne/notification-service"
    }
  }
]
```

**Done when:** All three blueprints exist and all six services (`payments-service`, `order-management`, `menu-catalog`, `delivery-tracking`, `user-profiles`, `notification-service`) appear in the catalog.

**If something fails:** Explain the Port error in plain language and what to change (usually a typo in an identifier or a relation target).
