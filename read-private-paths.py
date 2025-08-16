#!/bin/python
import configparser
from sys import argv

global CFG_FILENAME
CFG_FILENAME = ".private.cfg"

if __name__ == "__main__":
    config = configparser.ConfigParser()
    with open(CFG_FILENAME, 'r', encoding='utf8') as f:
        config.read_file(f)
    paths = config.items(section=f"{argv[1]}-paths")
    for pair in paths:
        if pair[0] == argv[2]:
            print(pair[1])
