#! /usr/bin/python
# -*- coding: utf-8 -*-


from numpy.random import randn, randint


# a sample dataframe for testing purposes
n = 1000
df_s = pd.DataFrame({
    'a': randn(n),
    'b': randn(n),
    'c': randint(10, 200, (n)),
    'y': 'x'
})

df_n = pd.DataFrame({
    'movie': ['thg', 'thg', 'mol', 'mol', 'lob', 'lob'],
    'rating': [3., 4., 5., np.nan, np.nan, np.nan],
    'name': ['John', np.nan, 'N/A', 'Graham', np.nan, np.nan]
})
