import frappe
from frappe.utils import now_datetime
@frappe.whitelist(allow_guest=True)
def check_in(booking: str):
    doc = frappe.get_doc("Booking", booking)
    doc.status = "Checked-in"
    doc.save(ignore_permissions=True)
    sess = frappe.get_doc("Class Session", doc.session)
    sess.append("attendance", {"member": doc.member, "status": "Present", "check_in_time": now_datetime()})
    sess.save(ignore_permissions=True)
    return {"ok": True, "booking": doc.name}
