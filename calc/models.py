from django.db import models


class UserData(models.Model):
    user_id = models.CharField(max_length=50, default='')
    electricity_past = models.IntegerField(default="0")
    electricity_current = models.IntegerField(default="0")
    water_past = models.IntegerField(default="0")
    water_current = models.IntegerField(default="0")
    electricity_tariff = models.FloatField(default="0")
    water_tariff = models.FloatField(default="0")
