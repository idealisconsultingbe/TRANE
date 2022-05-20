from odoo import models, api, fields, _


class TraneStockPicking(models.Model):
    _inherit = "stock.picking"
    
    def button_validate(self):
        self.ensure_one()
        res = super(TraneStockPicking, self).button_validate()
        if self.picking_type_id.code == "incoming":
            for move in self.move_ids_without_package:
                equipment = self.env["maintenance.equipment"].search([('product_id', '=', move.product_id.id)])
                if not equipment:
                    self.env["maintenance.equipment"].create(
                        {
                            'product_id': move.product_id.id,
                            'name': move.product_id.name,
                            'effective_date': move.date,
                            'origin_picking_ids': [(4, self.id)],
                            'account_analystic_id': move.analytic_account_line_id.id,
                            'serial_no': len(move.lot_ids) > 0 and move.lot_ids[:1].name,
                        }
                    )
        elif self.picking_type_id.code == "outgoing":
            for move in self.move_ids_without_package:
                equipment_id = self.env["maintenance.equipment"].search([('product_id', '=', move.product_id.id)], limit=1)
                if equipment_id:
                    equipment_id.write(
                        {
                            'client_id': self.partner_id,
                            'commission_date': self.scheduled_date,
                            'origin_picking_ids': [(4, self.id)],
                            'serial_no': len(move.lot_ids) > 0 and move.lot_ids[:1].name,
                        }
                    )
        return res

    def action_open_view_equipment(self):
        views = [
            (self.env.ref('maintenance.hr_equipment_view_kanban').id, 'kanban'),
            (self.env.ref('maintenance.hr_equipment_view_tree').id, 'tree'),
            (self.env.ref('maintenance.hr_equipment_view_form').id, 'form'),       
        ]
        return {
            'name': _('Equipment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'kanban',
            'res_model': 'maintenance.equipment',
            'views': views,
            'view_id': self.env.ref('maintenance.hr_equipment_view_kanban').id,
            'target': 'current',
            'domain': [('origin_picking_ids', 'in', self.id)],
        }