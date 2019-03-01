import sympy
import sympy.physics.quantum as quantum_operations
import sympy.physics.quantum.qubit as qubit_operations


class QubitOperations:
    def __init__(self,
                 static_initialization_operations_object):
        self.static_initialization_operations_object = static_initialization_operations_object

    def gate_to_matrix(self,
                       gate_matrix: sympy.Matrix,
                       number_of_qubits_the_gate_operates_on: int,
                       total_number_of_qubits: int,
                       lowest_index_qubit_of_gate_operation: int):

        pre_gate_identity = \
            self.static_initialization_operations_object.generate_identity_matrix_given_number_of_qubits(
                number_of_qubits=(lowest_index_qubit_of_gate_operation - 1))

        post_gate_qubits = \
            total_number_of_qubits - (lowest_index_qubit_of_gate_operation + number_of_qubits_the_gate_operates_on)

        post_gate_identity = \
            self.static_initialization_operations_object.generate_identity_matrix_given_number_of_qubits(
                number_of_qubits=post_gate_qubits)

        return quantum_operations.TensorProduct(pre_gate_identity, gate_matrix, post_gate_qubits)
