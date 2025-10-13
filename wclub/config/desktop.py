from frappe import _
def get_data():
    return [{
        "label": _("wClub"),
        "items": [
            {"type": "doctype", "name": "Member", "label": _("Members")},
            {"type": "doctype", "name": "Booking"},
            {"type": "doctype", "name": "Class Session"},
            {"type": "doctype", "name": "Promotion Exam"},
            {"type": "report", "is_query_report": 1, "name": "Class Utilization", "doctype": "Class Session"},
        ]
    }]
