// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on("Supplier Qualification", {
	after_workflow_action: (frm) => {
        frm.refresh_field('cubic_meters_per_week');
        frm.refresh_field('no_of_totes');
        frm.refresh_field('number_of_round_trips');
        frm.refresh_field('price_per_ton');
    }
});
