from unittest.mock import Mock
from lib.text import *
import pytest
from datetime import datetime

"""
format message with no items on the order raises error
"""
def test_format_message_no_order():
    mock_order = Mock()
    mock_order.current_order = {}
    text_confirmation = TextConfirmation(mock_order)
    with pytest.raises(Exception) as err:
        text_confirmation.format_message()
    assert str(err.value) == "No items on the order"


"""
cost of order is 
formats message correctly
"""
def test_raise_error_when_send_text_called_and_no_order_is_placed():
    mock_order = Mock()
    mock_order.current_price = 70
    
    mock_time = Mock()
    mock_time.now.return_value = datetime.strptime("14:09", "%H:%M")

    text_confirmation = TextConfirmation(mock_order, mock_time)
    assert text_confirmation.format_message() == f"Thank you! Your order was placed and will be delivered before 14:39"


"""
sends text with correct message
"""
