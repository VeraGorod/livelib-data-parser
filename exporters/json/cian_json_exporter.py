# coding=utf-8
import os
import sys

from exporters.cian_data_collector import CianDataCollector
from ..json_exporter import JsonExporter
sys.path.append(os.path.join(os.pardir, os.pardir))
from helpers.file_handler import FileHandler


class CianJsonExporter(JsonExporter):
    def __init__(self, filename: str, export_path: str):
        super().__init__(filename, export_path)
        self.__export_file = str(self._export_path) + '.json'
        FileHandler.check_and_create_path(self.__export_file)
        self.__array = list()

    def export(self):
        collector = CianDataCollector(self._filename)
        for elem in collector.collect():
            self.__write_to_json(elem)
        self.__create_json()

    # noinspection PyMethodMayBeStatic
    def __write_to_json(self, data):
        self.__array.append(data)

    def __create_json(self):
        # noinspection PyBroadException
        try:
            os.remove(self.__export_file)
        except Exception:
            pass
        FileHandler.write_array_to_json_file(self.__array, self.__export_file)
