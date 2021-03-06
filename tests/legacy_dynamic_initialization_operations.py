from src import dynamic_initialization_operations
from src import data_interpretation
from src import initialization_operations
from src import read_write_operations
from src import circuit_parser
from src import qubit_operations
from . import get_test_data

import sympy
import sympy.physics.quantum.qubit as qubit_operations

test_data_path = get_test_data.GetTestData().get_test_data_path()

data_interpretation_operations_object = data_interpretation.DataInterpretationOperations()
static_initialization_operations_object = initialization_operations.InitializationOperations()
read_write_operations_object = read_write_operations.ReadWriteOperations(
    data_path=test_data_path,
    data_interpretation_operations_object=data_interpretation_operations_object)

qubit_operations_object = qubit_operations.QubitOperations(
    static_initialization_operations_object=static_initialization_operations_object)

circuit_parser_object = circuit_parser.CircuitParser(
    data_interpretation_operations_object=data_interpretation_operations_object,
    qubit_operations=qubit_operations_object)

dynamic_initialization_operations_object = dynamic_initialization_operations.DynamicInitializationOperations(
    data_interpretation_operations_object=data_interpretation_operations_object,
    read_write_operations_object=read_write_operations,
    static_initialization_operations_object=static_initialization_operations_object,)


def test_matrix_to_qubit_notation_for_two_qubits(self):
    two_qubit_matrix = self.return_expected_matrix_for_arbitrary_qubit_state_initialization(
        number_of_qubits=2)

    two_qubit_dirac = qubit_operations.matrix_to_qubit(two_qubit_matrix)

    assert two_qubit_dirac == static_initialization_operations_object.initialize_qubit_dirac_with_arbitrary_states(
        number_of_qubits=2)


def test_matrix_to_qubit_notation_for_five_qubits(self):
    two_qubit_matrix = self.return_expected_matrix_for_arbitrary_qubit_state_initialization(
        number_of_qubits=5)

    two_qubit_dirac = qubit_operations.matrix_to_qubit(two_qubit_matrix)

    assert two_qubit_dirac == static_initialization_operations_object.initialize_qubit_dirac_with_arbitrary_states(
        number_of_qubits=5)
