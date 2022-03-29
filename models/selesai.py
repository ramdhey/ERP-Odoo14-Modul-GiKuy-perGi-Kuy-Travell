from odoo import api, fields, models


class Selesai(models.Model):
    _name = 'gikuy.selesai'
    _description = 'History Perjalanan yang Telah Terlaksana'

    name = fields.Char(compute='_compute_nama_pemesan', string='Pesanan atas Nama')
    order_id = fields.Many2one(comodel_name='gikuy.order', string='ID Booking')
    noted = fields.Char(string='Note Evaluasi Perjalanan')
    
    


    @api.depends('order_id')
    def _compute_nama_pemesan(self):
        for record in self:
            record.name = self.env['gikuy.order'].search([('id', '=', record.order_id.id)]).mapped('namapemesannya').name

    
    
    bill = fields.Integer(compute='_compute_bill', string='Tagihan')
    
    @api.depends('order_id')
    def _compute_bill(self):
        for record in self:
            record.bill = record.order_id.total

    

    @api.model
    def create(self,vals):
        record = super(Selesai, self).create(vals) 
        if record.noted:
            self.env['gikuy.order'].search([('id','=',record.order_id.id)]).write({'selesaicuy':True})
            self.env['gikuy.akunting'].create({'kredit' : record.bill, 'name':record.name})          
            
                      
            return record




    def unlink(self):
        for gikuy in self:
            self.env['gikuy.order'].search([('id','=',gikuy.order_id.id)]).write({'selesaicuy':False})
        record = super(Selesai, self).unlink()

    
    
    