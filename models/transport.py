from odoo import api, fields, models


class Transport(models.Model):
    _name = 'gikuy.transport'
    _description = 'New Description'

    name = fields.Selection(string='Transportasi', selection=[('paket1', 'Paket 1'), ('paket2', 'Paket 2'),('paket3', 'Paket 3'),('Paket4', 'Paket 4'),('paket5', 'Paket 5'),('paket6', 'Paket 6')])

    mitraperusahaan = fields.Char(string='Nama Perusahaan')
    harga = fields.Integer(string='Harga')
    detail = fields.Char(string='Detail')
    
