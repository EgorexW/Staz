import requests

ACCESS_KEY = '656d03ab8936ca69c67727f8cfc8a299'

def GetFlights(departure, arrival):

    params = {
        'access_key': ACCESS_KEY,
        'dep_iata': departure,
        'arr_iata': arrival,
        'flight_status': 'active'
    }
    api_response = GetRequest(params)
    return api_response['data']


def GetRequest(params):
    print("Waiting for request...")
    api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
    print("Request completed.")
    api_response = api_result.json()
    return api_response


def PrintFlights(flights):
    if len(flights) == 0:
        print('No flights')
    for flight in flights:
        print(u'%s flight %s from %s (%s) to %s (%s) is in the air.' % (
            flight['airline']['name'],
            flight['flight']['iata'],
            flight['departure']['airport'],
            flight['departure']['iata'],
            flight['arrival']['airport'],
            flight['arrival']['iata']))

DEPARTURE = 'ZRH'
ARRIVAL = 'YYZ'
PrintFlights(GetFlights(DEPARTURE, ARRIVAL))