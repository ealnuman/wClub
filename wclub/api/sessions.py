import frappe
@frappe.whitelist()
def list_available(limit: int = 50):
	return []
