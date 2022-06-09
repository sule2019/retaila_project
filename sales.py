from email.policy import default
import pandas as pd
from pandas import DataFrame as df
import numpy as np

from model import *

sales_data = data.tail(10).copy(deep=True)

def totalSales():
    if sales_data.get(['total_sales']) is not None:
        return sales_data
    else:
        sales_data['total_sales'] = sales_data['Quantity'] * sales_data['Price']
        return data
    