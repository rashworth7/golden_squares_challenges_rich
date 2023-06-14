from unittest.mock import Mock
from lib.cat_facts import CatFacts

def test_provide_returns_cat_fact():

    request_mock = Mock()
    response_mock = Mock()

    request_mock.get.return_value = response_mock ##

    response_mock.json.return_value = {
        "fact": "Cats' hearing is much more sensitive than humans and dogs.",
        "length": 58
         } ####
    
    cat_facts = CatFacts(request_mock)
    result = cat_facts.provide()
    assert result == "Cat fact: Cats' hearing is much more sensitive than humans and dogs."