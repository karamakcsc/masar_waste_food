import frappe

def execute(filters=None):
    return columns(), data(filters), None, chart()

def data(filters):
    conditions = ""

    if filters.get('city'):
        conditions += f" AND city = '{filters.get('city')}'"

    if filters.get('workflow_state'):
        conditions += f" AND workflow_state = '{filters.get('workflow_state')}'"

    if filters.get('supplier_name'):
        conditions += f" AND supplier_name = '{filters.get('supplier_name')}'"

    return frappe.db.sql(f"""
        SELECT supplier_name, contact_number, contact_no_confirmed, email_id, city, workflow_state
        FROM `tabSupplier Qualification`
        WHERE 1=1 {conditions}
    """)

def columns():
    return [
        "Supplier Name:Data:200",
        "Contact Number:Data:200",
        "Contact No. Confirmed:Check:150",
        "Email ID:Data:200",
        "City:Data:150",
        "Workflow State:Link/Workflow State:200",
    ]

def chart():
    state_data = frappe.db.sql("""
        SELECT workflow_state, COUNT(supplier_name) AS suppliers
        FROM `tabSupplier Qualification`
        GROUP BY workflow_state
        ORDER BY CASE
            WHEN workflow_state IS NULL THEN 8
            WHEN workflow_state = 'Draft' THEN 0
            WHEN workflow_state = 'Address Confirmed' THEN 1
            WHEN workflow_state = 'Route Feasible' THEN 2
            WHEN workflow_state = 'RSite Surveyed' THEN 3
            WHEN workflow_state = 'Pass Test 1' THEN 4
            WHEN workflow_state = 'Pass Test 2' THEN 5
            WHEN workflow_state = 'Approved' THEN 6
            ELSE 7
        END;
    """, as_dict=True)

    state_chart_labels = []
    state_chart_datasets = []

    for row in state_data:
        state_chart_labels.append(row.workflow_state)
        state_chart_datasets.append(row.suppliers)

    state_chart = {
        'data': {
            'labels': state_chart_labels,
            'datasets': [{
                'name': 'Suppliers',
                'values': state_chart_datasets,
            }]
        },
        'type': 'bar'
    }

    return state_chart