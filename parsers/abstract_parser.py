# coding=utf-8
from abc import *


class AbstractParser(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def export_json(self):
        pass

