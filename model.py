import pandas as pd
from pandas import DataFrame as df
import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import pickle

data = pd.read_csv('uk_data.csv', header=1,low_memory=False)

data_2 = data.tail(35)

