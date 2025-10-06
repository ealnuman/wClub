import frappe
def on_submit(doc, method):
    member = frappe.get_doc("Member", doc.member)
    member.current_belt = doc.new_belt
    member.save(ignore_permissions=True)
