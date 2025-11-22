# ====================================================================
# IMPORTS 
# ====================================================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import json
import sys
import time

# ====================================================================
# GLOBAL DATA
# ====================================================================

data = {}

# ====================================================================
# CONSTANTS
# ====================================================================

RED    = "\033[1;31m"
CYAN   = "\033[36m"
YELLOW = "\033[33m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

DATASET = "./data/data.csv"
SAVE_RESULT = "./data/result.json"
INIT_M = 0
INIT_C = 0
LEARN_RATE = 1
CONVERGE_LIMIT = 0.00001
ITERATION_LIMIT = 10000

ERR_READ  = f"{RED}❌ Training stopped. Failed to import data.csv{RESET}"
ERR_DATA  = f"{RED}❌ Training stopped. Invalid data{RESET}"
ERR_SMALL = f"{RED}❌ Training stopped. Not enough data{RESET}"

ERR_OUT_OF_RANGE = f"{RED}❌ Value out of range (0-999999){RESET}"
ERR_INVALID_TYPE  = f"{RED}❌ Invalid input: please enter an integer{RESET}"

USER_PROMPT = f"{YELLOW}Enter mileage value:{RESET} "