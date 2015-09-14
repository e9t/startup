#! /usr/bin/python
# -*- coding: utf-8 -*-

# Configurations for notebook only

if 'terminal' not in str(get_ipython()):
    %matplotlib inline
    %config InlineBackend.figure_format = 'retina'

from matplotlib import pyplot as plt
from matplotlib import rcParams; oldparams = rcParams.copy()  # rcParams.update(oldparams)
