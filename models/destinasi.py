from odoo import api, fields, models


class destinasi(models.Model):
    _name = 'gikuy.destinasi'
    _description = 'Destinasi Wisata'

    
    
   
    name = fields.Char(string='Destinasi Tujuan')
    harga = fields.Integer(string='Harga')
    detail = fields.Char(string='Detail Tempat dan Acara')
    
    

    
