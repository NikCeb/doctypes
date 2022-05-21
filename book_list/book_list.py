import frappe


def get_context(context):
    context.booker_list = frappe.get_all("Library Books",
                          fields=["title", "lbks_author", "lbks_subject", "lbks_quantity"],
                          order_by="lbks_subject desc")
    return context
