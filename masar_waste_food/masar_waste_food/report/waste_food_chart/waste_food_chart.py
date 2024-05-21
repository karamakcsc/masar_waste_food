import frappe

def execute(filters=None):
	return columns(), data(filters), None, chart()

def data(filters):
	conditions = ""
	if filters.get('workflow_state'):
		conditions += f" AND workflow_state = '{filters.get('workflow_state')}'"

	if filters.get('supplier_name'):
		conditions += f" AND supplier_name = '{filters.get('supplier_name')}'"

	return frappe.db.sql(f"""
SELECT supplier_name, contact_number, contact_no_confirmed, email_id, expected_quantity, workflow_state
FROM `tabSupplier Qualification`
WHERE 1=1 {conditions}					  
""")

def columns():
	return [
		"Supplier Name:Data:200",
		"Contact Number:Data:200",
		"Contact No. Confirmed:Check:200",
		"Email ID:Data:200",
		"Expected Quantity:Data:200",
    ]

def chart():
	data = frappe.db.sql("""
					  SELECT address , estimated_quantity_per_week
					  FROM `tabSupplier Qualification`
					  """, as_dict = True)
	
	address = []
	quantity = []

	for row in data:
		address.append(row.address)
		quantity.append(row.estimated_quantity_per_week)

	chart = {
        'data': {
            'labels': address,
			
            'datasets': [{
                'name': 'Quantity Per Week',
                'values': quantity,
            }]
        },
        'type': 'bar'
    }

	return chart	
	

	
