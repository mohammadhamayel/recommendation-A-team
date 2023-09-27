def prepare_knn(data):
    movie_to_user_df = data.pivot(index='movieId', columns='userId', values='rating').fillna(0)

    movies_list = list(movie_to_user_df.index)

    movie_dict = {movie: index for index, movie in enumerate(movies_list)}

    return movie_to_user_df, movies_list, movie_dict
