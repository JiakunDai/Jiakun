import json
import argparse
from math import sqrt

def pearson_score(dataset, user1, user2):
    common_movies = {}
    for movie in dataset[user1]:
        if movie in dataset[user2]:
            common_movies[movie] = 1
    n_common_movies = len(common_movies)
    if n_common_movies == 0:
        return 0
    sum1 = sum([dataset[user1][movie] for movie in common_movies])
    sum2 = sum([dataset[user2][movie] for movie in common_movies])
    sum1_sq = sum([pow(dataset[user1][movie], 2) for movie in common_movies])
    sum2_sq = sum([pow(dataset[user2][movie], 2) for movie in common_movies])
    product_sum = sum([dataset[user1][movie] * dataset[user2][movie] for movie in common_movies])
    num = product_sum - (sum1 * sum2 / n_common_movies)
    den = sqrt((sum1_sq - pow(sum1, 2) / n_common_movies) * (sum2_sq - pow(sum2, 2) / n_common_movies))
    if den == 0:
        return 0
    return num/den

def main():
    args = parse_arguments()
    input_user = args.user
    data = load_data()
    if input_user not in data:
        print(f'User {input_user} not found in dataset')
        return
    recommendations = get_recommendations(data, input_user)
    print(f'Recommended movies for {input_user}:')
    for movie in recommendations:
        print(movie)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Movie Recommender System')
    parser.add_argument('--user', type=str, help='User for whom to generate movie recommendations')
    return parser.parse_args()

def get_recommendations(dataset, input_user):
    overall_scores = {}
    similarity_scores = {}
    for user in dataset:
        if user == input_user:
            continue
        sim_score = pearson_score(dataset, input_user, user)
        if sim_score <= 0:
            continue
        for movie in dataset[user]:
            if movie not in dataset[input_user] or dataset[input_user][movie] == 0:
                overall_scores.setdefault(movie, 0)
                overall_scores[movie] += dataset[user][movie] * sim_score
                similarity_scores.setdefault(movie, 0)
                similarity_scores[movie] += sim_score
    if len(overall_scores) == 0:
        return ['No recommendations possible']
    movie_scores = [(score/similarity_scores[movie], movie) for movie, score in overall_scores.items()]
    movie_scores.sort(reverse=True)
    return [movie for _, movie in movie_scores]

def load_data():
    with open('ratings.json', 'r') as f:
        return json.loads(f.read())


if __name__ == '__main__':
    main()
