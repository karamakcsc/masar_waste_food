// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Supplier Qualification", {
// 	validate: function(frm){
//         cubicMeterSum(frm);
//         numOfToteSum(frm);
//         pricePerTonSum(frm);
//     }
// });

// function cubicMeterSum(frm){
//     var sum;
//     var total = frm.doc.expected_quantity;
//     var tons_per = frm.doc.tons_per_cubic_meters;
//     if(total && tons_per && tons_per > 0){
//         sum = flt(total / tons_per);
//         frm.set_value('cubic_meters_per_week', sum);
//         frm.refresh_field('cubic_meters_per_week');
//     }
//     else {
//         frappe.throw('Error dfs');
//     }
// }

// function numOfToteSum(frm){
//     var sum = 0;
//     var tote_size = frm.doc.suitable_container_size;
//     var cubic_meters = frm.doc.cubic_meters_per_week;
//     if(cubic_meters && tote_size && tote_size > 0){
//         sum = flt(cubic_meters / tote_size);
//         frm.set_value('no_of_totes', sum);
//         frm.refresh_field('no_of_totes');
//         frm.set_value('number_of_round_trips', sum);
//         frm.refresh_field('number_of_round_trips');
//     }
//     else {
//         frappe.throw('Error no cubic meters');
//     }
// }

// function pricePerTonSum(frm){
//     var sum = 0;
//     var num_of_rt = frm.doc.number_of_round_trips;
//     var price_rt = frm.doc.round_trip_cost;
//     var total = frm.doc.expected_quantity;
//     if(!num_of_rt && !price_rt && !total && total > 0){
//         sum = flt((num_of_rt * price_rt) / total);
//         frm.set_value('price_per_ton', sum);
//         frm.refresh_field('price_per_ton');
//     }
//     else {
//         frappe.throw('Error no num of rt');
//     }
// }