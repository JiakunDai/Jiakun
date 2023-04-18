from math import sqrt
from scipy.stats import pearsonr

david = {
    "Vertigo": 4,
    "Scarface": 4.5,
    "Raging Bull": 3.0,
    "Goodfellas": 4.5,
    "The Apartment": 1.0
}

bill = {
    "Vertigo": 4.5,
    "Scarface": 5.0,
    "Goodfellas": 4.5,
    "The Apartment": 1.0
}

# Euclidean Distance
euclidean_dist = sqrt(sum([(david[movie] - bill[movie])**2 for movie in david if movie in bill]))
print("Euclidean Distance:", euclidean_dist)

# Pearson Correlation Coefficient
david_scores = [david[movie] for movie in david if movie in bill]
bill_scores = [bill[movie] for movie in bill if movie in david]
pearson_corr, _ = pearsonr(david_scores, bill_scores)
print("Pearson Correlation Coefficient:", pearson_corr)

# Manhattan Distance
manhattan_dist = sum([abs(david[movie] - bill[movie]) for movie in david if movie in bill])
print("Manhattan Distance:", manhattan_dist)
