from src import read_write_operations
from src import data_interpretation
from . import get_test_data

get_test_data_object = get_test_data.GetTestData()
test_data_path = get_test_data_object.get_test_data_path()
data_interpretation_operations_object = data_interpretation.DataInterpretationOperations()

read_write_operations_object = read_write_operations.ReadWriteOperations(
                                    data_path=test_data_path,
                                    data_interpretation_operations_object=data_interpretation_operations_object)


class TestReadWriteOperations:
    def test_read_circuit(self):
        qubits, gates_list = \
            read_write_operations_object.read_circuit_from_path(circuit_file_name='test_circuit_1.json')

        expected_gates_list = ["X(0)", "X(1)"]

        assert qubits == 2 and gates_list == expected_gates_list

    #FIXME: test this after implementing, obviously
    def test_read_gates(self):
        assert True
