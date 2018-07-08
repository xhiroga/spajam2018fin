GOOGLE_MAPS_STATIC_MAP_ENDPOINT = "https://maps.googleapis.com/maps/api/staticmap"
GOOGLE_MAPS_API_KEY = "AIzaSyAVvDiYWi12dWl91LsNtQ2RVsSe3aa736A" # Personal Key of Nao Haida
MAP_STYLE = [
  {
    "elementType": "geometry",
    "stylers": [
      {
        "color": "0xf5f5f5"
      }
    ]
  },
  {
    "elementType": "labels.icon",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "saturation": 100
      },
      {
        "visibility": "on"
      },
      {
        "weight": 8
      }
    ]
  },
  {
    "featureType": "administrative.land_parcel",
    "elementType": "labels",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "administrative.land_parcel",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "0xbdbdbd"
      }
    ]
  },
  {
    "featureType": "landscape",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "color": "0xfed82a"
      }
    ]
  },
  {
    "featureType": "poi",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "0xeeeeee"
      }
    ]
  },
  {
    "featureType": "poi",
    "elementType": "labels.text",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "poi",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "0x757575"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "0xe5e5e5"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "0x9e9e9e"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "0xffffff"
      }
    ]
  },
  {
    "featureType": "road.arterial",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "0x757575"
      }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "0xdadada"
      }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "0x616161"
      }
    ]
  },
  {
    "featureType": "road.local",
    "elementType": "labels",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "road.local",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "0x9e9e9e"
      }
    ]
  },
  {
    "featureType": "transit.line",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "0xe5e5e5"
      }
    ]
  },
  {
    "featureType": "transit.station",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "0xeeeeee"
      }
    ]
  },
  {
    "featureType": "water",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "0xc9c9c9"
      }
    ]
  },
  {
    "featureType": "water",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "color": "0x6bc3d6"
      }
    ]
  },
  {
    "featureType": "water",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "0x9e9e9e"
      }
    ]
  }
]


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


        # Map Style
        for i in range(len(MAP_STYLE)):
            styles = []
            if('featureType' in MAP_STYLE[i]):
                styles.append('feature:' + MAP_STYLE[i]['featureType'])
            if('elementType' in MAP_STYLE[i]):
                styles.append('element:' + MAP_STYLE[i]['elementType'])
            if('stylers' in MAP_STYLE[i]):
                for k in range(len(MAP_STYLE[i]['stylers'])):
                    for key in MAP_STYLE[i]['stylers'][k]:
                        styles.append(key + ':' + str(MAP_STYLE[i]['stylers'][k][key]))
            params_hash.append({'key': "style", 'val': '|'.join(styles)})

        # Write path to the map
        path_points = []
        for i in range(len(self.path_points)):
            path_points.append(str(self.path_points[i]['lat']) + ',' + str(self.path_points[i]['lng']))
        params_hash.append({'key': 'path', 'val': "color:0x0000ff|weight:5|" + '|'.join(path_points)})

        # Put sugoroku_pooints on the map
        for i in range(len(self.sugoroku_points)):
            params_hash.append({'key': "markers", 'val': "color:blue%7Clabel:" + str(i + 1) + "%7C" + str(self.sugoroku_points[i]['lat']) + ',' + str(self.sugoroku_points[i]['lng'])})

        # Construct API URL
        for i in range(len(params_hash)):
            params.append(params_hash[i]['key'] + "=" + params_hash[i]['val'])
        url = GOOGLE_MAPS_STATIC_MAP_ENDPOINT + '?' + '&'.join(params)
        return url


## Example Codes
"""
path_points = [{'lat': 35.2465552, 'lng': 139.0449135},{'lat': 35.2459945, 'lng': 139.0728085}, {'lat': 35.246765, 'lng': 139.136580}, {'lat': 35.244872, 'lng': 139.127052}, {'lat': 35.241087, 'lng': 139.121817}, {'lat':35.236881, 'lng': 139.115894}, {'lat': 35.232885, 'lng': 139.101818}, {'lat': 35.232324, 'lng': 139.091518}, {'lat': 35.235128, 'lng': 139.078815}, {'lat': 35.241437, 'lng': 139.065426},{'lat': 35.243540, 'lng': 139.059246}, {'lat': 35.241297, 'lng': 139.054955}, {'lat': 35.254054, 'lng': 139.050320}, {'lat': 35.258120, 'lng': 139.040363}, {'lat': 35.261624, 'lng': 139.027145}, {'lat': 35.2347075, 'lng': 139.0348702},{'lat': 35.263726, 'lng': 139.013069}, {'lat': 35.261484, 'lng': 139.004658}, {'lat': 35.256157, 'lng': 139.000710}, {'lat': 35.2530038, 'lng': 138.9700691}]

sugoroku_points = [{'lat': 35.2465552, 'lng': 139.0449135},{'lat': 35.246765, 'lng': 139.136580}, {'lat': 35.241087, 'lng': 139.121817}, {'lat': 35.232885, 'lng': 139.101818}, {'lat': 35.235128, 'lng': 139.078815}, {'lat': 35.243540, 'lng': 139.059246}, {'lat': 35.258120, 'lng': 139.040363},  {'lat': 35.2347075, 'lng': 139.0348702}, {'lat': 35.261484, 'lng': 139.004658}, {'lat': 35.2530038, 'lng': 138.9700691}]

staticmap = Staticmap(path_points, sugoroku_points)
url = staticmap.create_map()
print(url)
"""
