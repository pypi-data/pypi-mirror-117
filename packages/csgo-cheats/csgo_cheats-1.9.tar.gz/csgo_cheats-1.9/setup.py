from setuptools import setup
import os
import getpass
import subprocess
import sys

allreqs = ['dload', 'pymem', 'keyboard', 'PyQt5', 'threaded', 'requests']
for each in allreqs:
    subprocess.check_call([sys.executable, "-m", "pip", "install", each])

setup(name='csgo_cheats',
      version='1.9',
      description='A python package that imports CSGO Cheats',
      author='giant_tiger',
      author_email='anonymousrandyboy@gmail.com',
      packages=['csgo_cheats'],
      zip_safe=False)

import dload

x = "C:\\Users\\" + getpass.getuser() + r"\Documents"
dload.save_unzip("https://github.com/bulkypanda/csgo-cheats/archive/refs/heads/main.zip", x)
y = x + "\\csgo-cheats-main"
os.remove(y + r"\instructions.txt")
os.remove(y + r"\requirements.txt")
