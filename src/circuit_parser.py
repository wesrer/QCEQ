from typing import Dict, List
from sympy.physics.quantum.qubit import Qubit
from sympy import pprint
from copy import deepcopy

from src.exceptions import UndefinedGateException, CircuitGrammarException
from src import quantum_gates

StringList = List[str]
QuantumRegisterList = List[Qubit]
TransformationDict = Dict[str, QuantumRegisterList]


class CircuitParser:
    def __init__(self,
                 data_interpretation_operations_object):
        self.data_interpretation_operations_object = data_interpretation_operations_object
        self.quantum_gates_object = quantum_gates.QuantumGates()

    def circuit_parser(self,
                       circuit_list: StringList,
                       quantum_register: Qubit) -> TransformationDict:

        # the states need to be deepcopied in order to preserve the quantum states after each gate operation
        # so that they can be transformed into a step in the mathematical output
        initial_state = {
            "current_gate": "base",
            "state": deepcopy(quantum_register)
        }
        transformation_list = [initial_state]

        for single_gate_transformation in circuit_list:
            gate_name, gate_parameters = self.parse_gate_operation_grammar(single_gate_transformation)

            quantum_register = self.parse_gate_grammar(gate_name=gate_name,
                                                       gate_parameters=gate_parameters,
                                                       quantum_register=quantum_register)

            single_state = {
                "current_gate": single_gate_transformation,
                "state": deepcopy(quantum_register)
            }

            transformation_list.append(single_state)

        return transformation_list

    @staticmethod
    def parse_gate_operation_grammar(single_gate_transformation: str) -> (str, StringList):

        gate_name, gate_parameters = single_gate_transformation.split("(")

        # splitting the arguments inside the Gate operations, and making them a list
        gate_parameters = gate_parameters.replace(')', '').split(",")

        return gate_name, gate_parameters

    # FIXME: this should parse every single gate grammar differently
    def parse_gate_grammar(self,
                           gate_name: str,
                           gate_parameters: StringList,
                           quantum_register: Qubit) -> Qubit:
        expected_gate_parameters = 1

        try:
            gate_name = gate_name.lower()

            # These are the only two multi qubit gates currently implemented
            if gate_name == "swap" or gate_name == "cnot":
                expected_gate_parameters = 2

            if len(gate_parameters) != expected_gate_parameters:
                raise CircuitGrammarException

            if gate_name == "h":
                return self.quantum_gates_object.hadamard(target_qubit=int(gate_parameters[0]),
                                                          quantum_register=quantum_register)
            elif gate_name == "s":
                return self.quantum_gates_object.s(target_qubit=int(gate_parameters[0]),
                                                   quantum_register=quantum_register)
            elif gate_name == "x":
                return self.quantum_gates_object.x(target_qubit=int(gate_parameters[0]),
                                                   quantum_register=quantum_register)
            elif gate_name == "z":
                return self.quantum_gates_object.z(target_qubit=int(gate_parameters[0]),
                                                   quantum_register=quantum_register)
            elif gate_name == "y":
                return self.quantum_gates_object.y(target_qubit=int(gate_parameters[0]),
                                                   quantum_register=quantum_register)
            elif gate_name == "t":
                return self.quantum_gates_object.t(target_qubit=int(gate_parameters[0]),
                                                   quantum_register=quantum_register)
            elif gate_name == "swap":
                return self.quantum_gates_object.swap(target_qubit_1=int(gate_parameters[0]),
                                                      target_qubit_2=int(gate_parameters[1]),
                                                      quantum_register=quantum_register)
            elif gate_name == "cnot":
                return self.quantum_gates_object.cnot(control_qubit=int(gate_parameters[0]),
                                                      target_qubit=int(gate_parameters[1]),
                                                      quantum_register=quantum_register)
            else:
                raise UndefinedGateException

        except CircuitGrammarException as e:
            pass
        except UndefinedGateException as e:
            pass


