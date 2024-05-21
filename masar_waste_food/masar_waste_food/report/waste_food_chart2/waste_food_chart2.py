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
					  SELECT supplier_name, estimated_quantity_per_week, moisture_percentage, price_per_ton
FROM `tabSupplier Qualification`
ORDER BY supplier_name DESC
LIMIT 5;
					  """, as_dict = True)
	
	supplier = []
	quantity = []
	moisture = []
	cost = []

	for row in data:
		supplier.append(row.supplier_name)
		quantity.append(row.estimated_quantity_per_week)
		moisture.append(row.moisture_percentage)
		cost.append(row.price_per_ton)

	chart = {
        'data': {
            'labels': supplier,
			
            'datasets': [{
                'name': 'Quantity Per Week',
                'values': quantity,
            },
			{
				'name': 'Moisture Percentage',
				'values': moisture,
			},
			{
				'name': 'Cost Per Ton',
				'values': cost,
			}]
        },
        'type': 'bar'
    }

	return chart	