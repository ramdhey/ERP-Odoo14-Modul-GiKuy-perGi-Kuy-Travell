from odoo import api, fields, models


class destinasi(models.Model):
    _name = 'gikuy.destinasi'
    _description = 'Destinasi Wisata'

    name = fields.Selection(string='Nama Daerah', selection=[('bali', 'Bali'), ('bdg', 'Bandung'),('jgj', 'Jogjakarta'),('smg', 'Semarang'),('mlg', 'Malang'),('brm', 'Bromo')])
    
    destinasinya = fields.Char(string='Tempat Wisata yang akan dituju')
    harga = fields.Integer(string='Harga')
    detail = fields.Char(string='Detail Tempat dan Acara')
    
    

    
