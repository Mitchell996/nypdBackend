import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'nypdBackend.settings'
import django
import json
django.setup()

# regular imports
from api.models import conviction

# main script
def main():
    #categories will be a dictionary
    #key: string name of category
    #value: the actual category?
    with open('products.json') as json_file:
        data = json.load(json_file)
    campaigns = data['convictions']
    #fill in everything from products
    for prod in campaigns:
        dbprod = conviction()
        #dbprod.weekday = prod['weekday']
       #dbprod.WEEKDAY = prod['WEEKDAY']
      #"FIELD1": 0,
      #"ARREST_BORO": "K ",
      #"ARREST_PRECINCT": 66,
      #"JURISDICTION_CODE": 0,
      #"AGE_GROUP": "25-44",
      #"PERP_SEX": "M",
      #"PERP_RACE": "WHITE",
      #"Longitude": -73.990957907,
      #"DRUG_RELATED": false,
      #"WEEKDAY": "Saturday"
        dbprod.ARREST_BORO = prod['ARREST_BORO']
        dbprod.ARREST_PRECINCT = prod['ARREST_PRECINCT']
        dbprod.JURISDICTION_CODE = prod['JURISDICTION_CODE']
        dbprod.AGE_GROUP = prod['AGE_GROUP']
        dbprod.PERP_SEX = prod['PERP_SEX']
        dbprod.PERP_RACE = prod['PERP_RACE']
        dbprod.LONGITUDE = prod['Longitude']
        dbprod.DRUG_RELATED = prod['DRUG_RELATED']
        dbprod.WEEKDAY = prod['WEEKDAY']
        dbprod.save()
    
        
    

# bootstrap
if __name__ == '__main__':
    main()
