"""
From sentdex youtube channel:
Machine learning for Stocks and Forex Technical Analysis
Link: https://www.youtube.com/watch?v=cExOVprMlQg

Files (GBPUSD1d.txt, GBPUSD1m.txt) from: http://sentdex.com/GBPUSD.zip
""" 

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import quandl
import math
import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

def graph_raw_fx():
    date, bid, ask = np.loadtxt("GBPUSD1d.txt", unpack=True, delimiter=",",
                                converters={0:mdates.bytespdate2num("%Y%m%d%H%M%S")});
    
    # define figure
    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid(shape=(40,40), loc=(0,0), rowspan=40, colspan=40)
    
    # plot data
    ax1.plot(date, bid)
    ax1.plot(date, ask)
    
    # format x-axis so that it is in date format.
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask-bid), facecolor="g", alpha=.3)
    
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    plt.subplots_adjust(bottom=.23) # add additional space below date ticks
       
    plt.grid(True)
    #plt.show()

# required columns
adj = {
    'open': 'Adj. Open',
    'close': 'Adj. Close',
    'hi': 'Adj. High',
    'low': 'Adj. Low',
    'vol': 'Adj. Volume'}

def find_pattern():
    df = quandl.get("WIKI/GOOGL")
    #print(df[0:10])
    
    field_list = [adj['open'], adj['hi'], adj['low'], adj['close'], adj['vol']]
    print("field_list: ", field_list)
    df = df[field_list]
    df['HL_PCT'] = (df[adj['hi']] - df[adj['close']]) / df[adj['close']] * 100.0
    df['PCT_change'] = (df[adj['close']] - df[adj['open']]) / df[adj['open']] * 100.0
    df = df[ [adj['close'], 'HL_PCT', 'PCT_change', adj['vol']] ]
    
    forecast_col = adj['close']
    df.fillna(-99999, inplace=True)
    
    forecast_out = int(math.ceil(0.01 * len(df)))
    print("forecast_out: ", forecast_out)
    
    df['label'] = df[forecast_col].shift(-forecast_out)
    print("find_pattern: df head:\n", df.head())
    
    # features: drop label column
    X = np.array(df.drop(['label'], 1))
    print("X: ", X)
    X = X[:-forecast_out]
    print("X after bracket: ", X)
    X_lately = X[-forecast_out:]
    print("X_lately: ", X_lately)
    # normalize the new values alongside all your other values. adds to processing time, unfortunately.
    X = preprocessing.scale(X)
    
    df.dropna(inplace=True)
    # labels
    y = np.array(df['label'])
    
    # cross validation
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2) # 20% of data is test data
    
    # run linear regression train and test
    clf = LinearRegression(n_jobs=-1)
    #clf = svm.SVR()
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    print("accuracy: ", accuracy)
    
    

def main():
    graph_raw_fx()
    find_pattern()
    #print(req_cols.AdjOpen)

if __name__ == "__main__":
    main()