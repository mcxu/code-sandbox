"""
Estimate Pi
"""

import random
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class EstPi:
    
    """
    n: number of random samples within a 1x1 cell.
    (with quarter circle tracing the 1 coordinate for x and y)
    """
    @staticmethod
    def estimatePi(n):
        
        nQCircle = 0 # num points in quarter circle
        nSquare = 0 # num points in square
        
        for i in range(n):
            x = random.uniform(0,1)
            y = random.uniform(0,1)
            rp = math.sqrt(x**2 + y**2)
            
            nSquare += 1
            if rp <= 1:
                nQCircle += 1
        
        pi = 4 * nQCircle/nSquare
        return pi
    
    @staticmethod
    def test_estimatePi():
        n = 1000000
        piEst = EstPi.estimatePi(n)
        print("piEst = ", piEst)
    
    """
    Generate plots of pi estimation and error rate
    for [1,sampleSize] inclusive. 
    """
    @staticmethod
    def runErrorSimulation(sampleSize=2000):
        nSquare = 0
        nQCircle = 0
        
        nVals = []
        piEsts = []
        errorRates = []
        piEstFinal = 0
        errorRateFinal = 0
        
        # create plots
        fig = plt.figure()
        fig.suptitle('Pi Estimation Simulation')
        
        estPiSubplotAx = fig.add_subplot(2, 1, 1) # returns Axes object: https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes
        estPiSubplotAx.set_xlabel("sample size (n)")
        estPiSubplotAx.set_ylabel('Estimated Value of Pi')
        estPiSubplotAx.axhline(y=math.pi, color="red")
        estPiSubplotAx.plot(nVals, piEsts, '-', linewidth=1)
        plt.grid()
        
        errorRateSubplotAx = fig.add_subplot(2, 1, 2)
        errorRateSubplotAx.set_xlabel('sample size (n)')
        errorRateSubplotAx.set_ylabel('Error Rate')
        errorRateSubplotAx.axhline(y=0, color="red")
        errorRateSubplotAx.plot(nVals, errorRates, '-', linewidth=1)
        plt.grid()
        
        def animate(n):
            nonlocal nSquare, nQCircle, piEstFinal, errorRateFinal
            #print("estPiSubplotAx.lines: {}, errorRateSubplotAx.lines: {}".format(len(estPiSubplotAx.lines), len(errorRateSubplotAx.lines)))
            if n > 0:
                # run simulation
                x = random.uniform(0,1)
                y = random.uniform(0,1)
                rp = math.sqrt(x**2 + y**2)
                
                nSquare += 1
                if rp <= 1:
                    nQCircle += 1
                piEst = 4 * nQCircle/nSquare 
                #print("nSquare: {}, nQCircle: {}, piEst: {}".format(nSquare, nQCircle, piEst))
                errorRate = abs(piEst - math.pi)/math.pi
                
                if n % 10 == 0:
                    nVals.append(n)
                    piEsts.append(piEst)
                    errorRates.append(errorRate)
                    
                    if len(estPiSubplotAx.lines) > 1:
                        estPiSubplotAx.lines[1].remove()
                    estPiSubplotAx.plot(nVals, piEsts, '-', linewidth=1, color="blue")
                    
                    if len(errorRateSubplotAx.lines) > 1:
                        errorRateSubplotAx.lines[1].remove()
                    errorRateSubplotAx.plot(nVals, errorRates, '-', linewidth=1, color="blue")
                    
                    plt.draw()
                
                if n >= sampleSize:
                    piEstFinal = piEst
                    errorRateFinal = errorRate
             
        ani = animation.FuncAnimation(fig, animate, interval=1, repeat=False, frames=sampleSize+1)
        plt.show()
        
        # print pi for largest sample size
        print("pi estimate for {} samples: {}".format(sampleSize, piEstFinal))
        print("error rate: ", errorRateFinal)
        
        

#EstPi.test_estimatePi()
EstPi.runErrorSimulation()