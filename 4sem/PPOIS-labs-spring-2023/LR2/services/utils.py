import os
import json


class FileUtils:
    @staticmethod
    def is_file_exists(path: str) -> bool:
        return os.path.isfile(path)

    @staticmethod
    def read_from_json(path: str) -> dict:
        data = dict()

        with open(path, "r") as f:
            data = json.load(f)

        return data

    @staticmethod
    def save_in_json(state: dict, path: str) -> None:
        if path is None:
            raise Exception()

        with open(path, "w") as f:
            json.dump(state, f)
