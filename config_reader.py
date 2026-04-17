import json


class ConfigReader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigReader, cls).__new__(cls)

            with open("config.json") as f:
                cls._instance.data = json.load(f)
        return cls._instance

    def test_data(self):
        return self.data["test_data"]

    def main_url(self):
        return self.data["main_url"]