frappe.ui.form.on('Journal Entry', {
	refresh(frm) {
		// your code here
//		msgprint('bbbbbb');
        var new_options = ["Journal Entry",
                            "Bank Entry",
                            "Cash Entry",
                            "Credit Card Entry",
                            "Debit Note",
                            "Credit Note",
                            "Contra Entry",
                            "Excise Entry",
                            "Write Off Entry",
                            "Opening Entry",
                            "Depreciation Entry",
                            "Exchange Rate Revaluation",
                            "Exchange Gain Or Loss",
                            "Deferred Revenue"
                            ]

		set_field_options("voucher_type", new_options);



	}
})