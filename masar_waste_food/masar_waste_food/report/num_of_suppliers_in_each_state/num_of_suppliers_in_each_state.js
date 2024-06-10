// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

frappe.query_reports["Num of Suppliers in Each State"] = {
	"filters": [

	
		{
			"fieldname": "supplier_name",
			"label": __("Supplier Name"),
			"fieldtype": "Data",
		},

		{
			"fieldname": "city",
			"label": __("City"),
			"fieldtype": "Data",
		},
		
		{
			"fieldname": "workflow_state",
			"label": __("Workflow State"),
			"fieldtype": "Select",
			"options": " \nDraft\nPhone Call Completed\nRoute Completed\nSite Survey Completed\nLab Test 1 Completed\nLab Test 2 Completed\nApproved",
		},
		

	]
};
