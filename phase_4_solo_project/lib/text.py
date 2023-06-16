from datetime import datetime, timedelta
import os
from twilio.rest import Client

DELIVERY_MINS = 30


class TextConfirmation():

    def __init__(self, order, timer=datetime, client=Client):

        self.order = order
        self._timer = timer
        self._client = client


    def set_delivery_time(self):
        current_time = self._timer.now()
        new_time = current_time + timedelta(minutes=30)
        new_time_format = datetime.strftime(new_time, "%H:%M")
        return new_time_format
    

    def format_message(self):
        
        if self.order.current_order == {}:
            raise Exception("No items on the order")

        time_to_deliver = self.set_delivery_time()

        return f"Thank you! Your order was placed and will be delivered before {time_to_deliver}"
        

    def send_text(self, user_number, from_number="+447360268885"):

        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = self._client(account_sid, auth_token)

        message = client.messages \
                .create(
                     body=self.format_message(),
                     from_=from_number,
                     to=user_number
                 )

        print(message.sid)
        return message.sid
    


        




