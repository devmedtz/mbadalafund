from django.db import models
from .choices import COMPANY_STATUSES

# Create your models here.
class Pitch(models.Model):
    company_name = models.CharField(max_length=180)
    email = models.EmailField()
    phone = models.CharField(max_length=12)    
    website = models.CharField(max_length=180)
    status = models.CharField(max_length=180, choices=COMPANY_STATUSES)
    activity = models.CharField(max_length=180)
    stage = models.CharField(max_length=180)
    company_summary = models.TextField()
    management_summary = models.TextField()
    financial_information = models.CharField(max_length=180)
    capital = models.CharField(max_length=180)
    capital_type = models.CharField(max_length=180)
    venture = models.CharField(max_length=180)
    reason = models.CharField(max_length=180)
    current_source = models.CharField(max_length=180)
    pitch_deck = models.FileField() 

    def __str__(self):
        return self.company_name