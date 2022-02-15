import requests
import pprint
import time

class TrafficMonitor(object):
    # Google Direction Endpoint
    API_URL = "https://maps.googleapis.com/maps/api/directions/json"

    def __init__(self, origin="", destination="", key=""):
        self._origin = origin
        self._destination = destination
        self._key = key
        self._last_result = None

    def load_config(self):
        pass

    def get_link(self, outbound=True, origin=None, destination=None):
        if origin is None:
            if outbound:
                origin = self._origin
            else:
                origin = self._destination
        if destination is None:
            if outbound:
                destination = self._destination
            else:
                destination = self._origin

        origin = "+".join(origin.split(" "))
        destination = "+".join(destination.split(" "))
        return f"{TrafficMonitor.API_URL}?\
origin={origin}\
&destination={destination}\
&key={self._key}\
&mkde=driving\
&departure_time=now"

    def get_data(self, outbound=True, origin=None, destination=None):
        res = None
        print(self.get_link(outbound, origin, destination))

        # Requests to read the URL
        if outbound:
            res = requests.get(self.get_link(outbound, origin, destination))
            print(origin, destination)
        else:
            res = requests.get(self.get_link(outbound, destination, origin))
            print(origin, destination)

        # if res.status_code != 200:
            # raise Exception()
        
        res = res.json()
        self._last_result = res

        # pprint.pprint(res)
        print(f"Outbound: {outbound}")

        km = res["routes"][0]["legs"][0]["distance"]["value"] / 1000
        # minute = res["routes"][0]["legs"][0]["duration"]["value"] / 60
        minute = res["routes"][0]["legs"][0]["duration_in_traffic"]["value"] / 60

        return(km, minute)

        # print(f'{res["routes"][0]["legs"][0]["distance"]["value"] / 1000}')
        # print(f'{res["routes"][0]["legs"][0]["duration"]["value"] / 60}')

    def write_to_file(self):
        if self._last_fetch is None:
            print("No data to write!")
            return
        pass
