# coding=utf-8
from parsers.livelib_parser import LivelibParser

parser = LivelibParser()
parser.start()
parser.export_json()