import frappe
@frappe.whitelist()
def list_available(limit: int = 50):
    return frappe.db.sql("""
SELECT name, class_type, dojo, start, end, capacity
FROM `tabClass Session`
WHERE start >= NOW()
ORDER BY start ASC
LIMIT %s
""", (limit,), as_dict=True)
