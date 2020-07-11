
'''
    Purpose: run Jupyter Notebook within a virtual environment for exposing models using a custom package setup.
    Problem: simply running 'jupyter notebook' from within your venv doesn't link the notebook with your venv.
    Solution: add your venv as a kernel and select it when running jupyter notebook.
    Note: pip is not thread safe.
    Work around: run pip as a subprocess.
    Preliminaries:
    1. create virtual environment
    python -m venv venv
    2. copy setup_venv.py (this file) and data for analysis into venv
    3. activate virtual environment
    Run setup_venv.py and run Jupyter Notebook:
    4. run setup_venv.py
    python setup_venv.py
    5. run Jupyter Notebook
    jupyter notebook
    6. From the 'New' drop-down menu (on the right) under 'Notebook:' select 'venv' (not Python 3) 
'''

import sys
import subprocess

# implement pip as subprocess
# update pip and wheel
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', 'pip', 'wheel'])

# install IPython kernel
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', 'ipykernel'])

# add virtual environment (named 'venv') as a kernel
subprocess.check_call([sys.executable, '-m', 'ipykernel', 'install', '--user', '--name=venv'])

# install custom packages
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', 'pandas'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', 'matplotlib'])
