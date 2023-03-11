# Copyright (c) 2023, Zakaria and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


def get_employee_last_salary_slip(employee):
	salary_slips = frappe.get_list(
		"Salary Slip",
		filters={"employee": employee, "docstatus": 1},
		order_by="start_date desc",
	)

	return salary_slips


class ToWhomItConcerns(Document):

	@frappe.whitelist()
	def get_employee_fields(self):
		employee_name, department, date_of_joining = frappe.db.get_value(
			"Employee",
			{"name": self.employee},
			["employee_name", "department", "date_of_joining"],
		)
		salary = get_employee_last_salary_slip(self.employee)
		if not salary:
			salary = 0
		else:
			salary = salary[0].net_pay

		return {
			"employee_name": employee_name,
			"department": department,
			"date_of_joining": date_of_joining,
			"salary": salary,
		}



