import sympy
from sympy import I, pi
import sympy.physics.quantum.gate as quantum_gates
import sympy.physics.quantum.qubit as qubit_operations
import sympy.physics.quantum.qapply as qapply
from sympy.physics.quantum.dagger import Dagger


class QuantumGates:
    def __init__(self):
        pass

    @staticmethod
    def hadamard(target_qubit: int,
                 quantum_register: qubit_operations.Qubit) -> qubit_operations.Qubit:
        return qapply(quantum_gates.HadamardGate(target_qubit) * quantum_register)

    @staticmethod
    def x(target_qubit: int,
          quantum_register: qubit_operations.Qubit) -> qubit_operations.Qubit:
        return qapply(quantum_gates.XGate(target_qubit) * quantum_register)

    def x_dag(self,
              target_qubit: int,
              quantum_register: qubit_operations.Qubit) -> qubit_operations.Qubit:
        return self.x(target_qubit=target_qubit,
                      quantum_register=quantum_register)

    @staticmethod
    def y(target_qubit: int,
          quantum_register: qubit_operations.Qubit) -> qubit_operations.Qubit:
        return qapply(quantum_gates.YGate(target_qubit) * quantum_register)

    def y_dag(self,
              target_qubit: int,
              quantum_register: qubit_operations.Qubit) -> qubit_operations.Qubit:
        return self.y(target_qubit=target_qubit,
                      quantum_register=quantum_register)

    @staticmethod
    def z(target_qubit: int,
          quantum_register: qubit_operations.Qubit) -> qubit_operations.Qubit:
        return qapply(quantum_gates.ZGate(target_qubit) * quantum_register)

    def z_dag(self,
              target_qubit: int,
              quantum_register: qubit_operations.Qubit) -> qubit_operations.Qubit:
        return self.z(target_qubit=target_qubit,
                      quantum_register=quantum_register)

    @staticmethod
    def t(target_qubit: int,
          quantum_register: qubit_operations.Qubit) -> qubit_operations.Qubit:
        return qapply(quantum_gates.TGate(target_qubit) * quantum_register)

    # FIXME:
    # def t_dag(self,
    #           target_qubit: int,
    #           quantum_register: qubit_operations.Qubit) -> qubit_operations.Qubit:
    #
    #     quantum_register_matrix = qubit_operations(quantum_register)
    #     number_of_qubits = sympy.simplify(sympy.log(quantum_register.shape[0]) / sympy.log(2))
    #
    #     complete_transformation = sympy.eye(target_qubit - 1)
    #
    #     t_dag_matrix = sympy.Matrix([[1, 0], [0, exp(-I * pi / 4)]])
    #     matrix_after_t_dag_operations = t_dag_matrix * target_qubit_matrix
    #     return qubit_operations.Qubit(matrix_after_t_dag_operations)

    @staticmethod
    def s(target_qubit: int,
          quantum_register: qubit_operations.Qubit) -> qubit_operations.Qubit:
        return qapply(quantum_gates.PhaseGate(target_qubit) * quantum_register)

    #FIXME
    # def s_dag(self,
    #           target_qubit: int,
    #           quantum_register: qubit_operations.Qubit) -> qubit_operations.Qubit:
    #     target_qubit_matrix = qubit_operations(target_qubit)
    #     s_dag_matrix = sympy.Matrix([[1, 0], [0, -I]])
    #     matrix_after_s_dag_operations = s_dag_matrix * target_qubit_matrix
    #     return qubit_operations.Qubit(matrix_after_s_dag_operations)

    @staticmethod
    def swap(target_qubit_1: int,
             target_qubit_2: int,
             quantum_register: qubit_operations.Qubit) -> qubit_operations.Qubit:
        return qapply(quantum_gates.SwapGate(target_qubit_1, target_qubit_2) * quantum_register)

    @staticmethod
    def cnot(control_qubit: int,
             target_qubit: int,
             quantum_register: qubit_operations.Qubit) -> qubit_operations.Qubit:
        return qapply(quantum_gates.CNotGate(control_qubit, target_qubit) * quantum_register)


