import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
from networkx.generators.geometric import euclidean
from nltk.cluster.util import euclidean_distance
import pandas as pd
import random
from nltk.metrics import distance

style.use('fivethirtyeight')

#plot1 = [1,3]
#plot2 = [2,5]

#euclidean_distance = np.sqrt((plot1[0]-plot2[0])**2 + (plot1[1]-plot2[1])**2)
#print("euclidean_distance: ", euclidean_distance)

# dataset = {
#     'k' : [[1,2],[2,3],[3,1]],
#     'r' : [[6,5],[7,7],[8,6]]}
# 
# new_features = [5,7]
# 
# for i in dataset:
#     for ii in dataset[i]:
#         plt.scatter(ii[0], ii[1], s=100, color=i)
# plt.scatter(new_features[0], new_features[1])


def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K set to a value less than total voting groups!')

    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance, group])
    print("distances: ", distances)
    votes = [i[1] for i in sorted(distances)[:k]] # first k distances
    print("votes: ", votes)
    most_common_votes = Counter(votes).most_common(1)
    print("most_common_votes: ", most_common_votes)
    vote_result = most_common_votes[0][0]
    print("vote_result: ", vote_result)
    
    #knnalgos
    return vote_result
    
# result = k_nearest_neighbors(dataset, new_features)
# print("result: ", result)
# plt.show()

df = pd.read_csv("data/breast_cancer/breast-cancer-wisconsin.data.txt")
df.replace("?", -99999, inplace=True)
df.drop(['id'], 1, inplace=True)
full_data = df.astype(float).values.tolist()
print("full_data: ", full_data[:10])

random.shuffle(full_data)
print("full_data after shuffle: ", full_data[:10])

test_size= 0.2
train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
train_data = full_data[:-int(test_size * len(full_data))] #
test_data = full_data[-int(test_size * len(full_data)):] # last 20 percent of data

for i in train_data:
    train_set[i[-1]].append(i[:-1]) 
    
for i in test_data:
    test_set[i[-1]].append(i[:-1]) 
    
correct = 0
total = 0

for group in test_set:
    for data in test_set[group]:
        vote = k_nearest_neighbors(train_set, data, k=5)
        if group == vote:
            correct += 1
        total += 1
        
print("Accuracy: ", correct/total)