import os
from main import Logger
import pytest


@pytest.fixture(scope="function")
def logger_fixture_data():
    path_to_test_file = "test_log.txt"

    logger = Logger(path_to_test_file)

    yield logger

    os.remove(path_to_test_file)


@pytest.mark.logger
@pytest.mark.parametrize("data, ex_result",
                         [
                             ("123", "123"),
                             ("qwerty", "qwerty"),
                             ("", "")
                         ])

def test_logger_log_positive(logger_fixture_data, data, ex_result):

    logger_fixture_data.log(data)

    assert logger_fixture_data.get_logs() == [f"{ex_result}\n"]



@pytest.mark.logger
@pytest.mark.parametrize("data, ex_result",
                         [
                             (None, TypeError),
                             (1234, TypeError),
                             (0.112314, TypeError)
                         ])

def test_logger_log_negative(logger_fixture_data, data, ex_result):

    with pytest.raises(ex_result):
        logger_fixture_data.log(data)