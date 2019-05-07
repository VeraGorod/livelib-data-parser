# coding=utf-8
import os
from helpers.file_handler import FileHandler


class LivelibDataCollector:
    def __init__(self, filename: str):
        self._filename = filename

    def collect(self):
        data = list()
        requests = FileHandler.read_json_file_to_array(self._filename)
        for index, request in enumerate(requests):
            data.append(self.__collect_data(request))
        return data

    def __collect_data(self, request):
        file_path_array = self._filename.rsplit('\\', 1)
        if len(file_path_array) > 1:
            filename = str(request['file'])
            real_path = os.path.join(file_path_array[0], filename)
            return FileHandler.read_json_file_to_array(real_path)
        else:
            file_path_array = self._filename.rsplit('/', 1)
            filename = str(request['file'])
            real_path = os.path.join(file_path_array[0], filename)
            return FileHandler.read_json_file_to_array(real_path)
