import frappe
def test_wclub_setup():
    for dt in ["Member","Class Session","Booking","Promotion Exam"]:
        assert frappe.get_meta(dt)
    wfs = [w.workflow_name for w in frappe.get_all("Workflow", filters={"is_active":1})]
    for wf in ["Booking Workflow","Class Session Workflow","Promotion Exam Workflow"]:
        assert wf in wfs
    reports = [r.report_name for r in frappe.get_all("Report")]
    for r in ["Class Utilization","Daily Booking & Check-in","Belt Distribution","Attendance Heatmap (Summary)","Member List by Belt","Revenue Summary (by Class Type)"]:
        assert r in reports
    charts = [c.chart_name for c in frappe.get_all("Dashboard Chart")]
    for c in ["Members by Belt Level","Session Utilization","Monthly Revenue"]:
        assert c in charts
    notifs = [n.subject for n in frappe.get_all("Notification")]
    for s in ["New Booking","Booking Cancelled","Promotion Result"]:
        assert s in notifs
    assert frappe.get_all("Workspace", filters={"label":"wClub Dashboard"})
