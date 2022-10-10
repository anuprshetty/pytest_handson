import json
import os

class Student:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        data_file = os.path.join(os.path.dirname(__file__), data_file)
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    def get_data(self, name):
        for student in self.__data["students"]:
            if student["name"] == name:
                return student

    def close(self):
        pass
