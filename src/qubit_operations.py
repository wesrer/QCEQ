import sympy
import sympy.physics.quantum as quantum_operations
import sympy.physics.quantum as qubit_operations

class QubitOperations:
    def __init__(self):
        pass

    def gate_to_matrix(self,
                       number_of_qubits_the_gate_operates_on: int,
                       total_number_of_qubits: int,
                       lowest_index_qubit_of_gate_operation: int):
