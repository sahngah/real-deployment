from __future__ import unicode_literals
from django.db import models
from ..login_and_registration_app.models import User
from datetime import date

# Create your models here.
class PlanManager(models.Manager):
    def plan(self, data, user):
        errors=[]
        if len(data['destination']) < 1:
            errors.append('All Fields Are Required!')
        if len(data['description']) < 1:
            errors.append('All Fields Are Required!')
        if len(data['travelstartdate']) < 1:
            errors.append('All Fields Are Required!')
        if len(data['travelenddate']) < 1:
            errors.append('All Fields Are Required!')
        if data['travelstartdate'] > data['travelenddate']:
            errors.append('Travel end date should be after travel start date!')
        if errors:
            return {'errors': errors}
        else:
            plan = Plan.objects.create(user = user ,destination = data['destination'], description=data['description'], travelstartdate=data['travelstartdate'], travelenddate=data['travelenddate'])
            return {'plan': plan}

class Plan(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    travelstartdate = models.DateField()
    travelenddate = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = PlanManager()
    users = models.ManyToManyField(User, related_name = "plans_joined")
    user = models.ForeignKey(User, related_name = "plan_created")

#
# class PlanUser(models.Model):
#     user = models.ForeignKey('login_and_registration_app.user', default = None)
#     plan = models.ForeignKey('add_plan_app.plan', default = None)
