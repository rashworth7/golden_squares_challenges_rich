import requests
import json


class CatFacts:

    def __init__(self, requester=requests):
        self._requester = requester

    def provide(self):
        return f"Cat fact: {self._get_cat_fact()['fact']}"

    # Again, don't stub this method.
    def _get_cat_fact(self):
        response = self._requester.get("https://catfact.ninja/fact") ##
        return response.json() ####
    
# car_facts = CatFacts()
# print(json.dumps(car_facts._get_cat_fact(), indent = 4))