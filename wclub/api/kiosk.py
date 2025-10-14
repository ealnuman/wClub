import frappe
@frappe.whitelist(allow_guest=True)
def check_in(booking):
	return {'ok': True}
