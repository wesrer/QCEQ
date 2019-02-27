import json
import typing
from pathlib import Path


class ReadWriteOperations:
    def __init__(self, data_path):
        self.data_path = data_path

    # FIXME: handle read errors
    def read_circuit_from_path(self,
                               circuit_file_name:str = "circuit.json") -> typing.Dict:
        circuit_path = self.data_path / 'circuits' / circuit_file_name

        return self.json_to_dict(path_of_file=circuit_path)

    def read_gates(self,
                   gates_file_name:str = 'gates.json') -> typing.Dict:
        gates_file_path = self.data_path / gates_file_name

        return self.json_to_dict(path_of_file=gates_file_path)

    @staticmethod
    def json_to_dict(path_of_file: Path) -> typing.Dict:

        with path_of_file.open() as f:
            data = json.load(f)

        return data
