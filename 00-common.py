#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


#from __future__ import division, unicode_literals

from datetime import date, datetime, timedelta
from collections import Counter, defaultdict, namedtuple
import json
import os
import pickle
import re
import site
import sys

from matplotlib import pyplot as plt
from matplotlib import rcParams; oldparams = rcParams.copy()  # rcParams.update(oldparams)
import numpy as np
import pandas as pd
from pandas.io.packers import pack, unpack  # pickle이 느릴 때
import scipy as sp

from konlpy.tag import Twitter
from konlpy.utils import pprint

#import lzma
#from rpy2 import robjects as ro
#from rpy2.robjects.numpy2ri import numpy2ri as np2ri
#import shelve

#if not any(site.USER_SITE in p for p in sys.path):
#    known_paths = set(sys.path)
#    site.addusersitepackages(known_paths)
#    site.addsitedir(site.USER_SITE, known_paths)
#    sys.path[:] = list(known_paths) + sys.path
