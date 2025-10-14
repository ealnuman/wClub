app_name = "wclub"
app_title = "wClub"
app_publisher = "Taqrieb Information Technology Company"
app_description = "Fighting club & dojo management for Frappe"
app_email = "support@taqrieb.com"
app_license = "Taqrieb Proprietary License"
app_logo_url = "/assets/wclub/logo_light.png"
website_context = {
  "favicon": "/assets/wclub/favicon_light.png",
  "splash_image": "/assets/wclub/banner_light.jpg",
  "brand_html": '<img id="logo" src="/assets/wclub/logo_light.png" alt="wClub" height="28">'
}
fixtures = ["Workspace",
  {"doctype":"Role","filters":[["role_name","in",["Organization Admin","Club Admin","Coach","Front Desk","Accountant","Member","Parent"]]]},
  "Workflow","Email Template","Report","Dashboard Chart","Notification"]
website_route_rules = [
  {"from_route":"/portal/my-bookings","to_route":"portal/my-bookings"},
  {"from_route":"/portal/book","to_route":"portal/book"},
  {"from_route":"/portal/cancel-booking","to_route":"portal/cancel-booking"},
  {"from_route":"/portal/certificates","to_route":"portal/certificates"},
  {"from_route":"/coach/dashboard","to_route":"coach/dashboard"},
  {"from_route":"/kiosk/checkin","to_route":"kiosk/checkin"},
  {"from_route":"/setup","to_route":"setup/index"},
  {"from_route":"/help","to_route":"help/index"},
  {"from_route":"/docs","to_route":"docs/index"}
]
def after_install():
    import frappe
    frappe.msgprint("✅ wClub v1.1.0 installed. Visit /setup to configure your club. Demo data is loaded.")
