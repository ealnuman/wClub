import frappe
@frappe.whitelist()
def cancel(booking: str):
    doc = frappe.get_doc("Booking", booking)
    doc.status = "Cancelled"
    doc.save(ignore_permissions=True)
    return {"ok": True, "booking": doc.name}
