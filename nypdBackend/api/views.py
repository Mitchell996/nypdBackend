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
import pyodbc


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
        #newSale = conviction()
        #newSale.ARREST_BORO = body["ARREST_BORO"]
        #newSale.ARREST_PRECINCT = body["ARREST_PRECINCT"]
        #newSale.JURISDICTION_CODE = body["JURISDICTION_CODE"]
        #newSale.AGE_GROUP = body["AGE_GROUP"]
        #newSale.PERP_SEX = body["PERP_SEX"]
        #newSale.PERP_RACE = body["PERP_RACE"]
        #newSale.DRUG_RELATED = body["DRUG_RELATED"]
        #newSale.LONGITUDE = body["LONGITUDE"]
        #newSale.WEEKDAY = body["WEEKDAY"]
        #newSale.save()


        server = 'isserver2020.database.windows.net'
        database = 'NYPD'
        username = 'jboy7977'
        password = 'C00ties8119036!'
        driver= '{ODBC Driver 17 for SQL Server}'
        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        #cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
        cursor.execute("INSERT INTO FinalNYPDData (ARREST_BORO, ARREST_PRECINCT, JURISDICTION_CODE, AGE_GROUP, PERP_SEX, PERP_RACE, DRUG_RELATED, LONGITUDE, WEEKDAY)VALUES(" + body["ARREST_BORO"]+","+body["ARREST_PRECINCT"]+","+ body["JURISDICTION_CODE"]+","+body["AGE_GROUP"]+","+body["PERP_SEX"]+","+body["PERP_RACE"]+","+body["DRUG_RELATED"]+","+body["LONGITUDE"]+","+body["WEEKDAY"]+")")
        #row = cursor.fetchone()
        #while row:
        #    print (str(row[0]) + " " + str(row[1]))
        #    row = cursor.fetchone()



        return Response({
            'ARREST_BORO': body["ARREST_BORO"],
            'DRUG_RELATED':body["DRUG_RELATED"],
            })

    
