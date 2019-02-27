import sympy
import typing
from sympy.physics.quantum import TensorProduct

StringDict = typing.Dict[str, str]
MatrixDict = typing.Dict[str, sympy.ImmutableMatrix]



class InitializationOperations:
    def __init__(self,
                 data_interpretation_operations_object,
                 read_write_operations_object):
        self.data_interpretation_operations_object = data_interpretation_operations_object

        self.read_write_operations_object = read_write_operations_object

    def initialize_gates(self) -> MatrixDict:
        gate_dictionary = self.read_write_operations_object.read_gates()

        def convert_string_matrix_row_to_sympy_matrix_row(row):
            list(map(lambda x: sympy.sympify(x),
                     row))

        for gate, gate_matrix in gate_dictionary.items():
            gate_matrix = list(map(convert_string_matrix_row_to_sympy_matrix_row,
                                   gate_matrix))

            gate_dictionary[gate] = sympy.ImmutableMatrix(gate_matrix)

        return gate_dictionary

    def initialize_qubits(self,
                          number_of_qubits: int):
        list_of_qubits = []
        for x in range(0, number_of_qubits):
            list_of_qubits[x] = sympy.ImmutableMatrix([1, 0])

        return TensorProduct(tuple(list_of_qubits))


    def initialize_circuit(self,
                           circuit_json_string: str) -> typing.Dict:
        pass

