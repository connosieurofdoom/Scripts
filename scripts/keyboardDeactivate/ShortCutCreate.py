from pyshortcuts import make_shortcut

import pathlib
path = pathlib.Path(__file__).parent.absolute()
print(path)

import os

make_shortcut(os.path.join(path,'keyboardDeactivate.py'), name='keyboardDeactivate', icon=os.path.join(path,'keyboard.ico'))