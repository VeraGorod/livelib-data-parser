# coding=utf-8
import json
import os


class FileHandler:
    def __init__(self):
        pass

    @staticmethod
    def read_txt_file_to_array(filename):
        with open(filename, encoding="utf-8") as file:
            array = [row.strip() for row in file]
        return array

    @staticmethod
    def read_json_file_to_array(filename):
        with open(filename, encoding='utf-8') as file:
            array = json.loads(file.read())
        return array

    @staticmethod
    def write_array_to_json_file(data, filename):
        FileHandler.check_and_create_path(filename)
        with open(filename, "w", encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)

    @staticmethod
    def check_directory(directory):
        if not directory == '' and not os.path.exists(directory):
            os.makedirs(directory)

    @staticmethod
    def read_simple_txt_file(filename):
        with open(filename, encoding="utf-8") as file:
            data = file.read()
        return data

    @staticmethod
    def write_simple_txt_file(filename, data):
        FileHandler.check_and_create_path(filename)
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(data)

    @staticmethod
    def write_simple_xml_file(filename, data):
        FileHandler.check_and_create_path(filename)
        data.write(filename, encoding="utf-8")

    @staticmethod
    def check_and_create_path(path):
        array = path.split('\\')
        partial_path = ''
        if len(array) > 1:
            array = array[:-1]
            for directory in array:
                partial_path = partial_path + directory
                if ':' not in directory:
                    FileHandler.check_directory(partial_path)
                partial_path += '\\'
        else:
            array = path.split('/')
            partial_path = ''
            if len(array) > 1:
                array = array[:-1]
                for directory in array:
                    partial_path = partial_path + directory
                    if ':' not in directory:
                        FileHandler.check_directory(partial_path)
                    partial_path += '/'


