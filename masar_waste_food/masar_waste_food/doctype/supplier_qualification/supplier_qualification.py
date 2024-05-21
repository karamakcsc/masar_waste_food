# Copyright (c) 2024, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SupplierQualification(Document):
	def validate(self):
		if (self.email_id is None):
			frappe.throw('Please Enter Email')

	def on_update(self):
		self.cubic_meter_sum()
		self.num_of_tote_sum()
		self.price_per_ton_sum()

	def on_submit(self):
		self.creat_supplier()

	def creat_supplier(self):
		doc = frappe.new_doc('Supplier')
		doc.supplier_name = self.supplier_name
		doc.supplier_type = self.supplier_type
		doc.email_id = self.email_id
		doc.mobile_no = self.contact_number
		doc.supplier_primary_address = self.address
		doc.insert(ignore_permissions=True)
		frappe.db.commit()


	def cubic_meter_sum(self):
		sum = 0
		total = 0
		tons_per = 0
		
		if self.workflow_state == 'Route Feasible':
			total = self.expected_quantity
			tons_per = float(self.tons_per_cubic_meters)
			if tons_per > 0:
				sum = float(total / tons_per)
				self.cubic_meters_per_week = sum
				frappe.db.commit()

		elif self.workflow_state != 'Route Feasible':
			pass

		else:
			frappe.throw('Error: Cannot Sum Cubic Meters Per Week ')


	def num_of_tote_sum(self):
		sum = 0
		tote_size = 0
		cubic_meters = 0

		if self.workflow_state == 'Site Surveyed':
			tote_size = float(self.suitable_container_size)
			cubic_meters = float(self.expected_quantity/float(self.tons_per_cubic_meters))
			if tote_size > 0:
				sum = float(cubic_meters / tote_size)
				self.no_of_totes = sum
				frappe.db.commit()
				self.number_of_round_trips = sum
				frappe.db.commit()

		elif self.workflow_state != 'Site Surveyed':
			pass
		else:
			frappe.throw('Error: Cannot Sum Number of Totes')

	def price_per_ton_sum(self):
		sum = 0
		num_of_rt = 0
		price_of_rt = 0
		total = 0

		if self.workflow_state == 'Site Surveyed':
			num_of_rt = float(self.number_of_round_trips)
			price_of_rt = float(self.round_trip_cost)
			total = float(self.expected_quantity)
			if total > 0:
				sum = float((num_of_rt * price_of_rt) / total)
				self.price_per_ton = sum
				frappe.db.commit()

		elif self.workflow_state != 'Site Surveyed':
			pass
		else:
			frappe.throw('Error: Cannot Sum Price Per Ton')				

		
		
