import sympy
# from src import dynamic_initialization_operations
from src import data_interpretation
from src import read_write_operations
from src import initialization_operations
from . import get_test_data

import sympy.physics.quantum.qubit as qubit_operations

test_data_path = get_test_data.GetTestData().get_test_data_path()

data_interpretation_operations_object = data_interpretation.DataInterpretationOperations()

read_write_operations_object = read_write_operations.ReadWriteOperations(
                                    data_path=test_data_path,
                                    data_interpretation_operations_object=data_interpretation_operations_object)

static_initialization_operations_object = initialization_operations.InitializationOperations()

dynamic_initialization_operations_object = dynamic_initialization_operations.DynamicInitializationOperations(
        data_interpretation_operations_object=data_interpretation_operations_object,
        read_write_operations_object=read_write_operations_object,
        static_initialization_operations_object=static_initialization_operations_object)

class TestQuantumOperations:
    def test_CX_on_three_qubits(self):
        first_qubit_matrix = dynamic_initialization_operations_object.initialize_qubit_matrices_with_one(
            number_of_qubits=1)

        two_zero_qubit_matrices = dynamic_initialization_operations_object.initialize_qubit_matrices_with_zero(
            number_of_qubits=2)

        assert True

