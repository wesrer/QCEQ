import sympy
import typing

StringDict = typing.Dict[str]


class InitializationOperations:
    def __init__(self):
        pass

    def initialize_gates(self,
                         gate_dictionary: StringDict) -> typing.Dict:
        pass
        # for gate, gate_matrix in gate_dictionary.items():

    def initialize_circuit(self,
                           circuit_json_string: str) -> typing.Dict:
        pass

