import sympy
import sympy.physics.quantum.qubit as qubit_operations

from typing import List

MatrixList = List[sympy.Matrix]
StringList = List[str]
QubitList = List[qubit_operations.Qubit]


class ComputeTransformations:
    def __init__(self,
                 data_interpretation_operations_object,
                 circuit_parser_object):
        self.data_interpretation_operations_object = data_interpretation_operations_object
        self.circuit_parser_object = circuit_parser_object

    def compute_circuit(self,
                        circuit_list: StringList,
                        quantum_register: qubit_operations) -> QubitList:

        return self.circuit_parser_object.circuit_parser(circuit_list=circuit_list,
                                                         quantum_register=quantum_register)

