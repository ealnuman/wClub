import frappe

@frappe.whitelist()
def cancel(booking):
    return {"ok": True}
