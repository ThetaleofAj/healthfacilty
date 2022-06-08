from django.db import models

# Create your models here.
class HealthFacility(models.Model):
   Name = models.CharField(max_length=100,null=True)
   Province = models.CharField(max_length=100,null=True)
   District = models.CharField(max_length=100,null=True)
   Ward = models.CharField(max_length=100,null=True)
   Coordinates =  models.CharField(max_length=250,null=True)
  # phoneNumber = models.CharField(max_length=100,null=True)
   #services = models.CharField(max_length=100,null=True)
  # equipment = models.CharField(max_length=100,null=True)
   infrastructure = models.TextField(null=True)
   #operatingHours = models.CharField(max_length=100,null=True)

class ContactDetails(models.Model):
   facility = models.ForeignKey(HealthFacility,on_delete=models.CASCADE,blank=True,related_name='contacts')
   details = models.CharField(max_length=100,null=True)

class Services(models.Model):
   facility = models.ForeignKey(HealthFacility,on_delete=models.CASCADE,blank=True,related_name='services')
   service = models.CharField(max_length=100,blank=True)

class Equipment(models.Model):
   facility = models.ForeignKey(HealthFacility,on_delete=models.CASCADE,blank=True,related_name='equipment')
   equipment = models.CharField(max_length=100,blank=True)

class OperatingHours(models.Model):
   facility = models.ForeignKey(HealthFacility,on_delete=models.CASCADE,blank=True,related_name='hours')
   day = models.CharField(max_length=50,blank=True)
   hours = models.CharField(max_length=100,blank=True)

