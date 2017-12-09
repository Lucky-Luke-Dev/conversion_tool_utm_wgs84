'''
Conversion Tool UTM - WGS84
This program is a command line tool to convert coordinates from one world coordinate system to the other one in both
directions. It asks the user in which direction to convert and in which angle format (Decimal or Degrees, Minutes, Seconds)
the user will enter the locations. The user inserts one coordinate per line and as many as he wants.
'''

import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Conversion Tool UTM - WGS84')
parser.add_argument('DIRECTION', type=str, help='Choose the target coordinate system (UTM or WGS84)')
parser.add_argument('ANGLE_FORMAT', type=str, help='Choose input/output format for WGS84 (decimal or DMS)')
args = parser.parse_args()

dir = args.DIRECTION
format = args.ANGLE_FORMAT

coordinates = list()
if dir == 'WGS84' and format == 'decimal':
    print('Type in your coordinates for conversion.\n' +
          'Lat/Lon separated by comma, Multiple coordinates separated by Return\n' +
          '(e.g. +50.77552, -6.08432)')
elif dir == 'WGS84' and format == 'DMS':
    print('Type in your coordinates for conversion.\n' +
          'North/East separated by comma without symbols, Multiple coordinates separated by Return\n' +
          '(e.g. 50 46 30.2, 6 5 2.5213)')
elif dir == 'UTM':
    print('Type in your coordinates for conversion.\n' +
          'North/East/Zonenumber/Hemisphere separated by comma, Multiple coordinates separated by Return\n' +
          '(e.g. 5481745.123, 461344.432, 32U, N)')

while True:
    number = input()
    if number == '':
        print('Thanx for your input!')
        break
    else:
        coord = number.split(',')
        if format == 'DMS' and len(coord) == 2:
            north = coord[0].split(' ')
            east = coord[1].split(' ')
            try:
                north = np.array(north, dtype=float)
                east = np.array(east, dtype=float)
                coordinates.append([north, east])
            except:
                print('Invalid input!')

        elif dir == 'UTM' and len(coord) == 4:
            try:
                north = float(coord[0])
                east = float(coord[1])
                zone = coord[2]
                hemi = str(coord[3])
                coordinates.append([north, east, zone, hemi])
            except:
                print('Invalid input!')

        elif format == 'decimal' and len(coord) == 2:
            try:
                lat = float(coord[0])
                lon = float(coord[1])
                coordinates.append([lat, lon])
            except:
                print('Invalid input')
        else:
            print('Invalid input')

print(coordinates)
