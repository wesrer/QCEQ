import sympy
from . import data_interpretation
from . import read_write_operations
from . import dynamic_initialization_operations
from . import static_initialization_operations
from . import circuit_parser
from pathlib import Path
from os.path import dirname, abspath


class Application:
    def __init__(self):
        self.data_interpretation_object = data_interpretation.DataInterpretationOperations()

        self.source_path = Path(dirname(abspath(__file__))) / '..' / 'data'

        self.read_write_operations_object = \
            read_write_operations.ReadWriteOperations(
                data_path=self.source_path,
                data_interpretation_operations_object=self.data_interpretation_object)

        self.circuit_parser_object = circuit_parser.CircuitParser(
            data_interpretation_operations_object=self.data_interpretation_object)

        self.static_initialization_operations_object = \
            static_initialization_operations.StaticInitializationOperations()

        self.dynamic_initialization_operations_object = \
            dynamic_initialization_operations.DynamicInitializationOperations(
                data_interpretation_operations_object=self.data_interpretation_operations_object,
                read_write_operations_object=self.read_write_operations_object,
                static_initialization_operations_object=self.static_initialization_operations_object)

    def on_start_operations(self):
        gates_dictionary = \
            self.dynamic_initialization_operations_object.initialize_gates()

        return gates_dictionary

    def handle_input(self):
        return 'test_circuit.json'

    def run_equation(self):
        gates_dictionary = self.on_start_operations()
        circuit_file_name = self.handle_input()

        number_of_qubits, transformations_list = self.dynamic_initialization_operations_object.initialize_circuit(
            circuit_file_name=circuit_file_name)

        qubit_matrix = self.static_initialization_operations_object.initialize_qubit_matrices_with_arbitrary_states(
                number_of_qubits=number_of_qubits)



    def on_close_operations(self):
        pass
