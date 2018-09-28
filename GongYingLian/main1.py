from GongYingLian import readFile
from comment import util
import time
import numpy as np
import pandas as pd
from collections import defaultdict
import csv

train = pd.read_csv("../../GongYingLian/goodsaleSort.csv");
print(train);