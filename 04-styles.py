#! /usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
from IPython.display import HTML, Javascript

publish_css = '''
<style>
.prompt {
    display: None;
}
</style>
'''

# publish: `HTML(publish_css)`

np.set_printoptions(precision=4, edgeitems=4)
pd.set_option('display.max_rows', 240)
