import sys
import os

pw = sys.argv[1]

print(pw)

from notebook.auth import passwd
hash = passwd(pw)
# probably a better way to get this path...
pth = os.path.expanduser('~/.jupyter/jupyter_notebook_config.py')
with open(pth, 'a') as f:
    f.write('\nc.NotebookApp.password = {!r}'.format(hash))