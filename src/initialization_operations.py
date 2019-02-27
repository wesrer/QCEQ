import sympy
import typing

StringDict = typing.Dict[str]


class InitializationOperations:
    def __init__(self,
                 data_interpretation_operations_object,
                 read_write_operations_object):
        self.data_interpretation_operations_object = data_interpretation_operations_object

        self.read_write_operations_object = read_write_operations_object

    def initialize_gates(self) -> typing.Dict:
        gate_dictionary = self.read_write_operations_object.read_gates()

        for gate, gate_matrix in gate_dictionary.items():

            convert_item_to_sympy_expression = \
                lambda x: sympy.sympify(x)

            convert_string_matrix_row_to_sympy_matrix_row = \
                lambda row: map(convert_item_to_sympy_expression, row)

            map(convert_string_matrix_row_to_sympy_matrix_row, gate_matrix)




    def initialize_circuit(self,
                           circuit_json_string: str) -> typing.Dict:
        pass

    def get_gate_dictionary
