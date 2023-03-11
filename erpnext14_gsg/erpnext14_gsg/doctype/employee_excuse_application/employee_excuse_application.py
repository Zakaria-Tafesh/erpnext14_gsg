# Copyright (c) 2023, Zakaria and contributors
# For license information, please see license.txt

from frappe.utils import time_diff_in_hours, get_first_day, get_last_day
import frappe
from frappe.model.document import Document


class EmployeeExcuseApplication(Document):
	def validate(self):
		if time_diff_in_hours(self.from_time, self.to_time) > 0:
			frappe.throw("Error: From time should be before To time")
		self.hours = time_diff_in_hours(self.to_time, self.from_time)
		self.check_allowed_hours()

	def check_allowed_hours(self):
		department_hours = (
				frappe.db.get_value(
					"Department", self.department, "excuse_hours_allowed"
				)
				or 0
		)
		if department_hours == 0:
			return

		first_day_of_this_month = get_first_day(self.excuse_date)
		last_day_of_this_month = get_last_day(self.excuse_date)

		total_old_hours_in_month = frappe.db.sql(
						f"""
							SELECT IFNULL(sum(hours), 0) as hours FROM `tabEmployee Excuse Application`
							WHERE employee='{self.employee}'
							and excuse_date BETWEEN '{first_day_of_this_month}' AND '{last_day_of_this_month}'
							and department='{self.department}'
							and docstatus = 1
							""",
						as_dict=True,
						)
		if not total_old_hours_in_month:
			total_old_hours_in_month = 0
		else:
			total_old_hours_in_month = total_old_hours_in_month[0]['hours']

		total_old_and_new_hours = total_old_hours_in_month + self.hours

		if total_old_and_new_hours > department_hours:
			frappe.throw(
				f"This Employee exceeded his Allowed hours (depends on his Department): {department_hours}"
			)
