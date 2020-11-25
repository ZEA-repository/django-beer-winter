from django.db import models


class Bar(models.Model):
	class Meta:
		verbose_name_plural = "Bar"

	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200, unique=True) 

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return f"{self.id}/"


class Address(models.Model):
	class Meta:
		verbose_name_plural = "Address"

	bar = models.ForeignKey(Bar, on_delete=models.CASCADE, default="", null=True)
	lat = models.FloatField(unique=True)
	lon = models.FloatField(unique=True)
	description = models.CharField(max_length=200, null=True, blank=True, default=None)

	def __str__(self):
		return f"{self.lat, self.lon, self.description}"

	def get_absolute_url(self):
		return f"{self.id}/"
