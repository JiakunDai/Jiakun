import numpy as np

def knn(k, in_data, out_data):
    in_data = np.array(X = np.array([[2.1, 1.3], [1.3, 3.2], [2.9, 2.5], [2.7, 5.4], [3.8, 0.9], 
        [7.3, 2.1], [4.2, 6.5], [3.8, 3.7], [2.5, 4.1], [3.4, 1.9],
        [5.7, 3.5], [6.1, 4.3], [5.1, 2.2], [6.2, 1.1]]))
    out_data = np.array([[5.1 ,2.2],[3.8, 3.7],[3.4, 1.9],[2.9 ,2.5],[5.7, 3.5]])
    dist = np.sqrt(np.sum((in_data - out_data)**2, axis=1))
    sorted_indices = np.argsort(dist)
    k_nearest_indices = sorted_indices[:k]
    k_nearest_labels = [in_data[i] for i in k_nearest_indices]
    return k_nearest_labels

