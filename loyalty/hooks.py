# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "loyalty"
app_title = "Frappe Omnichannel Loyalty Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Omnichannel Loyalty Engine - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/loyalty/css/loyalty.bundle.css"
app_include_js = "/assets/loyalty/js/loyalty.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe Omnichannel Loyalty Engine Entry": {
        "validate": "loyalty.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "loyalty.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "loyalty.tasks.hourly_sync"
    ],
    "daily": [
        "loyalty.tasks.daily_reconciliation"
    ],
    "weekly": [
        "loyalty.tasks.weekly_digest"
    ]
}
