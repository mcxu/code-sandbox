'''
Min Rewards

Given list of unique scores, give list of reward points according to two rules:
1. all students must receive at least one reward
2. any given student must receive more rewards than an adjacent student 
with a lower score and must receive strictly fewer rewards than an adjacent 
student with a higher score. 

Sample input:      [8, 4, 2, 1, 3, 6, 7, 9, 5]
Sample output: 25 ([4, 3, 2, 1, 2, 3, 4, 5, 1])
'''
import time

class Prob:
    @staticmethod
    def minRewards(scores):
        rewards = [1] * len(scores)
        
        i = 1
        decn = 0
        while i < len(scores):
            print("i===", i)
            
            if scores [i-1] < scores[i]:
                # for increase
                if decn > 0:
                    print("    decn is currently: ", decn)
                    for j in range(i-2, i-decn-2, -1):
                        if rewards[j] < rewards[j+1]+1:
                            rewards[j] = rewards[j+1]+1
                            
                        print("    rewards[j={}]= {}".format(j,rewards[j]))
                    decn = 0
                 
                rewards[i] += rewards[i-1]
                 
            else:
                # for decrease
                # count number of decreasing values
                decn += 1
                print("decn: ", decn)
        
            i+=1
            
        if decn > 0 and rewards[-1]==1 and rewards[-2]==1:
            print("B i=", i)
            for j in range(i-2, i-decn-2, -1):
                print("B j=", j)
                rewards[j] = rewards[j+1] + 1
        print("final rewards:", rewards)        
        return sum(rewards)
    
    @staticmethod
    def test1():
        #scores = [8, 4, 2, 1, 3, 6, 7, 9, 5] #25
        #scores = [8, 4, 2, 1, 3, 6, 7, 9, 10] #30
        #scores = [1]
        #scores = [5,10]
        #scores = [10,5]
        #scores = [10,9,8,7]
        #scores = [5,10,11]
        #scores = [5,10,9]
        #scores = [5,10,15,20,17,18,19]
        #scores = [0, 4, 2, 1, 3] # 9
        scores = [800, 400, 20, 10, 30, 61, 70, 90, 17, 21]
        #scores = [800, 400, 20, 10, 30, 61, 70, 90, 17, 21, 22, 13, 12, 11, 8, 4, 2, 1, 3, 6, 7, 9, 0, 68, 55, 67, 57, 60, 51, 661, 50, 65, 53] #93
        #scores = [i for i in range(10,-1,-1)]
        rewardSum = Prob.minRewards(scores)
        print("test1: rewardSum: ", rewardSum)
    
    @staticmethod
    def minRewards2(scores):
        rewards = [1] * len(scores)
        for i in range(1, len(scores)):
            if scores[i-1] < scores[i]:
                rewards[i] += rewards[i-1]
        print("rewards A: ", rewards)
        for i in range(len(scores)-2, -1, -1):
            if scores[i] > scores[i+1] and rewards[i+1]+1 > rewards[i]:
                rewards[i] = rewards[i+1]+1
        print("rewards B: ", rewards)
        rewardSum = sum(rewards)
        print("rewardSum: ", rewardSum)
        return rewardSum
    
    @staticmethod
    def test2():
        scores = [8, 4, 2, 1, 3, 6, 7, 9, 5] #25
        #scores = [8, 4, 2, 1, 3, 6, 7, 9, 10] #30
        #scores = [1]
        #scores = [5,10]
        #scores = [10,5]
        #scores = [10,9,8,7]
        #scores = [5,10,11]
        #scores = [5,10,9]
        #scores = [5,10,15,20,17,18,19]
        #scores = [0, 4, 2, 1, 3] # 9
        #scores = [800, 400, 20, 10, 30, 61, 70, 90, 17, 21]
        #scores = [800, 400, 20, 10, 30, 61, 70, 90, 17, 21, 22, 13, 12, 11, 8, 4, 2, 1, 3, 6, 7, 9, 0, 68, 55, 67, 57, 60, 51, 661, 50, 65, 53] #93
        #scores = [i for i in range(10,-1,-1)]
        Prob.minRewards2(scores)
        
#Prob.test1()
Prob.test2()
