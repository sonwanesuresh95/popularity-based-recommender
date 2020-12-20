import pandas as pd
import numpy as np


class Lens:
    def __init__(self):
        self.dataset = self.build_dataset()

    def build_dataset(self):
        u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
        users = pd.read_csv('dataset/ml-100k/u.user', sep='|', names=u_cols, encoding='latin-1')
        r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
        ratings = pd.read_csv('dataset/ml-100k/u.data', sep='\t', names=r_cols, encoding='latin-1')
        m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
        movies = pd.read_csv('dataset/ml-100k/u.item', sep='|', names=m_cols, usecols=range(5), encoding='latin-1')
        movie_ratings = pd.merge(movies, ratings)
        lens = pd.merge(movie_ratings, users)
        return lens

    def recommend_most_popular(self):
        return list(self.dataset['title'].value_counts().to_dict().keys())[:20]

    def highly_rated(self):
        movie_stats = self.dataset.groupby('title').agg({'rating': [np.size, np.mean]})
        high_rated = movie_stats.sort_values([('rating', 'mean'), ('rating', 'size')], ascending=False)
        return list(high_rated[high_rated['rating']['size'] >= 100]['rating']['mean'].to_dict().keys())[:20]
