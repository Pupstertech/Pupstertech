from odoo import fields, models


class ExternalApp(models.Model):
    _name = "cc.external.app"
    _description = "Command Center External App"

    name = fields.Char(required=True)
    category = fields.Selection(
        [
            ("helpdesk", "Helpdesk"),
            ("esign", "E-Sign"),
            ("project", "Project"),
            ("marketing", "Marketing"),
            ("bi", "Business Intelligence"),
            ("knowledge", "Knowledge Base"),
        ],
        required=True,
    )
    url = fields.Char(required=True)
    active = fields.Boolean(default=True)


class PlanningNote(models.Model):
    _name = "cc.plan.note"
    _description = "Command Center Planning Note"

    title = fields.Char(required=True)
    summary = fields.Text(required=True)
    source = fields.Char(help="Meeting, task, assistant, or manual")
    planned_for = fields.Datetime()


class Reminder(models.Model):
    _name = "cc.reminder"
    _description = "Command Center Reminder"

    title = fields.Char(required=True)
    due_at = fields.Datetime(required=True)
    status = fields.Selection(
        [("pending", "Pending"), ("done", "Done"), ("dismissed", "Dismissed")],
        default="pending",
        required=True,
    )
    payload_json = fields.Text(help="Optional serialized context payload")
