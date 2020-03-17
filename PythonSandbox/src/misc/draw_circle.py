'''
Draw a Circle
(https://leetcode.com/discuss/interview-question/513389/facebook-phone-screen-draw-a-circle)
Let us say that we already have an Api drawPoint(int x, int y), which can draw a point at position(x,y) on screen.
I would like you to implement drawCircle(int a, int b, int r) which should draw a circle whose center is (a,b) and radius is r
'''

import math
import numpy as np
import matplotlib.pyplot as plt
import time

class CircleDraw:
    def __init__(self):
        self.coords = []
        plt.ion()
        self.fig = plt.figure(figsize=(7,7))
        self.circleSubplotAx = self.fig.add_subplot(1,1,1)
        plt.grid()
    
    def drawCircle(self, a, b, r):
        self.coords.clear()
        self.circleSubplotAx.set_xlim(a-r-5, a+r+5)
        self.circleSubplotAx.set_ylim(b-r-5, b+r+5)
                 
        for deg in np.linspace(0, 360, 360):
            if plt.fignum_exists(1):
                rad = (math.pi/180) * deg
                x = a + r*math.cos(rad)
                y = b + r*math.sin(rad)
                self.drawPoint(x, y)
                plt.pause(.0001)
        
        plt.ioff()
        plt.show()
        
    def drawPoint(self, x, y):
        #print("DEBUG: plotting point: [{}, {}]".format(x,y))
        self.circleSubplotAx.scatter(x,y, s=2)
        plt.draw()
    
    def test_drawCircle(self):
        self.drawCircle(2, 5, 10)
    
    "Calc x,y from 0 to pi/2, all the while reflecting those points across y,origin,x-axes"
    def drawCircle2(self, a, b, r):
        self.coords.clear()
        self.circleSubplotAx.set_xlim(a-r-5, a+r+5)
        self.circleSubplotAx.set_ylim(b-r-5, b+r+5)
        
        for deg in np.linspace(0, 90, 90):
            if plt.fignum_exists(1):
                rad = (math.pi/180) * deg
                x = a + r*math.cos(rad)
                y = b + r*math.sin(rad)
                self.drawPoint(x, y) # quadrant 1
                self.drawPoint(-x+2*a, y) # quadrant 2
                self.drawPoint(-x+2*a, -y+2*b) # quadrant 3
                self.drawPoint(x, -y+2*b) # quadrant 4
                plt.pause(.00001)
                
        plt.ioff()
        plt.show()
    
    def test_drawCircle2(self):
        self.drawCircle2(5, 18, 12)
        
cd = CircleDraw()
#cd.test_drawCircle()
cd.test_drawCircle2()
