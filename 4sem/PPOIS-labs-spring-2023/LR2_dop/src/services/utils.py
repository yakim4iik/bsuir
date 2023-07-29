import os
import json


class FileUtils:
    """
    Some utils for handling file access
    """
    @staticmethod
    def is_file_exists(path: str) -> bool:
        """
        Checks if a file exists at the specified path.

        :param path: the path to the file
        :type path: str
        :return: True if the file exists, False otherwise
        :rtype: bool
        """
        return os.path.isfile(path)

    @staticmethod
    def read_from_json(path: str) -> dict:
        """
        Reads data from a JSON file at the specified path.

        :param path: the path to the JSON file
        :type path: str
        :return: the data read from the file
        :rtype: dict
        """
        data = dict()

        with open(path, "r") as f:
            data = json.load(f)

        return data

    @staticmethod
    def save_in_json(state: dict, path: str) -> None:
        """
        Saves data to a JSON file at the specified path.

        :param state: the data to be saved
        :type state: dict
        :param path: the path to the JSON file
        :type path: str
        :raises Exception: if the path is None
            """
        if path is None:
            raise Exception()

        with open(path, "w") as f:
            json.dump(state, f)
