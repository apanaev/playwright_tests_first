import json


class ConfigReader:
    _instance = {}

    def __new__(cls, file_path):
        if file_path not in cls._instance:
            cls._instance[file_path] = super().__new__(cls)

            with open(file_path) as f:
                cls._instance[file_path].data = json.load(f)
        return cls._instance[file_path]

    @property
    def main_url(self):
        return self.data["main_url"]
