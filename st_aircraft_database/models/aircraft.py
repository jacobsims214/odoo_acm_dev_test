# -*- coding: utf-8 -*-
from odoo import api, fields, models

class AircraftData(models.Model):
    _name = "aircraft.data"
    _description = "Aircraft Data"

    tail_number = fields.Char(string='Tail Number', required=True)
    serial_number = fields.Char(string='Serial Number', required=True)
    sale_status = fields.Selection([
        ('sale', 'For Sale'),
        ('sold', 'Sold'),
    ], required=True, default='sale')
    note = fields.Text(string='Description')