#!/usr/bin/env python3
""" Convert a Google Plus Code to latitude/longitude """
import sys
import googlemaps
import os.path
with open(os.path.join(os.path.dirname(__file__),'map.key'),'r') as keyfile:
    key = keyfile.readline().strip()
if len(sys.argv) <= 1:
    print(f'{sys.argv[0]}  pluscode', file=sys.stderr)
    sys.exit(1)
coord = ' '.join(sys.argv[1:])
if '°' in coord and coord[0] in 'NS':
    # put the hemisphere at the end of the coordinates to make Lightroom happy
    # N 40° 53.982 W 072° 52.167 ==> 40° 53.982 N 072° 52.167 W
    print(' '.join([sys.argv[i] for i in (2,3,1,5,6,4)]))
else:
    gmaps = googlemaps.Client(key=key)
    try:
        result = gmaps.geocode(' '.join(sys.argv[1:]))[0]['geometry']['location']
        print(f"{result['lat']},{result['lng']}")
    except (KeyError, IndexError):
        sys.stderr.write(f"Can't convert {coord}\n")
        print(sys.argv[1:])


