import sympy
import typing
import sympy.physics.quantum.qubit as qubit_operations

from pathlib import Path

StringDict = typing.Dict[str, str]
MatrixDict = typing.Dict[str, sympy.Matrix]
QuantumRegisterList = typing.List[qubit_operations.Qubit]


class InitializationOperations:
    def __init__(self,
                 read_write_operations_object):
        self.read_write_operations_object = read_write_operations_object

    def initialize_circuit(self, circuit_file_name: Path) -> QuantumRegisterList:

        number_of_qubits, circuit_list = self.read_write_operations_object.read_circuit_from_path(
                circuit_file_name=circuit_file_name)

        quantum_register = self.initialize_quantum_register_with_quantum_states(
            number_of_qubits=number_of_qubits)

        transformations_list = self.circuit_parser_object.circuit_parser(
            circuit_list=circuit_list,
            quantum_register=quantum_register)

        return transformations_list

    def initialize_quantum_register_with_quantum_states(self,
                                                        number_of_qubits: int):

        qubit_matrix = self.initialize_qubit_matrices_with_arbitrary_states(number_of_qubits=number_of_qubits)
        return qubit_operations.matrix_to_qubit(qubit_matrix)

    @staticmethod
    def initialize_qubit_matrices_with_arbitrary_states(number_of_qubits: int) -> sympy.Matrix:

        qubit_column_list = [sympy.symbols('a_' + str(x)) for x in range(2 ** number_of_qubits)]

        return sympy.Matrix(qubit_column_list)


