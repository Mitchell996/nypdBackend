from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import numpy as np
import pandas as pd
from api.models import conviction
from api.serializers import convictionSerializer


#class getCSV(APIView):
 #   @csrf_exempt
  #  def get(self, request, format=None):
   #     cats = conviction.objects.all()
    #    df = pd.DataFrame(cats)
     #   df.to_csv()



class CreateConviction(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        body = json.loads(request.body)
        newSale = conviction()
        newSale.ARREST_BORO = body["ARREST_BORO"]
        newSale.ARREST_PRECINCT = body["ARREST_PRECINCT"]
        newSale.JURISDICTION_CODE = body["JURISDICTION_CODE"]
        newSale.AGE_GROUP = body["AGE_GROUP"]
        newSale.PERP_SEX = body["PERP_SEX"]
        newSale.PERP_RACE = body["PERP_RACE"]
        newSale.DRUG_RELATED = body["DRUG_RELATED"]
        newSale.LONGITUDE = body["LONGITUDE"]
        newSale.WEEKDAY = body["WEEKDAY"]
        newSale.save()
        return Response({
            'ARREST_BORO': newSale.ARREST_BORO,
            'DRUG_RELATED':newSale.DRUG_RELATED,
            })

    
