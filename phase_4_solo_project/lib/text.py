import requests


class TextConfirmation():

    def __init__(self, order, requester=requests):
        # Parameters:
        #   Requester - for testing
        #   order: instance of the Order class
        pass

    def format_message(self):
        # No params
        # returns:
        #   formatted message with ETA/arrive before
        pass

    def send_text(self, from_number, user_number):
        # No params
        # returns nothing
        # Side effects:
        #   formats message and sends text to the user's number if order has been placed
        pass