import frappe
import traceback


def make_stock_entry_from_material_issue(doc, method):
	if doc.material_request_type == 'Material Issue':
		from erpnext.stock.doctype.material_request.material_request import make_stock_entry

		stock_entry = make_stock_entry(doc.name)
		# stock_entry = frappe.new_doc("Stock Entry")
		# stock_entry.naming_series = "MAT-STE-.YYYY.-"
		# stock_entry.posting_date = frappe.utils.nowdate()
		# stock_entry.stock_entry_type = "Material Issue"
		# for item in doc.items:
		#     stock_entry.append("items", {
		#         "item_code": item.item_code,
		#         "item_name": item.item_name,
		#         "description": item.description,

		#         "material_request": doc.name,
		#     })
		stock_entry.save(ignore_permissions=True)
		stock_entry.submit()
		frappe.msgprint("Stock Entry saved successfully for this Material Request",
			alert=True,
		)
