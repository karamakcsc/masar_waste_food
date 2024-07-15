// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on("Supplier Qualification", {
	after_workflow_action: (frm) => {
        frm.refresh_field('cubic_meters_per_week');
        frm.refresh_field('no_of_totes');
        frm.refresh_field('number_of_round_trips');
        // frm.refresh_field('price_per_ton');
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

frappe.ui.form.on('Supplier Qualification', {
    setup: function (frm) {
        frm.fields_dict['child_list_of_plants'].grid.get_field('plant_code').get_query = function(doc, cdt, cdn) {
            return {
                filters: {
                    "enable": 1,
                }
            };
        };

        frm.fields_dict['child_type_of_food_waste'].grid.get_field('waste_code').get_query = function(doc, cdt, cdn) {
            return {
                filters: {
                    "enabled": 1,
                }
            };
        };

        frm.fields_dict['child_data_fact_source'].grid.get_field('source_code').get_query = function(doc, cdt, cdn) {
            return {
                filters: {
                    "enabled": 1,
                }
            };
        };
 
    },

    //// //onload: function (frm) {
        
    //     // frm.set_df_property("contact_no_confirmed", "reqd", true);
    //     // frm.set_df_property("address_confirmed", "reqd", true);

    //     // if (doc.contact_no_confirmed == 1 && doc.address_confirmed == 1){
            
    //     //     frm.toggle_display("section_break_yekf", false);

    //     // }
    // }
});


frappe.ui.form.on("Supplier Qualification", {
	waste_weight: function(frm)  {
        if (frm.doc.round_trip_cost && frm.doc.estimated_quantity_per_week && frm.doc.waste_weight && frm.doc.waste_weight!= 0 && frm.doc.estimated_quantity_per_week!= 0) {
        frm.doc.price_per_ton = flt(frm.doc.round_trip_cost) / (flt(frm.doc.estimated_quantity_per_week) * flt(frm.doc.waste_weight));
        frm.refresh_field('price_per_ton');
            }
    },
    solid_percentages: function(frm) {
        if (frm.doc.solid_percentages || frm.doc.moisture_percentages) {
            if (!frm.doc.moisture_percentages && frm.doc.solid_percentages > 0 && frm.doc.solid_percentages <= 100) {
                frm.doc.moisture_percentages = 100 - frm.doc.solid_percentages;
                frm.refresh_field("moisture_percentages");
            }
            if (!frm.doc.solid_percentages && frm.doc.moisture_percentages > 0 && frm.doc.moisture_percentages <= 100) {
                frm.doc.solid_percentages = 100 - frm.doc.moisture_percentages;
                frm.refresh_field("solid_percentages");
            }
        }
    },
    moisture_percentages: function(frm) {
        if (frm.doc.solid_percentages || frm.doc.moisture_percentages) {
            if (!frm.doc.moisture_percentages && frm.doc.solid_percentages > 0 && frm.doc.solid_percentages <= 100) {
                frm.doc.moisture_percentages = 100 - frm.doc.solid_percentages;
                frm.refresh_field("moisture_percentages");
            }
            if (!frm.doc.solid_percentages && frm.doc.moisture_percentages > 0 && frm.doc.moisture_percentages <= 100) {
                frm.doc.solid_percentages = 100 - frm.doc.moisture_percentages;
                frm.refresh_field("solid_percentages");
            }
        }
    },
    estimated_quantity_per_week: function(frm) {
        if (frm.doc.round_trip_cost && frm.doc.estimated_quantity_per_week && frm.doc.suitable_container_size && frm.doc.suitable_container_size!= 0 && frm.doc.estimated_quantity_per_week!= 0) {
            frm.doc.cubic_meters_per_week = flt(frm.doc.estimated_quantity_per_week) / flt(frm.doc.suitable_container_size);
            frm.refresh_field('cubic_meters_per_week');

            if (frm.doc.cubic_meters_per_week && frm.doc.cubic_meters_per_week != 0) {
                frm.doc.no_of_totes = flt(frm.doc.cubic_meters_per_week) / flt(flt(frm.doc.suitable_container_size));
                frm.refresh_field('no_of_totes');
            }
            
            if (frm.doc.cubic_meters_per_week && frm.doc.cubic_meters_per_week != 0) {
                frm.doc.number_of_round_trips = flt(frm.doc.cubic_meters_per_week) / flt(flt(frm.doc.suitable_container_size));
                frm.refresh_field('number_of_round_trips');
            }
        }
    },
});