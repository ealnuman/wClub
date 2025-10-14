import frappe
@frappe.whitelist()
def save(club_name: str, timezone: str = "Asia/Riyadh", load_demo: int = 1):
    if not frappe.db.exists("Club", club_name):
        frappe.get_doc({"doctype":"Club","name":club_name,"code":club_name[:8].upper(),"timezone":timezone}).insert(ignore_permissions=True)
    if int(load_demo):
        from wclub.wclub.patches.v1.initial_seed import execute as seed
        seed()
    return {"ok": True, "club": club_name}
