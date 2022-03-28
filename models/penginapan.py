from odoo import api, fields, models


class penginapan(models.Model):
    _name = 'gikuy.penginapan'
    _description = 'Daftar Penginapan'

    name = fields.Char(string='Nama Penginapan')
    harga = fields.Integer(string='Harga')
    detail = fields.Char(string='Detail')
    
    
