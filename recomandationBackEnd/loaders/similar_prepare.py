def prepare_knn(data):
    movie_to_user_df = data.pivot(index='title', columns='userId', values='rating').fillna(0)

    movies_list = list(movie_to_user_df.index)

    movie_dict = {movie: index for index, movie in enumerate(movies_list)}

    movie_title_id_dict = {title: movie_id for title, movie_id in zip(data['title'], data['movieId'])}

    return movie_to_user_df, movies_list, movie_dict,movie_title_id_dict
