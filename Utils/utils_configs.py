import os
from os.path import exists
import csv

# ---- DIR Handling ---- #
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_PARENT_DIR = os.path.split(BASE_DIR)[0]
DATA_DIR = os.path.join(PROJECT_PARENT_DIR,'Data')

