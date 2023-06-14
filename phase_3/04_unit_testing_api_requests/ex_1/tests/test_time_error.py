from unittest.mock import Mock
from lib.time_error import TimeError


def test_get_error_time():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {
    "unixtime": 1686740691,
}

    time_mock = Mock()
    time_mock_response = Mock()
    time_mock = time_mock_response
    time_mock.time.return_value = 1686740691.220405

    

    time_error = TimeError(requester_mock, time_mock)
    result = time_error.error()
    assert result == -0.22040510177612305

