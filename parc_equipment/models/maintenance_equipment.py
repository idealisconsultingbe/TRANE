from odoo import models, fields, _


class ParcEquipment(models.Model):
    _inherit = "maintenance.equipment"
    _description = "Trane Parc Maintenance Equipment"
    
    origin_picking_ids = fields.Many2many("stock.picking", string="origin picking")
    client_id = fields.Many2one("res.partner", string="Client & Address")
    account_analystic_id = fields.Many2one("account.analytic.account", string="Analytic Account")
    product_id = fields.Many2one("product.product", string="Product")

    def action_open_view_document(self):
        views = [
            (self.env.ref('documents.document_view_kanban').id, 'kanban'),
            (self.env.ref('documents.documents_view_list').id, 'tree'),       
        ]
        return {
            'name': _('Document'),
            'type': 'ir.actions.act_window',
            'view_mode': 'kanban',
            'res_model': 'documents.document',
            'views': views,
            'view_id': self.env.ref('documents.document_view_kanban').id,
            'target': 'current',
            'context': {
                "search_default_partner_id": self.client_id.id,
                "default_partner_id": self.client_id.id,
                "searchpanel_default_folder_id": False
            },
        }

    def action_open_view_stock(self):
        operation_type_id = False
        operation_type_code = self._context.get("picking_type_code")
        operation_incomming = operation_type_code == "incoming"
      
        views = [
            (self.env.ref('stock.stock_picking_kanban').id, 'kanban'),
            (self.env.ref('stock.vpicktree').id, 'tree'),
            (self.env.ref('stock.stock_picking_calendar').id, 'calendar'),
            (self.env.ref('stock_enterprise.stock_map_view').id, 'map'), 
            (self.env.ref('stock.view_picking_form').id, 'form'),       
        ]
        return {
            'name': _('Receipt') if operation_incomming else _('Delivery'),
            'type': 'ir.actions.act_window',
            'view_mode': 'kanban',
            'res_model': 'stock.picking',
            'views': views,
            'view_id': self.env.ref('stock.stock_picking_kanban').id,
            'target': 'current',
            'domain': [('id', 'in', self.origin_picking_ids.ids), ('picking_type_code', '=', operation_type_code)],
        }     