// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on("Supplier Qualification", {
	after_workflow_action: (frm) => {
        frm.refresh_field('cubic_meters_per_week');
        frm.refresh_field('no_of_totes');
        frm.refresh_field('number_of_round_trips');
        frm.refresh_field('price_per_ton');
    },

    // address_map: function(frm){
    //     let mapdata = JSON.prase(cur_frm.doc.map).features[0];
    //     if (mapdata && mapdata.geometry.type=='Point'){
    //       let lat = mapdata.geometry.coordinates[1];
    //       let lon = mapdata.geometry.coordinates[0];
    
    //       frappe.call({
    //         type: "GET",
    //         url: `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`,
    //         callback: function (r){
    //           frm.set_value('address_map',r.display);
    //           frm.refresh_field('address_map');
    //         }
    //       })
    //     }
    
    //   }
});
