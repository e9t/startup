#! /usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
from IPython.display import HTML, Javascript
from IPython.core.magic import register_cell_magic


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


# color print
def cprint(obj, color='red'):
    cmap = { 'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'magenta': 35, 'cyan': 36, 'white': 37 }
    print("\x1b[{}m{}\x1b[0m".format(cmap[color], obj))


# print csv
@register_cell_magic
def csv(line, cell):
    ''' Usage:

        %%csv
        a,b,c
        d,e,f
    '''
    string = '<table>'
    for rows in cell.split('\n'):
        string += '<tr><td>%s</td></tr>' % '</td><td>'.join(rows.split(','))
    string += '</table>'
    return HTML(string)
