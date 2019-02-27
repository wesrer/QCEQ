from pathlib import Path
import src
import os


class GetTestData:
    def __init__(self):
        self.source_path = os.path.dirname(os.path.abspath(src.__file__))
        self.test_data_path = os.path.dirname(os.path.abspath(__file__))

    def get_source_path(self):
        return Path(self.source_path)

    def get_test_data_path(self):
        return Path(self.test_data_path) / 'test_data'

