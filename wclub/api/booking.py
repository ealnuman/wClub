import frappe
@frappe.whitelist()
def create(member: str, session: str):
    doc = frappe.get_doc({"doctype":"Booking","member":member,"session":session,"status":"Booked"}).insert(ignore_permissions=True)
    return {"name": doc.name}
