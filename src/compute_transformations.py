import sympy
from typing import List

MatrixList = List[sympy.Matrix]


class ComputeTransformations:
    def __init__(self,
                 data_interpretation_operations_object):
        self.data_interpretation_operations_object = data_interpretation_operations_object

    def compute_single_transformation(self,
                                      initial_qubit_matrix: sympy.Matrix,
                                      transformation_matrix: sympy.Matrix) -> sympy.Matrix:
        return transformation_matrix * initial_qubit_matrix

    def return_list_of_states(self,
                              list_of_transformations: MatrixList,
                              initial_qubit_state: sympy.Matrix):

        return_list = [initial_qubit_state.copy()]
        current_state = initial_qubit_state

        for single_transformation in list_of_transformations:
            current_state = self.compute_single_transformation(
                initial_qubit_matrix=current_state,
                transformation_matrix=single_transformation)
            return_list.append(current_state.copy())

        return return_list

    def return_list_of_states_in_dirac_notation(self,
                                                list_of_transformations: MatrixList,
                                                initial_qubit_state: sympy.Matrix):
        list_of_states = self.return_list_of_states(
            list_of_transformations=list_of_transformations,
            initial_qubit_state=initial_qubit_state)

        return [self.data_interpretation_operations_object.generate_Dirac_notations_from_qubit_matrices(x)
                for x in list_of_states]


