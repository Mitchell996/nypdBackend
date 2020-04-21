from rest_framework import serializers

from api.models import conviction
# Serializers define the API representation.

class convictionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = conviction
        fields = ['ARREST_BORO', 'ARREST_PRECINCT', 'JURISDICTION_CODE',
        'DRUG_RELATED','LONGITUDE', 'AGE_GROUP', 'PERP_SEX','PERP_RACE','WEEKDAY']



