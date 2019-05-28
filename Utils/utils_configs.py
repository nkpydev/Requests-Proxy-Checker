import os
from os.path import exists
import csv
from Core.exceptions import ProxyCheckerDirHandlingError, ProxyCheckerRequestException

# ---- DIR Handling ---- #
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_PARENT_DIR = os.path.split(BASE_DIR)[0]
DATA_DIR = os.path.join(PROJECT_PARENT_DIR,'Data')
INPUT_FILE = os.path.join(DATA_DIR,'input.txt')
#print(INPUT_FILE)
OUTPUT_FILE = os.path.join(DATA_DIR,'output.csv')
#print(OUTPUT_FILE)