#! /usr/bin/python
# -*- coding: utf-8 -*-


# a sample dataframe for testing purposes
n = 1000
sdf = pd.DataFrame({
    'a': randn(n),
    'b': randn(n),
    'c': randint(10, 200, (n)),
    'y': 'x'
})
