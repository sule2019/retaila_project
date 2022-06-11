from email.policy import default
import pandas as pd
from pandas import DataFrame as df
import numpy as np

from model import *

sales_data = data.tail(10).copy(deep=True)

def ProcessSalesData():
    #convert data
    sales_data["Date"] = pd.to_datetime(sales_data.Date)
    sales_data["new_date"] = sales_data["Date"].dt.date
    sales_data["new_time"] = sales_data["Date"].dt.time
    
    #Calculate total sales
    if sales_data.get(['total_sales']) is not None:
        return sales_data
    else:
        sales_data['total_sales'] = sales_data['Quantity'] * sales_data['Price']
        return sales_data
    
#Total sales for all transactions
    
total_sales_all = sum(ProcessSalesData()['total_sales'])

#Total sales for each transaction
total_sales_each_transaction = ProcessSalesData().groupby(["BillNo"]).total_sales.sum().reset_index()

#Average sales for all transactions
average_transaction_sales = total_sales_each_transaction['total_sales'].mean()

#Total sales for each location
total_sales_each_location = ProcessSalesData().groupby(["Country"]).total_sales.sum().reset_index().round(2)

#Total sales for certain periods of time



#Total sales for each day
each_day_sales = ProcessSalesData().groupby(["new_date"]).total_sales.sum().reset_index().round(2)

#Total sales for each hour
ProcessSalesData()['hour'] = pd.DatetimeIndex(ProcessSalesData()['Date']).hour
each_hour_sales = ProcessSalesData().groupby(["hour"]).total_sales.sum().reset_index().round(2)




