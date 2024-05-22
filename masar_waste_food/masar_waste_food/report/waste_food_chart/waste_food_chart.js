// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

frappe.query_reports["Waste Food Chart"] = {
	"filters": [

		{
			"fieldname": "supplier_name",
			"label": __("Supplier Name"),
			"fieldtype": "Data",
		},

		{
			"fieldname": "country",
			"label": __("Country"),
			"fieldtype": "Link",
			"options": "Country",
		},

		{
			"fieldname": "city",
			"label": __("City"),
			"fieldtype": "Link",
			"options": "City",
		},

		{
			"fieldname": "estimated_quantity_per_week",
			"label": __("Quantity Per Week After Visit"),
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
