# --- Generic Imports --- #
import os
from os.path import exists
import csv
# --- Project Internal Imports --- #
from Core.exceptions import ProxyCheckerDirHandlingError, ProxyCheckerRequestException

# ---- DIR Handling ---- #
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # BASE_DIR
PROJECT_PARENT_DIR = os.path.split(BASE_DIR)[0] # PARENT_DIR OF BASE_DIR
DATA_DIR = os.path.join(PROJECT_PARENT_DIR,'Data') # Data - Source of input.txt and output.csv
INPUT_FILE = os.path.join(DATA_DIR,'input.txt') # Input file, store your IPs to test inside this file.
OUTPUT_FILE = os.path.join(DATA_DIR,'output.csv') # Output file, the result will be stored into this.