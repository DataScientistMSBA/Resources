# coding: utf-8



# %run "../Configuration/PackageLoader.ipynb"
# %run "./PackageLoader.ipynb"


# ## Standard Imports



import subprocess
import json
import os
import sys
import time
import re
import json


# # Aliased Imports



import pandas as pd
import numpy as np
import tkinter as tk


# # Specific Element Imports



from tkinter import messagebox









# import os, sys; sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'Package', 'scripts')))
# from Access.ReadDB import *
# from Access.WriteDB import *


# # Import Functions from Workbooks



import os; os.chdir(os.sep.join(os.getcwd().split(os.sep)[:os.getcwd().split(os.sep).index('Package') + 1]))

try:
    get_ipython().run_line_magic('run', '"notebooks/Python/Configuration/UpdatePackages.ipynb"')
except:
    get_ipython().run_line_magic('run', '"scripts/Python/Configuration/UpdatePackages.py"')

try:
    get_ipython().run_line_magic('run', '"notebooks/Python/Configuration/PackageInstaller.ipynb"')
except:
    get_ipython().run_line_magic('run', '"scripts/Python/Configuration/PackageInstaller.py"')

try:
    get_ipython().run_line_magic('run', '"notebooks/Access/ReadDB.ipynb"')
except:
    get_ipython().run_line_magic('run', '"scripts/Access/ReadDB.py"')

try:
    get_ipython().run_line_magic('run', '"notebooks/Access/WriteDB.ipynb"')
except:
    get_ipython().run_line_magic('run', '"scripts/Access/WriteDB.py"')






