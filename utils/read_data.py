import pytest
import json
from utils.path_creator import PathCreator


class ReadData:

    @staticmethod
    def load_test_data(file_path: str) -> list:
        """
        Load test data from JSON file
        Supports multiple test scenarios
        """

        file_path = PathCreator.relative_path_creator(file_path=file_path)

        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            pytest.fail(f"Test data file not found: {file_path}")
        except json.JSONDecodeError:
            pytest.fail(f"Invalid JSON in file: {file_path}")
