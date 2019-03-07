import sympy
import sympy.physics.quantum as quantum_operations
import sympy.physics.quantum.qubit as qubit_operations


class QubitOperations:
    def __init__(self,
                 static_initialization_operations_object):
        self.static_initialization_operations_object = static_initialization_operations_object

    def qubit_matrix_for_zero(self,
                              number_of_qubits: int) -> sympy.Matrix:
        qubit_column_list = self.generate_zero_column_list_for_matrices(2 ** number_of_qubits)
        qubit_column_list[0] = 1

        return sympy.Matrix(qubit_column_list)

    def qubit_matrix_for_one(self,
                             number_of_qubits: int) -> sympy.Matrix:
        qubit_column_list = self.generate_zero_column_list_for_matrices(2 ** number_of_qubits)

        qubit_column_list[(2 ** number_of_qubits) - 1] = 1

        return sympy.Matrix(qubit_column_list)

    @staticmethod
    def generate_identity_matrix_given_number_of_qubits(number_of_qubits: int):
        return sympy.eye((2 ** number_of_qubits))

    @staticmethod
    def generate_zero_column_list_for_matrices(number_of_cols):
        return [0] * number_of_cols

