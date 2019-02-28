from src import data_interpretation
from . import get_test_data

data_interpretation_operations_object = data_interpretation.DataInterpretationOperations()
test_data_path = get_test_data.GetTestData().get_test_data_path()


class TestDataInterpretations:
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
            data_interpretation_operations_object.json_to_dict(path_of_file=test_json_path)

        assert expected_dict == returned_dict

