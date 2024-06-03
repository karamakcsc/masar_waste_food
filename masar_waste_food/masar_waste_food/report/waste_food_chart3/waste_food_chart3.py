import frappe

def execute(filters=None):
	return columns(), data(filters), None, chart()

def data(filters):
	conditions = ""
	if filters.get('workflow_state'):
		conditions += f" AND workflow_state = '{filters.get('workflow_state')}'"

	if filters.get('supplier_name'):
		conditions += f" AND supplier_name = '{filters.get('supplier_name')}'"

	if filters.get('round_trip_cost'):
		conditions += f" AND round_trip_cost = '{filters.get('round_trip_cost')}'"

	if filters.get('city'):
		conditions += f" AND city = '{filters.get('city')}'"		

	return frappe.db.sql(f"""
SELECT supplier_name, contact_number, contact_no_confirmed, email_id, country, city, round_trip_cost, workflow_state
FROM `tabSupplier Qualification`
WHERE 1=1 {conditions}					  
""")

def columns():
	return [
		"Supplier Name:Data:200",
		"Contact Number:Data:200",
		"Contact No. Confirmed:Check:200",
		"Email ID:Data:200",
		"Country:Link/Country:200",
		"City:Link/City:200",
		"Round Trip Cost:Data:200",
		"Workflow State:Link/Workflow State:200",
    ]

def chart():
	data = frappe.db.sql("""
					  SELECT city, round_trip_cost
					  FROM `tabSupplier Qualification`
					  GROUP BY city
					  """, as_dict = True)
	
	address = []
	cost = []

	for row in data:
		address.append(str(row.city))
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
