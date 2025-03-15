import json
import os
from main import DataProcessor
import pytest


@pytest.fixture(scope="function")
def data_processor_fixture_data():
    path_to_test_file = "test_data_processor.json"

    process = DataProcessor(path_to_test_file)

    yield process

    os.remove(path_to_test_file)


@pytest.mark.data_processor
@pytest.mark.parametrize("data, ex_result",
                         [
                             (100, 100),
                             ("Hello World!", "Hello World!"),
                             ("", ""),
                             (None, None),
                             ([], [])
                         ])

def test_processor_data_positive(data_processor_fixture_data, data, ex_result):

    with open(data_processor_fixture_data.file_path, "a") as file:
        file.write(json.dumps(data))

    assert data_processor_fixture_data.load_data() == ex_result



@pytest.mark.data_processor
@pytest.mark.parametrize("data1, ex_result1, data2, ex_result2",
                         [
                             ("qwerty", "qwerty", 123456, 123456),
                             (None, None, [], []),
                             ("", "", [123], [123])
                         ])

def test_processor_data_negative(data_processor_fixture_data, data1, data2, ex_result1, ex_result2):

    index_data = {'data1' : data1,
                  'data2' : data2}

    with open(data_processor_fixture_data.file_path, "a") as file:
        file.write(json.dumps(index_data))

    assert data_processor_fixture_data.get_value('data1') == ex_result1
    assert data_processor_fixture_data.get_value('data2') == ex_result2