from datetime import datetime
from itertools import product
from typing_extensions import Required
from odoo import api,fields,models
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

class Farmer_details(models.Model):
    _name='farmer_details'
    _description='Farmer_Details'

    farmer_name=fields.Char(required=True)
    crop_name=fields.Char(string='Crop Name')
    date_delivered=fields.Datetime('Deliverty date',required=True, default=fields.Datetime.now)
    price_total=fields.Float(string='Amount')
    quantity_delivered=fields.Integer(string='Quantity')

    @api.model
    def create(self, vals):
        if vals.get('name','New') =='New':
            vals['name'] =self.env['ir.sequensue'].next_by_code('product_details') or '/'
        return super(Farmer_details,self).create(vals)   
    