# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class LibraryBooks(Document):
    #this method will run every time a document is saved
    def before_save(self):
        self.route = f'{self.title}-{self.lbks_isbn}'

    def before_naming(self):
        self.lbks_max_quantity = f'{self.lbks_quantity}'
