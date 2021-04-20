# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course(models.Model):
    _name = 'ras_project.project'
    _description = "Projects"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")