# coding=utf-8
import os

import requests

from exporters.json.livelib_json_exporter import LivelibJsonExporter
from helpers.file_handler import FileHandler
from parsers.abstract_parser import AbstractParser
from helpers import livelibNoveltiesParser


class LivelibParser(AbstractParser):
    def __init__(self):
        super().__init__()
        self.__export_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'common_results', 'livelib')
        self.__data_dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'temp_results', 'livelib')
        self.__data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'temp_results', 'livelib', 'main.json')

    def start(self):
        url = 'https://www.livelib.ru/'
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }

        result = requests.request("get", url, headers=headers, timeout=10)
        result.encoding = 'utf-8'
        books = livelibNoveltiesParser.parse(result.text)

        self.__write_temp_data(books)

    def export_json(self):
        exporter = LivelibJsonExporter(self.__data_path, self.__export_path)
        exporter.export()

    # noinspection PyBroadException
    def __write_temp_data(self, books):
        for index, book in enumerate(books):
            try:
                ready_array = FileHandler.read_json_file_to_array(self.__data_path)
            except Exception:
                ready_array = list()
            if not book['title'] == '' and not book['id'] == '' and not book['author'] == '' and not book['img'] == '':
                file_with_car_data = os.path.join(self.__data_dir_path, str(index + 1) + '.json')
                FileHandler.write_array_to_json_file(book, file_with_car_data)
                try:
                    ready_array[index] = {'id': index + 1, 'file': str(index + 1) + '.json',
                                          'source_id': str(book['id'])}
                except Exception:
                    ready_array.append({'id': index + 1, 'file': str(index + 1) + '.json', 'source_id': str(book['id'])})
                FileHandler.write_array_to_json_file(ready_array, self.__data_path)

