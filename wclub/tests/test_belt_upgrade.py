import frappe
import unittest

class TestBeltUpgrade(unittest.TestCase):
    def test_belt_upgrade_updates_member(self):
        # Create belt ranks
        white = frappe.get_doc({"doctype":"Belt Rank","belt_name":"White","club":"Demo Fighting Club"}).insert(ignore_permissions=True)
        blue = frappe.get_doc({"doctype":"Belt Rank","belt_name":"Blue","club":"Demo Fighting Club"}).insert(ignore_permissions=True)
        # Create member
        member = frappe.get_doc({"doctype":"Member","first_name":"Ali","club":"Demo Fighting Club","current_belt":white.name}).insert(ignore_permissions=True)
        # Submit belt upgrade
        upgrade = frappe.get_doc({"doctype":"Belt Upgrade","member":member.name,"new_belt":blue.name}).insert(ignore_permissions=True)
        upgrade.submit()
        member.reload()
        self.assertEqual(member.current_belt, blue.name)
