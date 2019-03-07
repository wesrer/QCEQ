import typing
from pathlib import Path
from sympy import latex

GatesList = typing.List[str]


class ReadWriteOperations:
    def __init__(self,
                 data_path: Path,
                 data_interpretation_operations_object):
        self.data_path = data_path
        self.data_interpretations_object = data_interpretation_operations_object

    # FIXME: handle read errors
    def read_circuit_from_path(self,
                               circuit_file_name: str) -> (int, GatesList):
        circuit_path = self.data_path / 'circuit' / circuit_file_name

        circuit = self.data_interpretations_object.json_to_dict(path_of_file=circuit_path)
        return int(circuit["Qubits"]), circuit["Circuit"]

    def read_gates(self,
                   gates_file_name:str = 'gates.json') -> typing.Dict:
        gates_file_path = self.data_path / gates_file_name

        return self.data_interpretations_object.json_to_dict(path_of_file=gates_file_path)

    @staticmethod
    def port_qubit_list_to_latex(qubit_state_list):
        latex_string = "\documentclass[12pt]{article} \n \\begin{document}"

        for state in qubit_state_list:
            latex_string += "\\begin{formula} \\rightarrow " + latex(state) + "\\end{formula} \smallskip\n \n"

        latex_string += "\\end{document}"

        return latex_string

    def write_latex_to_file(self, latex_string, latex_file_name):
        write_file_path = self.data_path / 'outputs' / latex_file_name

        with open(write_file_path, 'w') as outputfile:
            outputfile.write(latex_string)


