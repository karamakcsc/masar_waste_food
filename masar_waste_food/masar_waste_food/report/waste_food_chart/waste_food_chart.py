import frappe

def execute(filters=None):
	return columns(), data(filters), None, chart()

def data(filters):
	conditions = ""
	if filters.get('workflow_state'):
		conditions += f" AND workflow_state = '{filters.get('workflow_state')}'"

	if filters.get('supplier_name'):
		conditions += f" AND supplier_name = '{filters.get('supplier_name')}'"

	if filters.get('country'):
		conditions += f" AND country = '{filters.get('country')}'"	

	if filters.get('city'):
		conditions += f" AND city = '{filters.get('city')}'"

	if filters.get('estimated_quantity_per_week'):
		conditions += f" AND estimated_quantity_per_week = '{filters.get('estimated_quantity_per_week')}'"		

	return frappe.db.sql(f"""
SELECT supplier_name, contact_number, contact_no_confirmed, email_id, country, city, estimated_quantity_per_week, workflow_state
FROM `tabSupplier Qualification`
WHERE 1=1 {conditions}					  
""")

def columns():
	return [
		"Supplier Name:Data:200",
		"Contact Number:Data:200",
		"Contact No. Confirmed:Check:200",
		"Email ID:Data:200",
		"Country:Link/Country:150",
		"City:Link/City:150",
		"Quantity Per Week:Data:200",
		"Workflow State:Link/Workflow State:200",
    ]

def chart():
	data = frappe.db.sql("""
					  SELECT city, estimated_quantity_per_week
					  FROM `tabSupplier Qualification`
					  GROUP BY city
					  """, as_dict = True)
	
	address = []
	quantity = []

	for row in data:
		address.append(str(row.city))
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
	

	
