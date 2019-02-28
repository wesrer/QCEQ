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
    def parse_string_to_sympy_matrix(string_to_parse: str) -> sympy.ImmutableMatrix:
        pass

    # TODO: add a returntype, which is probably going to a be a list of things
    @staticmethod
    def parse_gate_operation_grammar(string_to_parse):
        pass

    @staticmethod
    def generate_Dirac_notations_from_qubits(starting_matrix: sympy.ImmutableMatrix):
        return qubit_operations.matrix_to_qubit(starting_matrix)





