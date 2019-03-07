import sympy
from . import data_interpretation
from . import read_write_operations
from . import dynamic_initialization_operations
from . import initialization_operations
from . import circuit_parser
from . import quantum_gates
from . import compute_transformations
from pathlib import Path
from os.path import dirname, abspath


class Application:
    def __init__(self):

        self.source_path = Path(dirname(abspath(__file__))) / '..' / 'data'

        self.data_interpretation_object = data_interpretation.DataInterpretationOperations()
        self.gate_initialization_operations = quantum_gates.QuantumGates()

        self.read_write_operations_object = read_write_operations.ReadWriteOperations(
                data_path=self.source_path,
                data_interpretation_operations_object=self.data_interpretation_object)

        self.initialization_operations_object = initialization_operations.InitializationOperations(
            read_write_operations_object=self.read_write_operations_object)

        self.circuit_parser_object = circuit_parser.CircuitParser(
            data_interpretation_operations_object=self.data_interpretation_object)

        self.compute_transformations_object = compute_transformations.ComputeTransformations(
            data_interpretation_operations_object=self.data_interpretation_object,
            circuit_parser_object=self.circuit_parser_object)

    def main(self):

        # legacy gates initialization
        # gates_dictionary = self.dynamic_initialization_operations_object.initialize_gates_from_file()

        circuit_file_name = self.handle_input()

        quantum_register, circuit_list = self.initialization_operations_object.initialize_circuit(
            circuit_file_name=circuit_file_name)

        transformations_list = self.compute_transformations_object.compute_circuit(
            circuit_list=circuit_list,
            quantum_register=quantum_register)

        latex_state_list = self.read_write_operations_object.port_qubit_list_to_latex(transformations_list)

    def handle_input(self):
        return 'test_circuit.json', 'test_latex.tex'

    def on_start_operations(self):
        pass

    def on_close_operations(self):
        pass
