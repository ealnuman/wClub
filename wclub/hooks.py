app_name = "wclub"
app_title = "wClub"
app_publisher = "Taqrieb Information Technology Company"
app_description = "wClub — Multi-tenant fighting club management for Frappe v15+"
app_email = "support@taqrieb.com"
app_license = "MIT"
app_version = "1.0.0"

after_install = "wclub.after_install.run"
app_logo = "/assets/wclub/images/logo.svg"

doc_events = {
    "Belt Upgrade": {
        "on_submit": "wclub.belt_upgrade.on_submit"
    }
}
