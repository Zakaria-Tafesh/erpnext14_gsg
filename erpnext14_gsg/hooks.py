from . import __version__ as app_version

app_name = "erpnext14_gsg"
app_title = "Erpnext14 Gsg"
app_publisher = "Zakaria"
app_description = "For GSG"
app_email = "zak@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext14_gsg/css/erpnext14_gsg.css"
# app_include_js = "/assets/erpnext14_gsg/js/erpnext14_gsg.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext14_gsg/css/erpnext14_gsg.css"
# web_include_js = "/assets/erpnext14_gsg/js/erpnext14_gsg.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erpnext14_gsg/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}

doc_events = {
	"Material Request": {
		"on_submit": "erpnext14_gsg.doc_events.material_request.make_stock_entry_from_material_issue"
	},
}


doctype_js = {"Journal Entry": "public/js/journal_entry.js",
              "Payment Entry": "public/js/payment_entry.js",
              }

fixtures = [
    "Purchase Taxes and Charges Template",
    "Sales Taxes and Charges Template",
    {"dt": "Salary Component",
        "filters":
            [["name", "like", "%GSG%"]]},
]
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "erpnext14_gsg.utils.jinja_methods",
#	"filters": "erpnext14_gsg.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "erpnext14_gsg.install.before_install"
# after_install = "erpnext14_gsg.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "erpnext14_gsg.uninstall.before_uninstall"
# after_uninstall = "erpnext14_gsg.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext14_gsg.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events



# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"erpnext14_gsg.tasks.all"
#	],
#	"daily": [
#		"erpnext14_gsg.tasks.daily"
#	],
#	"hourly": [
#		"erpnext14_gsg.tasks.hourly"
#	],
#	"weekly": [
#		"erpnext14_gsg.tasks.weekly"
#	],
#	"monthly": [
#		"erpnext14_gsg.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "erpnext14_gsg.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "erpnext14_gsg.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "erpnext14_gsg.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["erpnext14_gsg.utils.before_request"]
# after_request = ["erpnext14_gsg.utils.after_request"]

# Job Events
# ----------
# before_job = ["erpnext14_gsg.utils.before_job"]
# after_job = ["erpnext14_gsg.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"erpnext14_gsg.auth.validate"
# ]
