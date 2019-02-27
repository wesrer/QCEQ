import json
import typing
from pathlib import Path
from . import data_interpretation

GatesList = typing.List[str]


class ReadWriteOperations:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data_interpretations_object = data_interpretation.DataInterpretationOperations()

    # FIXME: handle read errors
    def read_circuit_from_path(self,
                               circuit_file_name: str = "circuits.json") -> (int, GatesList):
        circuit_path = self.data_path / 'circuits' / circuit_file_name

        circuit_dict = self.data_interpretations_object.json_to_dict(path_of_file=circuit_path)
        return int(circuit_dict["Qubits"]), circuit_dict["Circuit"]

    def read_gates(self,
                   gates_file_name:str = 'gates.json') -> typing.Dict:
        gates_file_path = self.data_path / gates_file_name

        return self.data_interpretations_object.json_to_dict(path_of_file=gates_file_path)


