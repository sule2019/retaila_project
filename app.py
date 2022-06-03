
from flask import Flask, render_template, request, session, redirect

#import pickle
import numpy as np
import pandas as pd
from model import *
from data_exploration import *

app = Flask(__name__)

recent = None
historical = None

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST':
        #Recent Transactions
        recent = request.form['recent']
        global recent_transactions
        recent_transactions = data.head(int(recent))
        
        #Historical Transactions
        historical = request.form['historical']
        global historical_transactions
        historical_transactions = data.tail(int(historical))
        
    else:
        recent_transactions = data.head(13)
        historical_transactions = data.tail(13)
        
 
        
    
    
    
    return render_template('home.html', 
                           data_description=[data_description.to_html(classes='data', header='true')], 
                           data_sample=[data_sample.to_html(classes='data', header='true')], data_head=[data_head.to_html(classes='data', header='true')],data_tail=[data_tail.to_html(classes='data', header='true')],
                           recent_transactions = [recent_transactions.to_html(classes='data', header='true')],
                           historical_transactions = [historical_transactions.to_html(classes='data', header='true')]
                           
                           
                           )


if __name__ == "__main__":
    app.run(debug=True)
















