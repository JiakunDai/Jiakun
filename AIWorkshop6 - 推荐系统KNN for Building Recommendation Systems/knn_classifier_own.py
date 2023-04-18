from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import time
def knn_classifier(train_data, test_data, k):
    train_data = np.array(train_data)
    test_data = np.array(test_data)
    predictions = []
    for x_test in test_data:
        distances = []
        for x_train in train_data:
            distance = np.sqrt(np.sum((x_test[:-1] - x_train[:-1]) ** 2))
            distances.append(distance)
        distances = np.array(distances)
        nearest_neighbors = np.argsort(distances)[:k]
        nearest_labels = [train_data[i][-1] for i in nearest_neighbors]
        prediction = max(set(nearest_labels), key=nearest_labels.count)
        predictions.append(prediction)
    return predictions


with open('data.txt') as f:
    data = f.readlines()
data = [np.array(list(map(float, line.strip().split(',')))) for line in data]

train_data = data[:5]
test_data = data[5:]


k = 3
predictions = knn_classifier(train_data, test_data, k)

from sklearn.neighbors import KNeighborsClassifier
X_train = np.array([x[:-1] for x in train_data])
y_train = np.array([x[-1] for x in train_data])
X_test = np.array([x[:-1] for x in test_data])
clf = KNeighborsClassifier(n_neighbors=k)
clf.fit(X_train, y_train)
sk_predictions = clf.predict(X_test)


start_time = time.time()
knn_classifier(train_data, test_data, k)
print("My implementation time:", time.time() - start_time)
start_time = time.time()
clf.predict(X_test)
print("sklearn implementation time:", time.time() - start_time)
