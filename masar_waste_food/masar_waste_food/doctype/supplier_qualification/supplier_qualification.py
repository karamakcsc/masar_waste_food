import frappe
from frappe.model.document import Document

class SupplierQualification(Document):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.is_updating = False

    def validate(self):

        if self.workflow_state == 'Address Confirmed':
             if self.contact_no_confirmed and self.address_confirmed:
                  pass
             else:
                  frappe.throw('Contact No. Confirmed and Address Confirmed Must be Checked to Go to the Next State')

        if self.workflow_state == 'Site Surveyed':
            if not self.sample_collected:
                frappe.throw('Sample Collected Must Be Checked To Go The Next State')
            if not self.suitable_container_size:
                 frappe.throw('Suitable Container Size Must Be Selected To Go The Next State')
            self.cubic_meter_sum()
            self.num_of_tote_sum()
        if self.workflow_state == 'Pass Test 1':
            if not self.lab_test_1_result == 'Passed':
                frappe.throw('Lab Test Result Must Be "Passed" To Go To The Next State')
            if not self.waste_weight:
                 frappe.throw('Waste Weight Per Cubic Meter Must Be Selected To Go The Next State')    
            # self.price_per_ton_sum()
            if float(self.solid_percentages) + float(self.moisture_percentages) > 100:
                 frappe.throw('The Percentages of the Lab Tests Must Not be Bigger than 100')
        if self.workflow_state == 'Pass Test 2':
            if not self.lab_test_2_result == 'Passed':
                frappe.throw('Lab Test Result Must Be "Passed" To Go The Next State')
            if float(self.fat_percentage) + float(self.protein_percentage) + float(self.fiber_percentage) > 100:
                 frappe.throw('The Percentages of the Lab Tests Must Not be Bigger than 100')
    # def on_update(self):
    #     if not self.is_updating:
    #         self.is_updating = True
            
    #         self.is_updating = False

    def on_submit(self):
        self.create_supplier()

    def create_supplier(self):
        doc = frappe.new_doc('Supplier')
        doc.supplier_name = self.supplier_name
        doc.supplier_type = self.supplier_type
        doc.supplier_group = self.supplier_group
        doc.email_id = self.email_id
        doc.mobile_no = self.contact_number
        # doc.supplier_primary_address = self.address
        doc.insert(ignore_permissions=True)

    def cubic_meter_sum(self):
            total = float(self.estimated_quantity_per_week)
            tote_size = float(self.suitable_container_size)
            if tote_size > 0:
                self.cubic_meters_per_week = total / tote_size
                # self.save(ignore_permissions=True)
            else:
                 frappe.throw('Suitable Container Size Must Be A Number And Bigger Than 0')     

    def num_of_tote_sum(self):
            tote_size = float(self.suitable_container_size)
            cubic_meters = float(self.cubic_meters_per_week)
            if tote_size > 0:
                self.no_of_totes = cubic_meters / tote_size
                self.number_of_round_trips = self.no_of_totes
                # self.save(ignore_permissions=True)
            else:
                 frappe.throw('Suitable Container Size Must Be A Number And Bigger Than 0')    

    # def price_per_ton_sum(self):
    #         # num_of_rt = float(self.number_of_round_trips)
    #         price_of_rt = float(self.round_trip_cost)
    #         tote_weight = float(self.estimated_quantity_per_week) * float(self.waste_weight)
    #         if tote_weight > 0:
    #             self.price_per_ton = price_of_rt / tote_weight
    #         else:
    #              frappe.throw('Quantity Per Week After Visit Must Be A Number And Bigger Than 0')



######~.~. Mohamad Khalil Code ~.~.#####