# coding=utf-8
from exporter import Exporter
from abc import *


class JsonExporter(Exporter, ABC):
    def __init__(self, filename: str, export_path: str):
        super().__init__(filename, export_path)

    @abstractmethod
    def export(self):
        pass