from pathlib import Path


class PathCreator:

    @staticmethod
    def relative_path_creator(file_path: str) -> str:
        """
        Creates a relative path to a file within the project directory.

        Args:
            file_path: The relative path to the file within the project.

        Returns:
            The absolute path to the file.
        """

        # Locate the root of the `pytest_project` directory
        current_file = Path(__file__).resolve()  # Current file's absolute path
        project_root = current_file.parents[1]  # Adjust this based on the directory depth
        print(project_root)

        # Construct the full path
        file_path = str(project_root / file_path)
        print(file_path)
        return file_path
