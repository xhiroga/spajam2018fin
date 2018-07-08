import urllib

GOOGLE_MAPS_STATIC_MAP_ENDPOINT = "https://maps.googleapis.com/maps/api/staticmap"
GOOGLE_MAPS_API_KEY = "AIzaSyAVvDiYWi12dWl91LsNtQ2RVsSe3aa736A" # Personal Key of Nao Haida
MARKER_COLOR_CODE = "0xF02B60"
PATH_COLOR_CODE = "0xF02B60FF"
IMAGE_CONVERTER_HOST_NAME = "https://retravel-node.herokuapp.com"
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
        params_hash.append({'key': "size", 'val': "1128x792"})
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
            path_points.append(str(self.path_points[i]['latitude']) + ',' + str(self.path_points[i]['longitude']))
        params_hash.append({'key': 'path', 'val': "color:"+ PATH_COLOR_CODE + "|weight:3|" + '|'.join(path_points)})

        # Put sugoroku_pooints on the map
        # TODO: Should restrict #of markers less than 13
        for i in range(len(self.sugoroku_points)):
            icon_label = ""
            if(i == 0):
                icon_label = "size:mid%7Ccolor:" + MARKER_COLOR_CODE + "%7Clabel:S%7C"
            elif(i > 0 and i < len(self.sugoroku_points) - 1):
                icon_label = "size:mid%7Ccolor:" + MARKER_COLOR_CODE + "%7Clabel:" + str(i)+ "%7C"
            elif(i!= 0 and i == len(self.sugoroku_points) -1):
                icon_label = "size:mid%7Ccolor:" + MARKER_COLOR_CODE + "%7Clabel:G%7C"

            params_hash.append({'key': "markers", 'val': icon_label + str(self.sugoroku_points[i]['latitude']) + ',' + str(self.sugoroku_points[i]['longitude'])})

        # Construct API URL
        for i in range(len(params_hash)):
            params.append(params_hash[i]['key'] + "=" + params_hash[i]['val'])
        googleMapsUrl = GOOGLE_MAPS_STATIC_MAP_ENDPOINT + '?' + '&'.join(params)

        # Add Overlay
        converter_url = IMAGE_CONVERTER_HOST_NAME + "/addBadge?" + urllib.urlencode([('baseUrl', googleMapsUrl)])
        result = None
        try :
            result = urllib.urlopen(converter_url).read()
        except ValueError :
            print ("Access Failed")

        return result

## Example Codes
"""
path_points = [{'latitude': 35.2465552, 'longitude': 139.0449135},{'latitude': 35.2459945, 'longitude': 139.0728085}, {'latitude': 35.246765, 'longitude': 139.136580}, {'latitude': 35.244872, 'longitude': 139.127052}, {'latitude': 35.241087, 'longitude': 139.121817}, {'latitude':35.236881, 'longitude': 139.115894}, {'latitude': 35.232885, 'longitude': 139.101818}, {'latitude': 35.232324, 'longitude': 139.091518}, {'latitude': 35.235128, 'longitude': 139.078815}, {'latitude': 35.241437, 'longitude': 139.065426},{'latitude': 35.243540, 'longitude': 139.059246}, {'latitude': 35.241297, 'longitude': 139.054955}, {'latitude': 35.254054, 'longitude': 139.050320}, {'latitude': 35.258120, 'longitude': 139.040363}, {'latitude': 35.261624, 'longitude': 139.027145}, {'latitude': 35.2347075, 'longitude': 139.0348702},{'latitude': 35.263726, 'longitude': 139.013069}, {'latitude': 35.261484, 'longitude': 139.004658}, {'latitude': 35.256157, 'longitude': 139.000710}, {'latitude': 35.2530038, 'longitude': 138.9700691}]

sugoroku_points = [{'latitude': 35.2465552, 'longitude': 139.0449135},{'latitude': 35.246765, 'longitude': 139.136580}, {'latitude': 35.241087, 'longitude': 139.121817}, {'latitude': 35.232885, 'longitude': 139.101818}, {'latitude': 35.235128, 'longitude': 139.078815}, {'latitude': 35.243540, 'longitude': 139.059246}, {'latitude': 35.258120, 'longitude': 139.040363},  {'latitude': 35.2347075, 'longitude': 139.0348702}, {'latitude': 35.261484, 'longitude': 139.004658}, {'latitude': 35.2530038, 'longitude': 138.9700691}]

staticmap = Staticmap(path_points, sugoroku_points)
url = staticmap.create_map()
print(url)
"""
