frappe.ui.form.on('Journal Entry', {
	refresh(frm) {
		// your code here
		msgprint('ccccc');
        var old_options = frm.doc.voucher_type
        console.log('11111');
        console.log(old_options);
        console.log('2222222');

		set_field_options("voucher_type", ["help_content", "zaaaaaaaak"]);



	}
})