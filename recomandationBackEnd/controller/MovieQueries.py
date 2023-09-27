# Define SQL queries as static class variables
top10RatedMoviesQuery = """
        SELECT movieid, title, RatingCount, AvgRating, tmdbId
        FROM top_rated_movies
        WHERE AvgRating > 4
        ORDER BY RatingCount DESC
        LIMIT 10;
    """

top10NewMoviesQuery = """
        SELECT movieid, RatingCount, AvgRating, release_date, tmdbId
        FROM top_rated_movies
        WHERE AvgRating > 3
        AND release_date >= '2019-01-01'
        ORDER BY RatingCount DESC
        LIMIT 10;
    """

top10PerGenreQuery = """
        SELECT MovieID, Title, RatingCount, AvgRating, tmdbId
        FROM top_rated_movies
        WHERE AvgRating > 4
        AND genres LIKE :genre
        ORDER BY RatingCount DESC
        LIMIT 10;
    """

recommendedUserMoviesQuery = """
            SELECT tmdbId FROM movies WHERE movieId IN :movieIdList
        """

recommendedSimilarMoviesQuery = """
            SELECT tmdbId FROM movies WHERE movieId IN :movieIdList
        """


genreByMovieIdMoviesQuery = """
            SELECT genres FROM movies where movieId=:movieId
        """