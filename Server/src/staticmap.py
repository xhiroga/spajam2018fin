GOOGLE_MAPS_STATIC_MAP_ENDPOINT = "https://maps.googleapis.com/maps/api/staticmap"
GOOGLE_MAPS_API_KEY = "AIzaSyAVvDiYWi12dWl91LsNtQ2RVsSe3aa736A" # Personal Key of Nao Haida

class Staticmap():
    def __init__(self, path_points, sugoroku_points):
        self.path_points = path_points
        self.sugoroku_points = sugoroku_points

    # About Static Maps: https://developers.google.com/maps/documentation/maps-static/intro
    # About Styled Maps: https://developers.google.com/maps/documentation/maps-static/styling
    def create_map(self):
        params = []
        params_hash = []

        # Google Maps API Request Parameter Settings
        params_hash.append({'key': "size", 'val': "564x396"})
        params_hash.append({'key': "format", 'val': "png"})
        params_hash.append({'key': "key", 'val': GOOGLE_MAPS_API_KEY})
        params_hash.append({'key': "language", 'val': 'ja'})
        #params_hash.append({'key': "zoom", 'val': "8"})
        #params_hash.append({'key': "center", 'val': "Tokyo"})

        # Write path to the map
        path_points = []
        for i in range(len(self.path_points)):
            path_points.append(str(self.path_points[i]['latitude']) + ',' + str(self.path_points[i]['longitude']))
        params_hash.append({'key': 'path', 'val': "color:0x0000ff|weight:5|" + '|'.join(path_points)})

        # Put sugoroku_pooints on the map
        # &markers=color:blue%7Clabel:S%7C62.107733,-145.541936
        for i in range(len(self.sugoroku_points)):
            params_hash.append({'key': "markers", 'val': "color:blue%7Clabel:" + str(i + 1) + "%7C" + str(self.sugoroku_points[i]['latitude']) + ',' + str(self.sugoroku_points[i]['longitude'])})

        # Construct API URL
        for i in range(len(params_hash)):
            params.append(params_hash[i]['key'] + "=" + params_hash[i]['val'])
        url = GOOGLE_MAPS_STATIC_MAP_ENDPOINT + '?' + '&'.join(params)
        return url

## Example Codes
"""
# Staticmap test
path_points = [{'latitude': 35.2465552, 'longitude': 139.0449135},{'latitude': 35.2459945, 'longitude': 139.0728085}, {'latitude': 35.246765, 'longitude': 139.136580}, {'latitude': 35.244872, 'longitude': 139.127052}, {'latitude': 35.241087, 'longitude': 139.121817}, {'latitude':35.236881, 'longitude': 139.115894}, {'latitude': 35.232885, 'longitude': 139.101818}, {'latitude': 35.232324, 'longitude': 139.091518}, {'latitude': 35.235128, 'longitude': 139.078815}, {'latitude': 35.241437, 'longitude': 139.065426},{'latitude': 35.243540, 'longitude': 139.059246}, {'latitude': 35.241297, 'longitude': 139.054955}, {'latitude': 35.254054, 'longitude': 139.050320}, {'latitude': 35.258120, 'longitude': 139.040363}, {'latitude': 35.261624, 'longitude': 139.027145}, {'latitude': 35.2347075, 'longitude': 139.0348702},{'latitude': 35.263726, 'longitude': 139.013069}, {'latitude': 35.261484, 'longitude': 139.004658}, {'latitude': 35.256157, 'longitude': 139.000710}, {'latitude': 35.2530038, 'longitude': 138.9700691}]

sugoroku_points = [{'latitude': 35.2465552, 'longitude': 139.0449135},{'latitude': 35.246765, 'longitude': 139.136580}, {'latitude': 35.241087, 'longitude': 139.121817}, {'latitude': 35.232885, 'longitude': 139.101818}, {'latitude': 35.235128, 'longitude': 139.078815}, {'latitude': 35.243540, 'longitude': 139.059246}, {'latitude': 35.258120, 'longitude': 139.040363},  {'latitude': 35.2347075, 'longitude': 139.0348702}, {'latitude': 35.261484, 'longitude': 139.004658}, {'latitude': 35.2530038, 'longitude': 138.9700691}]

staticmap = Staticmap(path_points, sugoroku_points)
url = staticmap.create_map()
print(url)
"""
