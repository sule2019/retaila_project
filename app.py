
from flask import Flask, render_template, request, session, redirect

#import pickle
import numpy as np
import pandas as pd
from model import *
from data_exploration import *
from sales import *
from purchases import *

app = Flask(__name__)


#recent = None
#historical = None

@app.route("/",)
@app.route("/home", methods=['GET', 'POST'])
def home():
        
    if request.method == 'POST' and request.form.get('recent'):
        recent = request.form['recent']
        global recent_transactions
        recent_transactions = data.head(int(recent))
    else:
        recent_transactions = data.head(20)
    
    if request.method == 'POST' and request.form.get('historical'):
        historical = request.form['historical']
        global historical_transactions
        historical_transactions = data.tail(int(historical))
    else:   
        historical_transactions = data.tail(20)   
        
    return render_template('home.html', 
                           data_description=[data_description.to_html(classes='data', header='true')], 
                           data_sample=[data_sample.to_html(classes='data', header='true')], data_head=[data_head.to_html(classes='data', header='true')],data_tail=[data_tail.to_html(classes='data', header='true')],
                           recent_transactions = [recent_transactions.to_html(classes='data', header='true')],
                           historical_transactions = [historical_transactions.to_html(classes='data', header='true')]
                           
                           
                           )

@app.route('/sales')
def sales():
    
    
    
    return render_template('sales.html', sales_data = [ProcessSalesData().to_html(classes='data', header='true')], total_sales_all = total_sales_all, total_sales_each_transaction = [total_sales_each_transaction.to_html(classes='data', header='true')], total_sales_each_location = [total_sales_each_location.to_html(classes='data', header='true')], each_day_sales = [each_day_sales.to_html(classes='data', header='true')])
    
    
    
    
@app.route('/purchases')
def purchases():
    return render_template('purchases.html', purchases_data = [purchases_data.to_html(classes='data', header='true')])

    

if __name__ == "__main__":
    app.run(debug=True)
















