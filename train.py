# Purpose - This file is used to create a classifier and store it in a .pkl file. You can modify the contents of this
# file to create your own version of the classifier.

import numpy as np
from sklearn import metrics

from sklearn.ensemble import RandomForestClassifier

import joblib
from sklearn.metrics import accuracy_score, classification_report

labels = []
data_file = open('ml/dataset/PhishingDataset.arff').read()
data_list = data_file.splitlines()
data = np.array(data_list)
data1 = [i.split(',') for i in data]
data1 = data1[0:-1]
for i in data1:
    labels.append(i[26])
data1 = np.array(data1)
features = data1[:, :-1]
# Choose only the relevant features from the data set.
features = features[:,
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]]
features = np.array(features).astype(np.float64)

features_train = features
labels_train = labels
features_test = features[4000:]
labels_test = labels[4000:]

print("\n\n ""Random Forest Algorithm Results"" ")
clf4 = RandomForestClassifier(min_samples_split=7, verbose=True)
clf4.fit(features_train, labels_train)
importances = clf4.feature_importances_
std = np.std([tree.feature_importances_ for tree in clf4.estimators_], axis=0)
indices = np.argsort(importances)[::-1]
# Print the feature ranking
print("Feature ranking:")
for f in range(features_train.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

pred4 = clf4.predict(features_test)
print(classification_report(labels_test, pred4))
print('The accuracy is:', accuracy_score(labels_test, pred4))
print(metrics.confusion_matrix(labels_test, pred4))

# sys.setrecursionlimit(9999999)
joblib.dump(clf4, 'ml/classifier/random_forest.pkl', compress=3)
