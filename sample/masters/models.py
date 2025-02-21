from django.db import models

# Create your models here.

class MetaData(models.Model):
	location_code = models.CharField(max_length=100)
	location = models.CharField(max_length=100)

	department_code = models.CharField(max_length=100)
	department = models.CharField(max_length=100)

	category_code = models.CharField(max_length=100)
	category = models.CharField(max_length=100)

	subcategory_code = models.CharField(max_length=100)
	subcategory = models.CharField(max_length=100)

class SKUdata(models.Model):
	sku = models.IntegerField()
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	subCategory = models.CharField(max_length=100)