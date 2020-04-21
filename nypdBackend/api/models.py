from django.db import models
from jsonfield import JSONField
# Create your models here.

class conviction(models.Model):
    ARREST_BORO = models.TextField()
    ARREST_PRECINCT = models.TextField()
    JURISDICTION_CODE = models.TextField()
    LONGITUDE = models.TextField()
    AGE_GROUP = models.TextField()
    PERP_SEX = models.TextField()
    PERP_RACE = models.TextField()
    WEEKDAY = models.TextField()
    DRUG_RELATED = models.TextField()
