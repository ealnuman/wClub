import frappe
from frappe.utils import flt

@frappe.whitelist()
def apply_discount(club, member, amount, offer=None, coupon_code=None):
    amount = flt(amount)
    discount_value = 0.0
    if offer:
        o = frappe.get_doc("Offer", offer)
        if o.offer_type == "Percent":
            discount_value = (flt(o.value) / 100.0) * amount
        else:
            discount_value = flt(o.value)
    return {"amount": amount, "discount": discount_value, "final_amount": amount-discount_value}
