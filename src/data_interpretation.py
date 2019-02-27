import json
import typing
import pathlib
import sympy

StringDict = typing.Dict[str]


class DataInterpretationOperations:
    def __init__(self):
        pass


    @staticmethod
    def json_to_dict(path_of_file: pathlib.Path) -> typing.Dict:

        with path_of_file.open() as f:
            data = json.load(f)

        return data

    @staticmethod
    def parse_string_to_sympy_matrix(string_to_parse: str) -> sympy.ImmutableMatrix:
        pass

