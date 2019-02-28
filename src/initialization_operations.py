import sympy
import typing

StringDict = typing.Dict[str, str]
MatrixDict = typing.Dict[str, sympy.ImmutableMatrix]


class InitializationOperations:
    def __init__(self,
                 data_interpretation_operations_object,
                 read_write_operations_object):
        self.data_interpretation_operations_object = data_interpretation_operations_object

        self.read_write_operations_object = read_write_operations_object

    def initialize_gates(self) -> MatrixDict:
        gate_dictionary = self.read_write_operations_object.read_gates()

        def convert_string_matrix_row_to_sympy_matrix_row(row):
            list(map(lambda x: sympy.sympify(x),
                     row))

        for gate, gate_matrix in gate_dictionary.items():
            gate_matrix = list(map(convert_string_matrix_row_to_sympy_matrix_row,
                                   gate_matrix))

            gate_dictionary[gate] = sympy.ImmutableMatrix(gate_matrix)

        return gate_dictionary

    # Made this a static method because it's a pure function and does
    # not depend on object state
    def initialize_qubit_matrices_with_zero(self,
                                            number_of_qubits: int) -> sympy.ImmutableMatrix:
        qubit_column_list = \
            self.generate_zero_column_list_for_matrices(2 ** number_of_qubits)
        qubit_column_list[0] = 1

        return sympy.ImmutableMatrix(qubit_column_list)

    def initialize_qubit_matrices_with_one(self,
                                           number_of_qubits: int) -> sympy.ImmutableMatrix:
        qubit_column_list =\
            self.generate_zero_column_list_for_matrices(2 ** number_of_qubits)
        qubit_column_list[(2 ** number_of_qubits) - 1] = 1

        return sympy.ImmutableMatrix(qubit_column_list)

    @staticmethod
    def initialize_qubit_matrices_with_arbitrary_states(number_of_qubits: int) -> sympy.ImmutableMatrix:
        qubit_column_list = [sympy.symbols('a_' + str(x)) for x in range(2 ** number_of_qubits)]

        return sympy.ImmutableMatrix(qubit_column_list)

    @staticmethod
    def generate_zero_column_list_for_matrices(number_of_cols):
        return [0] * number_of_cols

    def initialize_circuit(self,
                           circuit_json_string: str) -> typing.Dict:
        pass

