from api.models import *
import pandas as pd
from django.conf  import settings
data = pd.read_csv(settings.BASE_DIR / 'api/indiadata.csv')
cityob = city.objects.filter(country__name = "India")
def load():
    print('working',len(cityob))
    count = 0
    for da in cityob:
        fdf = data[ (data["COUNTY"].str.lower() == da.name.lower()) & (data["STATE"].str.lower() == da.state.name.lower()) ]
        if len(fdf) > 0:
            bulkdata = [
                cityLocations(
                    city_id = da.id,
                    location = record['CITY'],
                    pincode = record['POSTAL_CODE'],
                    latitude = record['LATITUDE'],
                    longitude = record['LONGITUDE'],
                    communitiny = record['COMMUNITY'],
                )
                for record in fdf.to_dict('records')
            ]
            cityLocations.objects.bulk_create(bulkdata)
        count += 1
        print(F"{count} of {len(cityob)} {da.name} is done")