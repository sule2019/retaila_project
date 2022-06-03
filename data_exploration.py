from model import *


data_description = data.describe()
data_sample = data.sample()
data_head = data.head()
data_tail = data.tail()




# Data selection
number_for_recent = 15
number_for_historical = 15
#recent_transactions = data.head(number_for_recent)
historical_transactions = data.tail(number_for_historical)


