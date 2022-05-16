# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt
# By Nikolai Ceballos

import frappe
from datetime import date
import numpy as np
from frappe.model.document import Document

class LibraryReturnTeacher(Document):
	pass

	def validate(self):
		user = self.lr_library_borrow_teacher
		doc_borrow_teacher = frappe.get_doc("Library Borrow Teacher" , user) #GET Student
		from_date = doc_borrow_teacher.lb_from_date
		due_date = doc_borrow_teacher.lb_due_date
		member = doc_borrow_teacher.lb_teacher
		doc_borrow_teacher.enabled = 0

		return_book = doc_borrow_teacher.lb_title
		book = frappe.get_doc("Library Books", return_book) #GET Book Title
		number = book.lbks_quantity # Return Copy Int
		book.lbks_quantity = int(number) + 2

		book.save()
		# book.save() If this runs,you are calling lr_library_borrow_teacher.property
		# hence it will -1 from quantity again, hence + 2

		self.lr_return_date = date.today() # SET Date
		self.lr_due_date = doc_borrow_teacher.lb_due_date
		today =  date.today()
		due = doc_borrow_teacher.lb_due_date

		if (today > due):
			due_days = int(np.busday_count( str(due) , str(today)))

			try:
				doc_member = frappe.new_doc("Library Overdue")
				doc_member.lob_user = str(member)
				doc_member.lob_overdue = int(due_days)
				doc_member.insert()

			except:
				check_doc = frappe.get_doc("Library Overdue", member)
				due_date = check_doc.lob_overdue
				check_doc.lob_overdue = int(due_date) + int(due_days)
				check_doc.save()

		if True:
			doc_borrow_teacher.save()
