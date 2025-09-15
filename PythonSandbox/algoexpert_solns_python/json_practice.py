'''
Created on Aug 30, 2015

@author: Michael
'''

import json

class TransactionsParser(object):

    def __init__(self):
        self.json = json
    
    def parseJson(self):   
        # Read in the json file as a string
        path = "../../../JavaSandbox/data/transactions.json"
        jsonOpener = open(path, "r")
        jsonText = jsonOpener.read()
        jsonOpener.close()
        print(jsonText) 
        
        # convert json string into json object
        jsonObj = self.json.loads(jsonText)
        print("loaded json", jsonObj)
        
        # getting the transactions list
        transactionsList = jsonObj.get("transactions")
        print("transactionsList", transactionsList)
        
        # calculating the amounts
        transListLength = len(transactionsList)
        calculatedAmt = 0
        for i in range(transListLength):
            print("----------- for loop ------------")
            transType = transactionsList[i].get("type")
            print("transType", transType)
            transAmt = transactionsList[i].get("amount")
            print("transAmt", transAmt)
            
            if(transType == "CREDIT"):
                calculatedAmt = calculatedAmt - float(transAmt)
            elif(transType == "DEBIT"):
                calculatedAmt = calculatedAmt + float(transAmt)
        
        print("calculatedAmt", calculatedAmt)
        
def main():
    tp = TransactionsParser()
    tp.parseJson()
    
if __name__ == "__main__":
    main()