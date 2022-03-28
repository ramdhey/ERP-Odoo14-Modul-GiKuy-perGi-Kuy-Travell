from odoo import api, fields, models


class Transport(models.Model):
    _name = 'gikuy.transport'
    _description = 'New Description'

    name = fields.Selection(string='Alat Transportasi', selection=[('bis', 'Bis'), ('elf', 'ELF'),('mobil', 'Mobil'),('jeep', 'Jeep'),('kereta', 'Kereta'),('pesawat', 'Pesawat')])

    mitraperusahaan = fields.Char(string='Nama Perusahaan')
    harga = fields.Integer(string='Harga')
    detail = fields.Char(string='Detail')
    
