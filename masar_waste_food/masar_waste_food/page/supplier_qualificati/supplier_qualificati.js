frappe.pages['supplier-qualificati'].on_page_load = function (wrapper) {
	new MyPage(wrapper);
};
class MyPage {
	constructor(wrapper) {
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
			title: '',
			single_column: true
		});
		this.make();
	}
	make() {

		const head = ``;

		const body = `
			<div class="cards-container" id="cards-container"></div>
			<h4>Hello</h4>
		`;


		$(body).appendTo(this.page.main);

	}
	
	populateWasteCard() {
		frappe.call({
			method: 'masar_waste_food.masar_waste_food.page.supplier_qualificati.supplier_qualificati.waste_card_data',
			callback: (r) => {
				let submited_docs = r.message.waste_generator;
				let cardBody = ``;
				cardBody += `<div class="waste-card" id="waste-card">
								${submited_docs}
							</div>
							<div class="approved-card" id="approved-card">
								${submited_docs}
							</div>
							`;
				
				$('#cards-container').html(cardBody);
			}
		})
	}

	populateDraftCard() {
		frappe.call({
			method: 'masar_waste_food.masar_waste_food.page.supplier_qualificati.supplier_qualificati.draft_card_data',
			callback: (r) => {
				let drafts = r.message.drafts;
				let cardBody = ``;
				cardBody += `<div class="waste-card" id="waste-card">
								${drafts}
							</div>`;
				
				$('#cards-container').html(cardBody);
			}
		})
	}
}
