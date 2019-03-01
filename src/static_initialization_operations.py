import sympy
import typing

StringDict = typing.Dict[str, str]
MatrixDict = typing.Dict[str, sympy.Matrix]


class StaticInitializationOperations:
    def __init__(self):
        pass

    @staticmethod
    def initialize_qubit_matrices_with_arbitrary_states(number_of_qubits: int) -> sympy.Matrix:
        qubit_column_list = [sympy.symbols('a_' + str(x)) for x in range(2 ** number_of_qubits)]

        return sympy.Matrix(qubit_column_list)

    # Made this a static method because it's a pure function and does
    # not depend on object state
    def qubit_matrix_for_zero(self,
                              number_of_qubits: int) -> sympy.Matrix:
        qubit_column_list = \
            self.generate_zero_column_list_for_matrices(2 ** number_of_qubits)

        qubit_column_list[0] = 1

        return sympy.Matrix(qubit_column_list)

    def qubit_matrix_for_one(self,
                             number_of_qubits: int) -> sympy.Matrix:
        qubit_column_list =\
            self.generate_zero_column_list_for_matrices(2 ** number_of_qubits)

        qubit_column_list[(2 ** number_of_qubits) - 1] = 1

        return sympy.Matrix(qubit_column_list)

    @staticmethod
    def generate_zero_column_list_for_matrices(number_of_cols):
        return [0] * number_of_cols

