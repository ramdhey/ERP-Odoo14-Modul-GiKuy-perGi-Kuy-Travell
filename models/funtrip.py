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
    penginapan_id = fields.Many2one(comodel_name='gikuy.penginapan', string='Penginapan')
    
    detail = fields.Char(string='Detail Acara')
    
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    

    
    @api.depends('transportasi_id','destinasi_id','penginapan_id')
    def _compute_harga(self):
        for record in self:
            record.harga   = record.transportasi_id.harga + record.destinasi_id.harga + record.penginapan_id.harga 


    
    detaildestinasi = fields.Char(compute='_compute_detaildestinasi', string='Detail Destinasi')
    
    @api.depends('destinasi_id')
    def _compute_detaildestinasi(self):
        for record in self:
            record.detaildestinasi = record.destinasi_id.detail
    
    mitraperusahaantrans = fields.Char(compute='_compute_mitraperusahaantrans', string='Nama Perusahaan Mitra Transportasi')
    
    @api.depends('transportasi_id')
    def _compute_mitraperusahaantrans(self):
        for record in self:
            record.mitraperusahaantrans = record.transportasi_id.mitraperusahaan

    

    detailtransportasi = fields.Char(compute='_compute_detailtransportasi', string='Detail Alat Transportasi')
    
    @api.depends('transportasi_id')
    def _compute_detailtransportasi(self):
        for record in self:
            record.detailtransportasi = record.transportasi_id.detail


    
    
    

    
    
