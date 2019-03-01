from typing import Dict, List
GatesList = List[str]


class CircuitParser:
    def __init__(self,
                 data_interpretation_operations_object,
                 qubit_operations,
                 initialized_gates):
        self.data_interpretation_operations_object = data_interpretation_operations_object
        self.gate_transformation_matrices = initialized_gates
        self.qubit_operations_object = qubit_operations

    def circuit_parser(self,
                       circuit_list: GatesList,
                       total_number_of_qubits: int):

        transformation_list = []
        for single_gate_transformation in circuit_list:
            gate_name, gate_parameters = \
                self.data_interpretation_operations_object.parse_gate_operation_grammar(single_gate_transformation)

            transformation_list.append(self.parse_gate_grammar(
                gate_name=gate_name,
                gate_parameters=gate_parameters,
                total_number_of_qubits=total_number_of_qubits))

        return transformation_list

    # FIXME: this should parse every single gate grammar differently
    def parse_gate_grammar(self,
                           gate_name: str,
                           gate_parameters: str,
                           total_number_of_qubits: int):

        number_of_qubits_the_gate_operates_on = \
            self.gate_transformation_matrices[gate_name]["NumberOfQubits"]

        gate_parameters = gate_parameters.split(",")

        transformationMatrix = \
            self.qubit_operations_object.gate_to_matrix(
                gate_matrix=self.gate_transformation_matrices[gate_name],
                number_of_qubits_the_gate_operates_on=number_of_qubits_the_gate_operates_on,
                total_number_of_qubits=total_number_of_qubits,
                lowest_index_qubit_of_gate_operation=int(gate_parameters[0]))

        return transformationMatrix

