import numpy as np
import scipy.io as sio
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler
from DBADV import DBADV
from itertools import cycle, islice
import matplotlib.pyplot as plt

# Shape5: 5 classes;3150 samples;2 dimensionality
data = sio.loadmat('synthetic_datasets/Shape5.mat')
X = data['X']
Y = data['Y'].reshape(-1, )

# Standarize features
X = MinMaxScaler().fit_transform(X)

y_pred = DBADV(X, perplexity=16, MinPts=20, probability=0.977)
NMI = metrics.normalized_mutual_info_score(Y, y_pred, average_method='arithmetic')
print("NMI of Shape5 data set:", round(NMI, 2))

# plot
colors = np.array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
                                     '#f781bf', '#a65628', '#984ea3',
                                     '#999999', '#e41a1c', '#dede00']),
                              int(max(y_pred) + 1))))

colors = np.append(colors, ["#000000"])
plt.scatter(X[:, 0], X[:, 1], color=colors[y_pred], s=12, marker='.')
plt.xticks([])
plt.yticks([])
plt.show()
