from django.db import models


class Charity_Request(models.Model):
    TYPE = (
        ('', '------------'),
        ('educational', 'Educational'),
        ('health', 'Healthy'),
        ('environment', 'Environment'),
        ('international', 'International'),
        
    )

    organisation_name = models.CharField(default=None ,max_length=100)
    address = models.CharField(blank=True , default='' ,max_length=100)
    phone = models.CharField(default='' ,max_length=11)
    email = models.EmailField(max_length=254)

    constitution_doc = models.FileField(upload_to='uploads/')
    deeds_document = models.FileField(upload_to='uploads/')
    elligibility_doc = models.FileField(upload_to='uploads/')
    charity_type = models.CharField(blank=True , default='no' ,max_length=100 , choices = TYPE)
    approved = models.IntegerField(default=0)
    password = models.CharField(default='qwertypass' ,max_length=11)
    
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)
   

    def __str__(self):
        return '%s' % self.organisation_name
