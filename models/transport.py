from odoo import api, fields, models


class Transport(models.Model):
    _name = 'gikuy.transport'
    _description = 'New Description'

    

    mitraperusahaan = fields.Char(string='Nama Perusahaan')
    name = fields.Selection(string='Alat Transportasi', selection=[('MOBIL', 'Mobil'), ('BIS', 'BIS'),('ELF', 'ELF')])
    harga = fields.Integer(string='Harga')
    detail = fields.Char(string='Detail')
    
