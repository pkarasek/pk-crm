from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

"""
class CrmUser(models.Model):
    #user = models.OneToOneField(User, on_delete = models.CASCADE) 
    #company = models.ForeignKey(Company, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 50, null = False, blank = False)
    last_name = models.CharField(max_length = 50, null = False, blank = False)
 """   
    
class Company(models.Model):
    company_name = models.CharField(max_length = 50, null = False, blank = False)
    
    
    def __str__(self):
        return self.company_name