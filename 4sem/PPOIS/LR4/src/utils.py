import json


class FileUtils:

    @staticmethod
    def read_from_json(path: str):
        data = dict()

        with open(path, "r") as f:
            data = json.load(f)

        return data

    @staticmethod
    def save_in_json(state, path):
        with open(path, "w") as f:
            json.dump(state, f)
