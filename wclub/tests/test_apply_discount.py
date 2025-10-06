import frappe, unittest
from wclub.api import apply_discount

class TestApplyDiscount(unittest.TestCase):
    def test_apply_discount_percent(self):
        offer = frappe.get_doc({
            "doctype":"Offer",
            "club":"Demo Fighting Club",
            "title":"10% Off",
            "offer_type":"Percent",
            "value":10
        }).insert(ignore_permissions=True)
        res = apply_discount("Demo Fighting Club", None, 100, offer=offer.name)
        self.assertEqual(res["final_amount"], 90)
