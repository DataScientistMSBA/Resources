# coding: utf-8

# # Package Loader



get_ipython().run_line_magic('run', '"./PackageLoader.ipynb"')




import os, sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'Package', 'scripts')))
from Python.Configuration.PackageInstaller import *




os.getcwd()


# # Package Installer



PackageInstaller()


# # Update Packages



UpdatePackages()

