import sympy
from src import initialization_operations
from . import get_test_data

import sympy.physics.quantum.qubit as qubit_operations

static_initialization_operations_object = initialization_operations.InitializationOperations()


class TestStaticInitializationOperations:
    @staticmethod
    def return_expected_matrix_for_arbitrary_qubit_state_initialization(number_of_qubits: int):
        qubit_list = [sympy.symbols('a_' + str(x)) for x in range(2 ** number_of_qubits)]

        return sympy.Matrix(qubit_list)

    @staticmethod
    def return_expected_matrix_for_zero_qubit_initialization(number_of_qubits: int):
        qubit_list = [0] * (2 ** number_of_qubits)
        qubit_list[0] = 1

        return sympy.Matrix(qubit_list)

    def test_zero_qubit_matrix_initialization_for_two_qubits(self):
        expected_output = self.return_expected_matrix_for_zero_qubit_initialization(
            number_of_qubits=2)

        returned_output = static_initialization_operations_object.initialize_qubit_matrices_with_zero(
            number_of_qubits=2)

        sympy.pprint(returned_output)

        assert expected_output.equals(returned_output)

    def test_zero_qubit_matrix_initialization_for_three_qubits(self):
        expected_output = self.return_expected_matrix_for_zero_qubit_initialization(
            number_of_qubits=3)

        returned_output = static_initialization_operations_object.initialize_qubit_matrices_with_zero(
            number_of_qubits=3)

        assert expected_output.equals(returned_output)

    def test_arbitrary_matrix_qubit_initialization_for_five_qubits(self):
        expected_output = self.return_expected_matrix_for_arbitrary_qubit_state_initialization(
            number_of_qubits=5)

        returned_output = static_initialization_operations_object.initialize_qubit_matrices_with_arbitrary_states(
            number_of_qubits=5)

        assert expected_output.equals(returned_output)

    def test_initialization_of_CNOT_gate(self):
        expected_result = \
            sympy.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

        gate_dictionary = dynamic_initialization_operations_object.initialize_gates_from_file()

        assert expected_result.equals(gate_dictionary["CX"])

