import frappe

@frappe.whitelist()
def waste_card_data():
    query = frappe.db.sql("""
                SELECT COUNT(supplier_name)
                FROM `tabSupplier Qualification`
                WHERE docstatus = 1
                          """)
    
    # frappe.msgprint(query)
    waste_generator = query

    return {
        'waste_generator': waste_generator
    }

@frappe.whitelist()
def draft_card_data():
    query = frappe.db.sql("""
                        SELECT COUNT(supplier_name)
                        FROM `tabSupplier Qualification`
                        WHERE docstatus = 0  
                          """)
    
    drafts = query

    return {
        'drafts': drafts
    }
                          