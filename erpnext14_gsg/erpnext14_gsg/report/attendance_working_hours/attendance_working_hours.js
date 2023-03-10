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


	],
	};
//	"formatter": function (value, row, column, data, default_formatter) {
//    value = default_formatter(value, row, column, data);
//    let format_fields = ["attendance_name"];
//
//    if (in_list(format_fields, column.fieldname)) {
//      console.log(format_fields, column.fieldname);
//      value = "<style>.hover-me:hover{cursor: pointer}</style><span class='hover-me' onclick=" + open_new_tap_attendance(val) + "</span>"";
//    }
//
//    return value;
//  }
//    "formatter": function (value, row, column, data, default_formatter) {
//        value = default_formatter(value, row, column, data);
//        let format_fields = ["attendance_name"];
//
//        if (in_list(format_fields, column.fieldname)) {
////          console.log(format_fields, column.fieldname);
////			value = "<span style='color:red;'>" + value + "</span>";
//            value = '<span class="hover-me" onclick="open_new_tap_attendance(\''+value+'\')">'+value + '</span>';
//        }
//
//        return value;
//      }
//      };
//
//function open_new_tap_attendance(val) {
//    window.open(/app/attendance/${val});
//}

