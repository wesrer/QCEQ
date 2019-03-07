import sympy
import typing
from pathlib import Path

StringDict = typing.Dict[str, str]
MatrixDict = typing.Dict[str, sympy.Matrix]


class DynamicInitializationOperations:
    def __init__(self,
                 quantum_gates_object,
                 data_interpretation_operations_object,
                 read_write_operations_object,
                 static_initialization_operations_object,
                 circuit_parser_object):

        self.quantum_gates_object = quantum_gates_object
        self.data_interpretation_operations_object = data_interpretation_operations_object
        self.read_write_operations_object = read_write_operations_object
        self.static_initialization_operations_object = static_initialization_operations_object
        self.circuit_parser_object = circuit_parser_object

    # FIXME: this is a legacy function offering an interesting alternative
    # FIXME: gate initialization operation, using json definitions
    # TODO: Figure out if this can be incorporated into
    def initialize_gates_from_file(self) -> MatrixDict:
        gate_dictionary = self.read_write_operations_object.read_gates()

        for gate, gate_matrix in gate_dictionary.items():
            gate_matrix = \
                self.data_interpretation_operations_object.convert_string_matrix_to_sympy_matrix(
                    gate_matrix=gate_matrix)

            gate_dictionary[gate] = sympy.Matrix(gate_matrix)

        return gate_dictionary

