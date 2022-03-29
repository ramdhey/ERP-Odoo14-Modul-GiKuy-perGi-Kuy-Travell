from odoo import api, fields, models


class Order(models.Model):
    _name = 'gikuy.order'
    _description = 'New Description'

    rinciorderan_ids = fields.One2many(comodel_name='gikuy.orderrinci', inverse_name='order_id', string='Rincian Pesanan')
    

    name = fields.Char(string='ID Booking', required=True)
    tanggal_booking = fields.Date(string='Tanggal Booking', default=fields.Date.today())
    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    
    @api.depends('rinciorderan_ids')
    def _compute_total(self):
        for record in self:
            x = sum(self.env['gikuy.orderrinci'].search([('order_id', '=', record.id)]).mapped('harga'))
            
            record.total = x
    




class RincianOrderan(models.Model):
    _name = 'gikuy.orderrinci'
    _description = 'New Description'
    
    order_id = fields.Many2one(comodel_name='gikuy.order', string='Booking')
    funtrip_id = fields.Many2one(comodel_name='gikuy.funtrip', string='Paket FunTrip') 
    

    name = fields.Char(string='Name')
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    ava = fields.Integer(string='Quantity')
    hargaperunit = fields.Integer(compute='_compute_hargaperunit', string='Harga perPaket')

    @api.depends('funtrip_id')
    def _compute_hargaperunit(self):
        for record in self:
            record.hargaperunit   = record.funtrip_id.harga 

    
    @api.depends('ava','hargaperunit')
    def _compute_harga(self):
        for record in self:
            record.harga   = record.funtrip_id.harga * record.ava
