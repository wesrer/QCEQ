import sympy
from . import data_interpretation
from . import read_write_operations
from . import initialization_operations


class Application:
    def __init__(self):
        self.data_interpretation_object = data_interpretation.DataInterpretationOperations()

        self.read_write_operations_object = \
            read_write_operations.ReadWriteOperations(self.data_interpretation_object)

        self.initialization_operations_object = \
            initialization_operations.InitializationOperations(
                data_interpretation_operations_object=self.data_interpretation_operations_object,
                read_write_operations_object=self.read_write_operations_object)

    def on_start_operations(self):
        gates_dictionary = self.initialization_operations_object.initialize_gates()
        qubit_matrix = self.initialization_operations_object.initialize_qubits_with_zero()

        return gates_dictionary, qubit_matrix,

    def on_close_operations(self):
        pass
