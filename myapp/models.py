from django.db import models

# Create your models here.
class District(models.Model):
	pid = models.IntegerField()
	district_name = models.CharField(max_length=255)
	class Meta:
		db_table = "district" 