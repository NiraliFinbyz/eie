# Copyright (c) 2013, FinByz Tech Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from eie.eie.report.eie_item_wise_sales_register.eie_item_wise_sales_register import _execute

def execute(filters=None):
	return _execute(filters, additional_table_columns=[
		dict(fieldtype='Data', label='Customer GSTIN', fieldname="customer_gstin", width=120),
		dict(fieldtype='Data', label='Company GSTIN', fieldname="company_gstin", width=120),
		dict(fieldtype='Data', label='HSN Code', fieldname="hsn_code", width=120),
		dict(fieldtype='Data', label='Stock UOM', fieldname="stock_uom", width=60)
	], additional_query_columns=[
		'customer_gstin',
		'company_gstin',
		'gst_hsn_code',
		'stock_uom'
	])
