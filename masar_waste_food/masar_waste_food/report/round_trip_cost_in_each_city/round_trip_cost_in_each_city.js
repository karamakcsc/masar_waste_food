// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

frappe.query_reports["Round Trip Cost in Each City"] = {
	"filters": [

		{
			"fieldname": "supplier_name",
			"label": __("Supplier Name"),
			"fieldtype": "Data",
		},

		{
			"fieldname": "city",
			"label": __("City"),
			"fieldtype": "Link",
			"options": "City",
		},

		{
			"fieldname": "round_trip_cost",
			"label": __("Round Trip Cost"),
			"fieldtype": "Data",
		},

		{
			"fieldname": "workflow_state",
			"label": __("Workflow State"),
			"fieldtype": "Select",
			"options": " \nDraft\nAddress Confirmed\nRoute Feasible\nSite Surveyed\nPass Test 1\nPass Test 2\nApproved",
		},
		

	]
};
