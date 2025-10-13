import frappe
from frappe.utils import add_days, nowdate
import datetime

def execute():
    def ensure(doctype, name, **kwargs):
        if frappe.db.exists(doctype, name):
            return frappe.get_doc(doctype, name)
        doc = frappe.get_doc({"doctype": doctype, "name": name, **kwargs})
        doc.insert(ignore_permissions=True)
        return doc

    bs = ensure("Belt System", "Default Karate", title="Default Karate")
    ensure("Belt Level", "White", belt_system=bs.name, order=1, color="White", min_weeks_since_last=0)
    ensure("Belt Level", "Yellow", belt_system=bs.name, order=2, color="Yellow", min_weeks_since_last=6)

    club = ensure("Club", "Demo Club", code="DEMO", timezone="Asia/Riyadh")
    dojo = ensure("Dojo", "Main Dojo", club=club.name, capacity=20, address="HQ")

    ct1 = ensure("Class Type", "Kids Beginner", title="Kids Beginner")
    ct2 = ensure("Class Type", "Adults Beginner", title="Adults Beginner")

    ensure("Member", "member1", first_name="Ali", last_name="Saud", email="member1@example.com", club=club.name)
    ensure("Member", "member2", first_name="Noura", last_name="Faisal", email="member2@example.com", club=club.name)

    base_date = add_days(nowdate(), 1)
    def dt(h):
        return datetime.datetime.combine(datetime.date.fromisoformat(base_date), datetime.time(h, 0))

    for i, ct in enumerate([ct1.name, ct2.name], start=1):
        frappe.get_doc({
            "doctype": "Class Session",
            "class_type": ct,
            "dojo": dojo.name,
            "start": dt(17+i),
            "end": dt(18+i),
            "capacity": 15
        }).insert(ignore_permissions=True)
