# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


from datetime import date
import frappe
from frappe.model.document import Document

class LibraryBorrowStudent(Document):
	pass

	def validate(self):
		book = self.lb_title
		doc = frappe.get_doc("Library Books" , book)
		number = doc.lbks_quantity
		doc.lbks_quantity = number - 1

		self.lb_from_date = date.today()

		doc.save()
