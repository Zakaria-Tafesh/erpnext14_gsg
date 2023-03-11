// Copyright (c) 2023, Zakaria and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Attendance Working Hours"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),

			"fieldtype": "Date",
			"width": "80",
			"reqd": 0,
			"default": frappe.datetime.add_days(frappe.datetime.get_today(), -1),

		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),

			"fieldtype": "Date",
			"width": "80",
			"reqd": 0,
			"default": frappe.datetime.get_today()
		},
        {
			"fieldname":"employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"width": "80",
            "options": "Employee"
		},
        {
			"fieldname":"department",
			"label": __("Department"),
			"fieldtype": "Link",
			"width": "80",
            "options": "Department"
		},

	]
};
