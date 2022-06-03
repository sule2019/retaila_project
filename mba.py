from flask import Flask, render_template, request

import pandas as pd
from pandas import DataFrame as df
import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import pickle

data = pd.read_csv('dummy-data.csv', header=0,low_memory=False)


def after():
    global data_2
    data_2=fpgrowth(data, min_support = 0.3, use_colnames = True)
    return render_template('home.html', data_3 = data_2)
