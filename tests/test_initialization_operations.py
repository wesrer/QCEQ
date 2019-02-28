import sympy
from src import initialization_operations
from src import data_interpretation
from src import read_write_operations
from . import get_test_data

test_data_path = get_test_data.GetTestData().get_test_data_path()

data_interpretation_operations_object = data_interpretation.DataInterpretationOperations()

read_write_operations_object = read_write_operations.ReadWriteOperations(
                                    data_path=test_data_path,
                                    data_interpretation_operations_object=data_interpretation_operations_object)

initialization_operations_object = initialization_operations.InitializationOperations(
                                    data_interpretation_operations_object=data_interpretation_operations_object,
                                    read_write_operations_object=read_write_operations_object)


class TestInitializationOperations:
    @staticmethod
    def return_expected_matrix_for_arbitrary_qubit_state_initialization(number_of_qubits: int):
        qubit_list = [sympy.symbols('a_' + str(x)) for x in range(2 ** number_of_qubits)]

        return sympy.ImmutableMatrix(qubit_list)

    @staticmethod
    def return_expected_matrix_for_zero_qubit_initialization(number_of_qubits: int):
        qubit_list = [0] * (2 ** number_of_qubits)
        qubit_list[0] = 1

        return sympy.ImmutableMatrix(qubit_list)

    def test_zero_qubit_matrix_initialization_for_two_qubits(self):
        expected_output = self.return_expected_matrix_for_zero_qubit_initialization(
            number_of_qubits=2)

        returned_output = initialization_operations_object.initialize_qubit_matrices_with_zero(
            number_of_qubits=2)

        sympy.pprint(returned_output)

        assert expected_output.equals(returned_output)

    def test_zero_qubit_matrix_initialization_for_three_qubits(self):
        expected_output = self.return_expected_matrix_for_zero_qubit_initialization(
            number_of_qubits=3)

        returned_output = initialization_operations_object.initialize_qubit_matrices_with_zero(
            number_of_qubits=3)

        assert expected_output.equals(returned_output)

    def test_arbitrary_matrix_qubit_initialization_for_five_qubits(self):
        expected_output = self.return_expected_matrix_for_arbitrary_qubit_state_initialization(
            number_of_qubits=5)

        returned_output = initialization_operations_object.initialize_qubit_matrices_with_arbitrary_states(
            number_of_qubits=5)

        assert expected_output.equals(returned_output)

    def test_matrix_to_qubit_notation_for_two_qubits(self):
        assert "something" == "something"

    def test_matrix_to_qubit_notation_for_five_qubits(self):
        assert "something" == "something"
