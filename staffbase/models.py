from django.db import models

class StaffBase(models.Model):
    full_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=False)

    def get_role(self):
        return "Staff"

class Manager(StaffBase):
    title = models.CharField(max_length=100)

    def get_role(self):
        return "Manager"

class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.CASCADE)
    internship_end = models.DateField()

    def get_role(self):
        return "Intern"

# Create your models here.
