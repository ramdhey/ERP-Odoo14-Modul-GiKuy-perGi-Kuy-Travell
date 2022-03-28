from odoo import api, fields, models


class Funtrip(models.Model):
    _name = 'gikuy.funtrip'
    _description = 'Paket FunTrip '

    name = fields.Char(string='Nama Paket FunTrip' , required=True)
    tanggalberangkat = fields.Date(string='Keberangkatan', default=fields.Date.today(), required=True)
    tanggaltiba = fields.Date(string='Tiba Kembali', default=fields.Date.today(), required=True)
    makspeserta = fields.Integer(string='Max Peserta', required=True)
    transportasi_id = fields.Many2one(comodel_name='gikuy.transport', string='Transportasi')
    destinasi_id = fields.Many2one(comodel_name='gikuy.destinasi', string='Destinasi Wisata')
    harga = fields.Integer(string='Harga')
    detail = fields.Char(string='Detail Acara')

    
    
