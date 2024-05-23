from flask import Flask, request, jsonify
import requests

ACCESS_KEY = '656d03ab8936ca69c67727f8cfc8a299'
app = Flask(__name__)


@app.get("/flights")
def GetFlightsApi():
    args = request.args
    departure = args.get("departure", default="", type=str)
    arrival = args.get("arrival", default="", type=str)

    output = GetFlights(departure, arrival)
    return output


def GetFlights(departure, arrival):
    params = {
        'access_key': ACCESS_KEY,
        'dep_iata': departure,
        'arr_iata': arrival,
        'flight_status': 'active'
    }
    api_response = GetRequest(params)
    flights = api_response['data']
    return PrintFlights(flights)


def GetRequest(params):
    print("Waiting for request...")
    api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
    print("Request completed.")
    api_response = api_result.json()
    return api_response


def PrintFlights(flights):
    output = ""
    if len(flights) == 0:
        output = "No flights"
    else:
        for flight in flights:
            output += (u'%s flight %s from %s (%s) to %s (%s) is in the air.' % (
                flight['airline']['name'],
                flight['flight']['iata'],
                flight['departure']['airport'],
                flight['departure']['iata'],
                flight['arrival']['airport'],
                flight['arrival']['iata']))
            output += u'\n'
    return output


# Testing code

DEPARTURE = 'DRW'
ARRIVAL = 'DPS'


@app.get("/default_flights")
def GetDefaultFlights():
    return GetFlights(DEPARTURE, ARRIVAL)


print(GetDefaultFlights())
