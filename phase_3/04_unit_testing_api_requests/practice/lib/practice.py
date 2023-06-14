import requests
import json

class ActivitySuggester:
    def __init__(self, requester):  # requester is usually `requests`
        self.requester = requester

    def suggest(self):
        response = self._make_request_to_api()
        return f"Why not: {response['activity']}"

    # This method calls an 'API' on the internet to get a random activity.
    # An API is a way of allowing programs to request data from other programs.
    def _make_request_to_api(self):
        response = requests.get("http://www.boredapi.com/api/activity")
        print(json.dumps(response.json(), indent=4))
        return response.json()

# Usage
# =====
activity_suggester = ActivitySuggester()
# activity_suggester.suggest() will return a different value every time

print(activity_suggester.suggest())
# Why not: Learn how to use a french press

print(activity_suggester.suggest())
# Why not: Hold a video game tournament with some friends