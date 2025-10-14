import frappe

def execute():
    if not frappe.db.exists('Member', {'first_name':'Demo Member'}):
        m = frappe.get_doc({'doctype':'Member','first_name':'Demo Member','belt':'White'})
        m.insert(ignore_permissions=True)
        frappe.db.commit()
