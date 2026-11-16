# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "loyalty"
app_title = "Frappe Omnichannel Loyalty Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Omnichannel Loyalty Engine for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/loyalty/css/loyalty.bundle.css"
app_include_js = "/assets/loyalty/js/loyalty.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "loyalty.engine.on_document_submit",
        "on_cancel": "loyalty.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "loyalty.engine.daily_scheduled_sync"
    ]
}
