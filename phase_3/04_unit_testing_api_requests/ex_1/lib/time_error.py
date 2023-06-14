import time
import requests
import json

class TimeError:

    def __init__(self, requester=requests, timer=time):
        self._requester = requester
        self._timer = timer
    # Returns difference in seconds between the time on an external server
    # and the time on this computer
    def error(self):
        print(f"final answer {self._get_server_time() - self._timer.time()}")
        return self._get_server_time() - self._timer.time()

    # The underscore denotes this is a private method not to be called from the
    # outside. You also shouldn't stub it in your tests. So if your tests contain
    # the words `get_server_time`, you're on the wrong track.
    def _get_server_time(self):
        response = self._requester.get("https://worldtimeapi.org/api/ip")
        json_response = response.json()
        print(json.dumps(json_response, indent=4))
        return json_response["unixtime"]
    
time_error = TimeError()
print(time_error.error())
print(f" time now is {time.time()}") 