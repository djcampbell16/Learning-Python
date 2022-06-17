# Projects from the following link
# https://github.com/karan/Projects

# Distance Between Two Cities
# Calculates the distance between two cities and allows the user to specify a unit of distance.
# This program may require finding coordinates for the cities like latitude and longitude.

from geopy.geocoders import Nominatim
from geopy import distance
import random
demo_mode = False

def requestAddress():
    if demo_mode:
        rand1 = random.randint(0, 100)
        rand2 = random.randint(0, 100)

        if rand1 % 3 == 0:
            user_addresss1 = "50 Brookside Drive, Exeter, NH 03833"
        elif rand1 % 2 == 0:
            user_addresss1 = "100 Legends Way, Boston, MA 02114"
        else:
            user_addresss1 = "866 Waldo Lane, Wallingford, VT 05773"
        if rand2 % 3 == 0:
            user_addresss2 = "80 Edgecomb Avenue, New York, NY 10030"
        elif rand2 % 2 == 0:
            user_addresss2 = "188 Meeting St, Charleston, SC 29401"
        else:
            user_addresss2 = "24 Pine Street, Proctor, VT 05765"
    else:
        user_addresss1 = input("Please input the starting location: ")
        user_addresss2 = input("Please input the ending location: ")

    return user_addresss1, user_addresss2

def convertToLongLat(address1, address2):
    geolocator = Nominatim(user_agent="DanC Project")

    try:
        loc1 = geolocator.geocode(address1)
        loc2 = geolocator.geocode(address2)

        lat1 = loc1.latitude
        lon1 = loc1.longitude
        lat2 = loc2.latitude
        lon2 = loc2.longitude
    except:
        lat1 = 45
        lon1 = 40
        lat2 = 40
        lon2 = 45

    return [(lat1, lon1), (lat2, lon2)]

def convertUnits(distance):
    # Available units - miles, kilometers, fathoms
    userSelection = int(input("What units do you need? (1 - Miles, 2 - Kilometers, 3 - Fathoms): "))
    if userSelection == 2:
        return ("Kilometers", distance * 1.60934)
    elif userSelection == 3:
        return ("Fathoms", distance * 880)
    else:
        return ("Miles", distance)


def main():

    start_point, stop_point = requestAddress()

    coordinates = convertToLongLat(start_point, stop_point)

    coord_distance = distance.distance(coordinates[0], coordinates[1]).miles

    response = convertUnits(coord_distance)

    print(stop_point + " is " + str(round(response[1],2)) + " " + response[0].lower() + " from " + start_point)

if __name__ == '__main__':
    main()

