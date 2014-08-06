from django.db import models

# Create your models here.
class player(models.Model):
	name = models.CharField(max_length=200)
	fight = models.FloatField(max_length=200)
	weight = models.FloatField(max_length=200)
	height = models.FloatField(max_length=200)
	rank = models.IntegerField(max_length=200)
	chest = models.FloatField(max_length=200)
	biceps = models.FloatField(max_length=200)
	def power(self):
		self.power = (weight * height) / rank
		return power
	def __str__(self):
		return self.name

	class Admin:
		pass