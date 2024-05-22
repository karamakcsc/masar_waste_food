// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

frappe.query_reports["Waste Food Chart2"] = {
	"filters": [

		{
			"fieldname": "supplier_name",
			"label": __("Supplier Name"),
			"fieldtype": "Data",
		},

		{
			"fieldname": "estimated_quantity_per_week",
			"label": __("Quantity Per Week"),
			"fieldtype": "Float",
			"default": "Null",
		},

		{
			"fieldname": "moisture_percentage",
			"label": __("Moisture Percentage"),
			"fieldtype": "Data",
		},

		{
			"fieldname": "price_per_ton",
			"label": __("Price Per Ton"),
			"fieldtype": "Float",
			"default": "Null",
		},

		{
			"fieldname": "workflow_state",
			"label": __("Workflow State"),
			"fieldtype": "Select",
			"options": " \nDraft\nAddress Confirmed\nRoute Feasible\nSite Surveyed\nPass Test 1\nPass Test 2\nApproved",
		},
		

	]
};
