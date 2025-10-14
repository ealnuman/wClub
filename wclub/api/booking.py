import frappe

@frappe.whitelist()
def create(member, session, coupon=None):
    return {"ok": True}
