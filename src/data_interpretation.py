import json
import typing
import pathlib
import sympy
import sympy.physics.quantum.qubit as qubit_operations

StringDict = typing.Dict[str, str]


class DataInterpretationOperations:
    def __init__(self):
        pass

    @staticmethod
    def json_to_dict(path_of_file: pathlib.Path) -> typing.Dict:

        with path_of_file.open() as f:
            data = json.load(f)

        return data

    @staticmethod
    def convert_string_matrix_row_to_sympy_matrix_row(row):
        return list(map(lambda x: sympy.sympify(x), row))

    def convert_string_matrix_to_sympy_matrix(self, gate_matrix):
        return list(map(self.convert_string_matrix_row_to_sympy_matrix_row,
                        gate_matrix))





