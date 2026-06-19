You are helping me create the **self-service action** for the PlatformCon-Carne workshop in Port.

**Who this is for:** New Port users. Copy the JSON below and paste it into **Settings → Self-service → Actions → Import** (wording may vary). You do not have my disk; everything needed is **in this message**.

**Goal:** Action **Create a new resource** appears under Self-Service. Form: infrastructure type, resource types (cloud vs on-prem), environment, **service** entity picker (`service` blueprint), additional context.

---

## Action + trigger JSON (copy all of this)

```json
{
  "identifier": "request_cloud_resource",
  "title": "Create a new resource",
  "icon": "Server",
  "description": "Request a new cloud or on-premise resource with AI-generated implementation plan",
  "nodes": [
    {
      "identifier": "trigger",
      "title": "Request Cloud Resource",
      "icon": "Cloud",
      "config": {
        "type": "SELF_SERVE_TRIGGER",
        "userInputs": {
          "properties": {
            "infrastructure_type": {
              "title": "Infrastructure",
              "type": "string",
              "default": "Cloud",
              "enum": ["Cloud", "On-Premise"],
              "enumColors": {
                "Cloud": "turquoise",
                "On-Premise": "purple"
              }
            },
            "cloud_resource_type": {
              "title": "Resource Type",
              "type": "string",
              "default": "RDS Database",
              "visible": {
                "jqQuery": ".form.infrastructure_type == \"Cloud\""
              },
              "enum": ["RDS Database", "S3 Bucket", "EC2 Instance", "EKS Cluster", "ElastiCache"]
            },
            "onprem_resource_type": {
              "title": "Resource Type",
              "type": "string",
              "default": "Virtual Machine",
              "visible": {
                "jqQuery": ".form.infrastructure_type == \"On-Premise\""
              },
              "enum": ["Virtual Machine", "Virtual Disk", "Kubernetes Namespace"]
            },
            "environment": {
              "title": "Environment",
              "type": "string",
              "default": "Staging",
              "enum": ["Development", "Staging", "Production"],
              "enumColors": {
                "Development": "green",
                "Staging": "yellow",
                "Production": "red"
              }
            },
            "service": {
              "title": "Service",
              "type": "string",
              "format": "entity",
              "blueprint": "service"
            },
            "additional_context": {
              "title": "Additional Requirements",
              "description": "Describe any special requirements",
              "type": "string",
              "default": "Standard configuration with automated backups enabled"
            }
          },
          "required": ["infrastructure_type", "environment", "service"],
          "order": [
            "infrastructure_type",
            "cloud_resource_type",
            "onprem_resource_type",
            "environment",
            "service",
            "additional_context"
          ]
        },
        "actionCardButtonText": "Submit",
        "executeActionButtonText": "Submit Request",
        "published": true
      }
    }
  ],
  "connections": []
}
```

**After import, check:** Cloud vs On-Premise toggles resource type options; **Service** is an entity field on blueprint `service`; environments include Development / Staging / Production.

**Done when:** I can open Self-Service and the form loads with no error.
