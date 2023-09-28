import requests
from flask import jsonify

from recomandationBackEnd.loaders.logger_config import logger
from recomandationBackEnd.model.MovieExternalInfoModel import MovieExternalModel, Genre, ProductionCompany, \
    ProductionCountry, SpokenLanguage


def get_movie_info(tmdbId):
    # Define the URL and headers
    url = 'https://api.themoviedb.org/3/movie/' + str(tmdbId)
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NmM5MWIwOWVhNTQ0ZDM0Y2IzMmJhYjM3MDFjZjBiYiIsInN1YiI6IjY1MGU5MWFiZTFmYWVkMDEwMGU4MWVmNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xdHjKPspMbIHlzk1IMYE5DvPF2miEu6Xwv0TOawsXU4',
        'accept': 'application/json'
    }

    # Make the API call
    logger.info(f'Calling External Themoviedb API : {tmdbId}')
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        json_data = response.json()
        movie_info = MovieExternalModel(
            adult=json_data["adult"],
            backdrop_path=json_data["backdrop_path"],
            belongs_to_collection=json_data["belongs_to_collection"] if json_data.get(
                "belongs_to_collection") else None,
            budget=json_data["budget"],
            genres=[Genre(**genre_data) for genre_data in json_data["genres"]],
            homepage=json_data.get("homepage"),
            id=json_data["id"],
            imdb_id=json_data["imdb_id"],
            original_language=json_data["original_language"],
            original_title=json_data["original_title"],
            overview=json_data["overview"],
            popularity=json_data["popularity"],
            poster_path=json_data["poster_path"],
            production_companies=[ProductionCompany(**company_data) for company_data in
                                  json_data["production_companies"]],
            production_countries=[ProductionCountry(**country_data) for country_data in
                                  json_data["production_countries"]],
            release_date=json_data["release_date"],
            revenue=json_data["revenue"],
            runtime=json_data["runtime"],
            spoken_languages=[SpokenLanguage(**language_data) for language_data in json_data["spoken_languages"]],
            status=json_data["status"],
            tagline=json_data["tagline"],
            title=json_data["title"],
            video=json_data["video"],
            vote_average=json_data["vote_average"],
            vote_count=json_data["vote_count"]

        )
        logger.info(f'Response External {tmdbId} Themoviedb API : {movie_info}')
        return movie_info
    else:
        logger.info(f'Problem Response External {tmdbId} Themoviedb API')
        return jsonify({'error': 'Failed to fetch movie information'}), response.status_code
