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
					  SELECT address , round_trip_cost
					  FROM `tabSupplier Qualification`
					  """, as_dict = True)
	
	address = []
	cost = []

	for row in data:
		address.append(row.address)
		cost.append(row.round_trip_cost)

	chart = {
        'data': {
            'labels': address,
			
            'datasets': [{
                'name': 'Round Trip Cost',
                'values': cost,
            }]
        },
        'type': 'bar'
    }

	return chart	
