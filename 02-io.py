#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import json
import sys


if sys.version_info[0] < 3:
    import codecs
    open = codecs.open


def read_text(filename, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as f:
        return f.read()

def write_text(text, filename, encoding='utf-8'):
    with open(filename, 'w', encoding=encoding) as f:
        f.write(text)


def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def write_json(data, filename, indent=2):
    # TODO: [ensure ascii](http://stackoverflow.com/a/18337754/1054939)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=indent)
