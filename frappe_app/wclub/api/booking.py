import frappe
@frappe.whitelist()
def create(member: str, session: str, coupon: str | None = None):
    sess = frappe.get_doc("Class Session", session)
    if sess.capacity and int(sess.capacity) > 0:
        current = len(sess.get("attendance") or [])
        if current >= int(sess.capacity):
            frappe.throw("Session is full")
    doc = frappe.get_doc({
        "doctype": "Booking",
        "member": member,
        "session": session,
        "status": "Booked",
        "coupon": coupon
    }).insert(ignore_permissions=True)
    return {"name": doc.name}
