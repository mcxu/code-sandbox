"""
Machine Learning Andrew Ng - Programming Exercise 1
"""

import pandas as pd
import os.path as path
import matplotlib.pyplot as plt

class Ex1:
    @staticmethod
    def readCSVData(filePath, pickleFile, colNames=[]):
        df = pd.read_csv(filePath, names=colNames)
        print(df.info())
        print(df.head())
        df.to_pickle(pickleFile)
    
    # read pickle file by default
    @staticmethod
    def readEx1Data():
        ex1data1DF = None
        ex1Pickle = "../data/ex1data1.pkl"
        if path.exists(ex1Pickle):
            ex1data1DF = pd.read_pickle(ex1Pickle)
        else:
            ex1data1DF = Ex1.readCSVData("../data/ex1data1.txt", ex1Pickle,
                                           colNames=["CityPopulation","FoodTruckProfit"])
        return ex1data1DF
    
    
    # 2.1 Plotting the Data
    @staticmethod
    def plotEx1Data1():
        ex1data1DF = Ex1.readEx1Data()
        print(ex1data1DF.info())
        print(ex1data1DF.head())
        
        X = ex1data1DF["CityPopulation"]
        y = ex1data1DF["FoodTruckProfit"]
        plt.scatter(X,y, marker=".", color="red")
        plt.xlabel("CityPopulation")
        plt.ylabel("FoodTruckProfit")
    
    @staticmethod
    def linReg(X, y):
        pass
        

    @staticmethod
    def test_linReg(self):
        pass

def main():
    Ex1.plotEx1Data1()
    plt.show()
    
main()
