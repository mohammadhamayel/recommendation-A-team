def top10RatedMoviesQuery():
    return """
            SELECT m.MovieID As MovieID,m.Title As Title, COUNT(r.Rating) AS RatingCount, AVG(r.Rating) AS AvgRating , m.tmdbId As tmdbId
            FROM movies m
            JOIN ratings r ON m.MovieID = r.MovieID
            WHERE r.Rating > 4
            GROUP BY m.MovieID, m.Title,m.tmdbId
            ORDER BY RatingCount DESC
            LIMIT 10;
        """


def top10NewMoviesQuery():
    return """
            SELECT m.Title, COUNT(r.Rating) AS RatingCount, AVG(r.Rating) AS AvgRating, m.release_date,m.tmdbId
            FROM movies m
            JOIN ratings r ON m.MovieID = r.MovieID
            WHERE r.Rating > 3
            AND m.release_date >= '2019-01-01'
            GROUP BY m.MovieID, m.Title, m.release_date,m.tmdbId
            ORDER BY RatingCount DESC
            LIMIT 10;
        """


def top10PerGenreQuery():
    return """
            SELECT m.MovieID As MovieID,m.Title As Title, COUNT(r.Rating) AS RatingCount, AVG(r.Rating) AS AvgRating , m.tmdbId As tmdbId
            FROM movies m
            JOIN ratings r ON m.MovieID = r.MovieID
            WHERE r.Rating > 4
            and m.genres like :genre
            GROUP BY m.MovieID, m.Title,m.tmdbId
            ORDER BY RatingCount DESC
            LIMIT 10;
        """
