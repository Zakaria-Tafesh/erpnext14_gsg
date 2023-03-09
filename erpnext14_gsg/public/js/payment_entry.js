frappe.ui.form.on('Payment Entry', {
	refresh(frm) {
		// your code here
//		msgprint('bbbbbb');
        var new_option = ["GSG-JV-.YYYY.-"]

		set_field_options("naming_series", new_option);



	}
})