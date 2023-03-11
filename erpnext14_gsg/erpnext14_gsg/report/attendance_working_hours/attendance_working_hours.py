# Copyright (c) 2023, Zakaria and contributors
# For license information, please see license.txt
from frappe import _, qb
import frappe
from frappe.utils import date_diff, flt, getdate, time_diff_in_hours


def execute(filters=None):
	'''
	Attendance Date, Employee , Employee Name , Check in and Check Out .

	'''
	if not filters:
		return [], [], None, []

	validate_filters(filters)
	columns = get_columns()
	conditions = get_conditions(filters)

	data = get_data(conditions, filters)
	if not data:
		return [], []

	return columns, data


def get_conditions(filters):
	conditions = ""

	if filters.get("from_date") and filters.get("to_date"):
		conditions += " and a.attendance_date between %(from_date)s and %(to_date)s"

	elif filters.get("from_date") and not filters.get("to_date"):
		conditions += " and a.attendance_date > %(from_date)s"

	if filters.get("employee"):
		conditions += " and a.employee = %(employee)s"

	if filters.get("department"):
		conditions += " and a.department = %(department)s"

	return conditions


def get_data(conditions, filters):
	print('#'*100)
	print('#'*100)
	print('#'*100)

	def calc_working_hours(check_in, check_out):
		print('check_in:', check_in, type(check_in))
		print('check_out:', check_out, type(check_out))

		if not check_in or not check_out:
			return 0
		else:
			return time_diff_in_hours(check_out, check_in)

	data = frappe.db.sql(
		"""
		SELECT
			a.attendance_date as attendance_date,
			a.employee as employee,
			a.employee_name as employee_name,
			a.check_in as check_in,
			a.check_out as check_out
		FROM
			`tabAttendance` a
		WHERE
			a.idx >= 0
			{conditions}
			
	""".format(
			conditions=conditions
		),
		filters,
		as_dict=1,
	)
	for row in data:
		working_hours = calc_working_hours(row['check_in'], row['check_out'])
		row['working_hours'] = working_hours

	print(type(data))
	print(data)
	# print("""
	# 	SELECT
	# 		a.attendance_date as attendance_date,
	# 		a.employee as employee,
	# 		a.employee_name as employee_name,
	# 		a.check_in as check_in,
	# 		a.check_out as check_out
	# 	FROM
	# 		`tabAttendance` a
	# 	WHERE
	# 		a.idx > 0
	# 		{conditions}
	#
	# """.format(
	# 		conditions=conditions
	# 	))
	return data


def validate_filters(filters):
	from_date, to_date = filters.get("from_date"), filters.get("to_date")

	# if not from_date and to_date:
	# 	frappe.throw(_("From and To Dates are required."))
	if from_date and  to_date:
		if date_diff(to_date, from_date) < 0:
			frappe.throw(_("To Date cannot be before From Date."))


def get_columns():
	columns = [
		{
			"label": _("Attendance Date"),
			"fieldname": "attendance_date",
			"fieldtype": "Date",
			"width": 150,
		},

		{
			"label": _("Employee"),
			"fieldname": "employee",
			"fieldtype": "Link",
			"options": "Employee",
			"width": 150,
		},
		{
			"label": _("Employee Name"),
			"fieldname": "employee_name",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"label": _("Check in"),
			"fieldname": "check_in",
			"fieldtype": "Time",
			"width": 100,
		},
		{
			"label": _("Check Out"),
			"fieldname": "check_out",
			"fieldtype": "Time",
			"width": 100,
		},

		{
			"label": _("Working Hours"),
			"fieldname": "working_hours",
			"fieldtype": "Float",
			"width": 150,
		},
	]






	return columns
