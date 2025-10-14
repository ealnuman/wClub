import frappe

def test_install_and_fixtures():
    for dt in ['Member','Class Session','Booking']:
        assert frappe.get_meta(dt)
    wfs=[w.workflow_name for w in frappe.get_all('Workflow', filters={'is_active':1})]
    assert 'Booking Workflow' in wfs
    assert frappe.get_all('Workspace', filters={'label':'wClub Dashboard'})
