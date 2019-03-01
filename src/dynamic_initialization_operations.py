import sympy
import typing

StringDict = typing.Dict[str, str]
MatrixDict = typing.Dict[str, sympy.Matrix]


class DynamicInitializationOperations:
    def __init__(self,
                 data_interpretation_operations_object,
                 read_write_operations_object,
                 static_initialization_operations_object):
        self.data_interpretation_operations_object = data_interpretation_operations_object

        self.read_write_operations_object = read_write_operations_object
        self.static_initialization_operations_object = static_initialization_operations_object

    def initialize_gates(self) -> MatrixDict:
        gate_dictionary = self.read_write_operations_object.read_gates()

        for gate, gate_matrix in gate_dictionary.items():
            gate_matrix = \
                self.data_interpretation_operations_object.convert_string_matrix_to_sympy_matrix(
                    gate_matrix=gate_matrix)

            gate_dictionary[gate] = sympy.Matrix(gate_matrix)

        return gate_dictionary

    def initialize_qubit_dirac_with_arbitrary_states(self, number_of_qubits: int):
        qubit_matrix = self.static_initialization_operations_object.initialize_qubit_matrices_with_arbitrary_states(
            number_of_qubits=number_of_qubits)

        return self.data_interpretation_operations_object.generate_Dirac_notations_from_qubit_matrices(qubit_matrix)

    def initialize_circuit(self,
                           circuit_json_string: str) -> typing.Dict:
        pass

