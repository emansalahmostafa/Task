from sre_constants import CATEGORY
from tabnanny import verbose
from unicodedata import category
from django.db import models

# Create your models here.
Gender=(
    ('male', 'male'),
    ('female', 'female')

)
Consultant=(
    ('yes', 'yes'),
    ('no', 'no')

)
OldPatient=(
    ('yes', 'yes'),
    ('no', 'no')

)
LiveConsultation=(
    ('yes', 'yes'),
    ('no', 'no')

)
class Inpatient(models.Model):
    count = models.PositiveIntegerField(null=True)
    name=models.CharField(max_length=100 ,null=True)
    date_of_birth=models.DateField(max_length=100 ,null=True)
    admission_date=models.DateField(max_length=100 ,null=True)
    gender= models.CharField(max_length=50 ,choices=Gender,null=True)
    reference=models.TextField(max_length=500 ,null=True)
    case=models.CharField(max_length=100 ,null=True)
    phone=models.CharField(max_length=100 ,null=True)
    consultant=models.CharField(max_length=50 ,choices=Consultant,null=True)
    credit_limit=models.TextField(max_length=500 ,null=True)
    old_patient=models.CharField(max_length=50 ,choices=OldPatient,null=True)
    bed_number=models.CharField(max_length=100 ,null=True)
    live_consultation=models.CharField(max_length=50 ,choices=LiveConsultation,null=True)
    height=models.CharField(max_length=100 ,null=True)
    weight=models.CharField(max_length=100 ,null=True)
    bp=models.CharField(max_length=100 ,null=True)
    pulse=models.CharField(max_length=100 ,null=True)
    temperature=models.CharField(max_length=100 ,null=True)
    respiration=models.CharField(max_length=100 ,null=True)
    symptoms_type=models.CharField(max_length=100 ,null=True)
    symptoms_title=models.CharField(max_length=100 ,null=True)
    symptoms_description=models.CharField(max_length=100 ,null=True)

        
    def __str__(self):
        return self.name
    
    
    
