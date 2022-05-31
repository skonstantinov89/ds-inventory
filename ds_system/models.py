from django.db import models
from logging.config import IDENTIFIER
from django.forms import SlugField

# Create your models here.
class Assets(models.Model):
    ID=IDENTIFIER
    Asset_tag=models.CharField
    Category_id=models.ForeignKey('Asset_Category')
    Description=models.CharField
    Active=models.BooleanField
    Location=models.ForeignKey('Asset_Location')
    Structural_Unit=models.ForeignKey('Structural_Unit')
    Date=models.DateField

class Maintenance(models.Model):
    ID=IDENTIFIER
    Notes=models.CharField
    Resolved=models.BooleanField
    Asset_id=models.ForeignKey('Assets')
    Date=models.DateField

class Asset_Category:
    ID=IDENTIFIER
    Category_Name=models.CharField
    Slug=models.SlugField
    Active=models.BooleanField

class Asset_Location:
    ID=IDENTIFIER
    Asset_Location=models.CharField
    Active_time=models.IntegerField
    isActive=models.BooleanField

class Asset_Ownership:
    ID=IDENTIFIER
    Ownership_Type=models.CharField
    Owner_Name=models.ForeignKey('django.users.db')
    Asset_ID=models.ForeignKey('Assets')
    Is_Active=models.BooleanField

class Structural_Unit:
    ID=IDENTIFIER
    Struct_Unit=models.CharField
    Owner_Name=models.ForeignKey('Asset_Ownership')