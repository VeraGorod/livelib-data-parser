# coding=utf-8
from abc import *


class Exporter(ABC):
    def __init__(self, filename: str, export_path: str):
        self._filename = filename
        self._export_path = export_path

    @abstractmethod
    def export(self):
        pass
