"""
Estimate Pi
"""

import random
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import time
import queue

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
    def runErrorSimulation(sampleSize=10000):
        nSquare = 0
        nQCircle = 0
        
        nVals = queue.Queue(maxsize=sampleSize)
        piEsts = queue.Queue(maxsize=sampleSize)
        errorRates = queue.Queue(maxsize=sampleSize)
        piEstFinal = 0
        errorRateFinal = 0
        
        # create plots
        fig = plt.figure()
        fig.suptitle('Pi Estimation Simulation')
        
        estPiSubplotAx = fig.add_subplot(2, 1, 1) # returns Axes object: https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes
        estPiSubplotAx.set_xlabel("sample size (n)")
        estPiSubplotAx.set_ylabel('Estimated Value of Pi')
        estPiSubplotAx.axhline(y=math.pi, color="red")
        estPiSubplotAx.plot(list(nVals.queue), list(piEsts.queue), '-', linewidth=1)
        plt.grid()
        
        errorRateSubplotAx = fig.add_subplot(2, 1, 2)
        errorRateSubplotAx.set_xlabel('sample size (n)')
        errorRateSubplotAx.set_ylabel('Error Rate')
        errorRateSubplotAx.axhline(y=0, color="red")
        errorRateSubplotAx.plot(list(nVals.queue), list(errorRates.queue), '-', linewidth=1)
        plt.grid()
        
        # run simulation
        def generateSamples(threadName):
            print("generateSamples thread started. threadName: ", threadName)
            nonlocal nSquare, nQCircle, piEstFinal, errorRateFinal
            for i in range(1, sampleSize+1):
                x = random.uniform(0,1)
                y = random.uniform(0,1)
                rp = math.sqrt(x**2 + y**2)
                #print("x: {}, y: {}".format(x, y))
                nSquare += 1
                if rp <= 1:
                    nQCircle += 1
                #print("nSquare: {}, nQCircle: {}".format(nSquare, nQCircle))
                piEst = 4 * nQCircle/nSquare 
                #print("nSquare: {}, nQCircle: {}, piEst: {}".format(nSquare, nQCircle, piEst))
                errorRate = abs(piEst - math.pi)/math.pi
                
                nVals.put(i, block=False)
                piEsts.put(piEst)
                errorRates.put(errorRate)
                print("i={}, piEst={}, errorRate={}".format(i, piEst, errorRate))
                time.sleep(.001)
            
            piEstFinal = list(piEsts.queue)[-1]
            errorRateFinal = list(errorRates.queue)[-1]
                    
        
        def animate(n):
            nonlocal nVals, piEsts, errorRates
            #print("estPiSubplotAx.lines: {}, errorRateSubplotAx.lines: {}".format(len(estPiSubplotAx.lines), len(errorRateSubplotAx.lines)))
            print("animate n={}".format(n))
            nScaled = n*10
            if nVals and n % 2 == 0:
                if len(estPiSubplotAx.lines) > 1:
                    estPiSubplotAx.lines[1].remove()
                estPiSubplotAx.plot(list(nVals.queue)[0:nScaled], list(piEsts.queue)[0:nScaled], '-', linewidth=1, color="blue")
                 
                if len(errorRateSubplotAx.lines) > 1:
                    errorRateSubplotAx.lines[1].remove()
                errorRateSubplotAx.plot(list(nVals.queue)[0:nScaled], list(errorRates.queue)[0:nScaled], '-', linewidth=1, color="blue")
            
                plt.draw()
                
            if nScaled >= sampleSize and nVals.qsize() >= sampleSize:
                print("stopping animation")
                ani.event_source.stop()
                
                # print pi for largest sample size
                print("pi estimate for {} samples: {}".format(sampleSize, piEstFinal))
                print("error rate: ", errorRateFinal)
                

        intvl = 1 # milliseconds
        ani = animation.FuncAnimation(fig, animate, interval=intvl, repeat=False, frames=None)
        genSampleThread = threading.Thread(target=generateSamples, args=(1,))    
        genSampleThread.start()
        plt.show()

#EstPi.test_estimatePi()
EstPi.runErrorSimulation()