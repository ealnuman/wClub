from frappe import _
def get_data():
    return [{
        "label": _("wClub"),
        "icon": "octicon octicon-person",
        "items": [
            {"type": "doctype", "name": "Club"},
            {"type": "doctype", "name": "Membership Plan"},
            {"type": "doctype", "name": "Member"},
            {"type": "doctype", "name": "Coach"},
            {"type": "doctype", "name": "Class"},
            {"type": "doctype", "name": "Session"},
            {"type": "doctype", "name": "Attendance"},
            {"type": "doctype", "name": "Payment"},
            {"type": "doctype", "name": "Belt Rank"},
            {"type": "doctype", "name": "Belt Upgrade"},
            {"type": "doctype", "name": "Offer"},
            {"type": "doctype", "name": "Coupon"},
            {"type": "report", "is_query_report": False, "name": "Belt Distribution", "doctype": "Member"},
            {"type": "report", "is_query_report": False, "name": "Upcoming Belt Promotions", "doctype": "Member"},
        ]
    }]
