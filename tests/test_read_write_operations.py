from src import read_write_operations
from . import get_test_data

get_test_data_object = get_test_data.GetTestData()
test_data_path = get_test_data_object.get_test_data_path()

read_write_operations_object = \
    read_write_operations.ReadWriteOperations(data_path=test_data_path)


class TestReadWriteOperations:
    def test_json_to_dict(self):
        test_json_path = test_data_path / 'test_json_to_read.json'

        expected_dict = {
            "1": "this is some random data to read",
            "2": {
                "1": "this is nested random data",
                "2": ["this", "is", "a", "list", "of", "random", "data"]
            }
        }
        returned_dict = \
            read_write_operations_object.json_to_dict(path_of_file=test_json_path)

        assert expected_dict == returned_dict
