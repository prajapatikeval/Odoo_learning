from datetime import datetime
from odoo import fields, models

class BasePerson(models.Model):
    _name = "base.person"
    
    image = fields.Binary(string="Image")


    name = fields.Char(string="name")
    age = fields.Integer(string="Age")
    email = fields.Char(string="Email")
    gender = fields.Selection([("male","male"),("female","female"),("other","other")], string="Gender")
    date_of_birth = fields.Date(string="Date of Birth")
    start_date = fields.Date(string="Start Date")
    department_id = fields.Float(string="Salary")
    is_manager = fields.Boolean(string="Is manager")
    address = fields.Text(string="Address")
    created_at = fields.Datetime(string="Created Date", default=fields.Datetime.now, readonly=True)
    notes = fields.Html(string="Notes",help="Additional notes in HTML format")

class Employee(models.Model):
    _name = "employee.name"
    _description = "Employee Management System"
    _inherit = 'base.person'

class Manager(models.Model):
    _name = "manager.name"
    _description = "Manager Management"
    _inherit = 'base.person'

class Client(models.Model):
    _name = "client.name"
    _description = "Client Management"
    _inherit = 'base.person'


class Project(models.Model):
    _name = "project"
    _description = "Projects"

    project_image = fields.Binary(string="Image")
    project_name = fields.Char(string="Project Name")
    project_description = fields.Text(string="Project Description")
    project_start_date = fields.Date(string="Start Date")
    project_deadline = fields.Date(string="Deadline")
    project_state = fields.Selection([('todo','Todo'),('in progress','In Progress'),('done','Done'),], string="State",default="todo")

    project_days_left = fields.Integer(string="Days Left", compute="_compute_days_left" ,readonly=True)
    day_color = fields.Char(string="Days Left", compute="_compute_days_left" ,readonly=True)

    def _compute_days_left(self):
        today = datetime.today().date()

        for project in self:
            if project.project_deadline >= today:
                delta = project.project_deadline - today

                if delta.days > 2:
                    project.day_color = "#168D07" #green
                elif delta.days>1 and delta.days <= 2:
                    project.day_color = "#DB9A27" #yellow
                else:
                    project.day_color = "#CB0505" #red

                project.project_days_left = delta.days
            else:
                project.project_daus_left = 0
