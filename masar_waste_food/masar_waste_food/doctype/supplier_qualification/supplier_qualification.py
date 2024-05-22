import frappe
from frappe.model.document import Document

class SupplierQualification(Document):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_updating = False

    def validate(self):
        pass
        # if (self.email_id is None):
        #     frappe.throw('Please Enter Email')

    def on_update(self):
        if not self.is_updating:
            self.is_updating = True
            self.cubic_meter_sum()
            self.num_of_tote_sum()
            self.price_per_ton_sum()
            self.is_updating = False

    def on_submit(self):
        self.create_supplier()

    def create_supplier(self):
        doc = frappe.new_doc('Supplier')
        doc.supplier_name = self.supplier_name
        doc.supplier_type = self.supplier_type
        doc.email_id = self.email_id
        doc.mobile_no = self.contact_number
        # doc.supplier_primary_address = self.address
        doc.insert(ignore_permissions=True)

    def cubic_meter_sum(self):
        if self.workflow_state == 'Site Surveyed':
            total = float(self.estimated_quantity_per_week)
            tons_per = float(self.suitable_container_size)
            if tons_per > 0:
                self.cubic_meters_per_week = total / tons_per
                self.save(ignore_permissions=True)

    def num_of_tote_sum(self):
        if self.workflow_state == 'Site Surveyed':
            tote_size = float(self.suitable_container_size)
            cubic_meters = float(self.cubic_meters_per_week)
            if tote_size > 0:
                self.no_of_totes = cubic_meters / tote_size
                self.number_of_round_trips = self.no_of_totes
                self.save(ignore_permissions=True)

    def price_per_ton_sum(self):
        if self.workflow_state == 'Site Surveyed':
            num_of_rt = float(self.number_of_round_trips)
            price_of_rt = float(self.round_trip_cost)
            total = float(self.estimated_quantity_per_week)
            if total > 0:
                self.price_per_ton = (num_of_rt * price_of_rt) / total
                self.save(ignore_permissions=True)