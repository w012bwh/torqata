from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination, get_page_args


app = Flask(__name__,template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:EIhk4vxIwBd3gdPo@34.135.240.167:5432/netflix_data"
db = SQLAlchemy(app)

class NetflixTitles(db.Model):

    show_id = db.Column(db.String(), primary_key=True)
    type = db.Column(db.String())
    title = db.Column(db.String())
    director = db.Column(db.String())
    cast = db.Column(db.String())
    country = db.Column(db.String())
    date_added = db.Column(db.String())
    release_year = db.Column(db.String())
    rating = db.Column(db.String())
    duration = db.Column(db.String())
    listed_in = db.Column(db.String())
    description = db.Column(db.String())

    def __init__(self, show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description):
        self.show_id = show_id
        self.type = type
        self.title = title
        self.director = director
        self.cast = cast
        self.country = country
        self.date_added = date_added
        self.release_year = release_year
        self.rating = rating
        self.duration = duration
        self.listed_in = listed_in
        self.description = description

    def __repr__(self):
        return f"<Netflix Title {self.title}>"


@app.route('/', methods=['GET'])
def handle_titles():
    if request.method == 'GET':
        Titles = NetflixTitles.query.all()
        results = [
            {
                "show_id": title.show_id,
                "title": title.title,
                "type": title.type,
                "director": title.director,
                "cast": title.cast,
                "country": title.country,
                "date_added": title.date_added,
                "release_year": title.release_year,
                "rating": title.rating,
                "duration": title.duration,
                "listed_in": title.listed_in,
                "description": title.description,

            } for title in Titles]

    return {"Number of titles: ": len(results), "Titles: ": results}


@app.route('/pagination', methods=['GET'])
def handle_titles_paginated():
    ROWS_PER_PAGE = 25

    if request.method == 'GET':

        page = request.args.get('page', 1, type=int)

        results = NetflixTitles.query.paginate(page=page, per_page=ROWS_PER_PAGE)
        paginated_results = (results.items)

        results = [
            {
                "show_id": title.show_id,
                "title": title.title,
                "type": title.type,
                "director": title.director,
                "cast": title.cast,
                "country": title.country,
                "date_added": title.date_added,
                "release_year": title.release_year,
                "rating": title.rating,
                "duration": title.duration,
                "listed_in": title.listed_in,
                "description": title.description,

            } for title in paginated_results]



    return {"Number of titles: ": len(paginated_results), "Titles: ": results}


@app.route('/stats/release_year/', methods=['GET'])
def release_year_stats():
    if request.method == 'GET':
        years = NetflixTitles.query.with_entities(NetflixTitles.release_year).all()

        release_year_count = {}


        for year in years:

            if year[0] not in release_year_count:
                release_year_count[year[0]] = 1

            else:
                oldCount =  release_year_count[year[0]]
                release_year_count[year[0]] = oldCount + 1

    return release_year_count

@app.route('/stats/country/', methods=['GET'])
def country_stats():
    if request.method == 'GET':
        group_countrys = NetflixTitles.query.with_entities(NetflixTitles.country).all()

        # group_countrys = ",".join(group_countrys)

        country_count = {}

        country_null_count = 0

        for countrys in group_countrys:
            countrys = countrys[0].split(',')

            for country in countrys:
                if country not in country_count:
                    country_count[country] = 1

                else:
                    oldCount =  country_count[country]
                    country_count[country] = oldCount + 1

    return country_count

@app.route('/stats/director/', methods=['GET'])
def director_stats():
    if request.method == 'GET':
        director_list = NetflixTitles.query.with_entities(NetflixTitles.director).all()

        director_count = {}


        for directors in director_list:
            directors = directors[0].split(',')

            for director in directors:

                if director not in director_count:
                    director_count[director] = 1

                else:
                    oldCount =  director_count[director]
                    director_count[director] = oldCount + 1

    return director_count



@app.route('/stats/type/', methods=['GET'])
def type_stats():
    if request.method == 'GET':
        types = NetflixTitles.query.with_entities(NetflixTitles.type).all()
        type_count = {}

        for type in types:
            if type[0] not in type_count:
                type_count[type[0]] = 1

            else:
                oldCount =  type_count[type[0]]
                type_count[type[0]] = oldCount + 1

    return type_count


@app.route('/stats/rating/', methods=['GET'])
def rating_stats():
    if request.method == 'GET':
        ratings = NetflixTitles.query.with_entities(NetflixTitles.rating).all()
        ratings_count = {}

        for rating in ratings:
            if rating[0] not in ratings_count:
                ratings_count[rating[0]] = 1

            else:
                oldCount =  ratings_count[rating[0]]
                ratings_count[rating[0]] = oldCount + 1

    return ratings_count

@app.route('/filter/type/movie', methods=['GET'])
def filter_by_movie():
    if request.method == 'GET':
        Titles = NetflixTitles.query.filter(NetflixTitles.type.ilike("movie"))
        results = [
            {
                "show_id": title.show_id,
                "title": title.title,
                "type": title.type,
                "director": title.director,
                "cast": title.cast,
                "country": title.country,
                "date_added": title.date_added,
                "release_year": title.release_year,
                "rating": title.rating,
                "duration": title.duration,
                "listed_in": title.listed_in,
                "description": title.description,

            } for title in Titles]

    return {"Number of titles of movies: ": len(results), "Titles: ": results}

@app.route('/filter/type/tvshow', methods=['GET'])
def filter_by_tvshow():
    if request.method == 'GET':
        Titles = NetflixTitles.query.filter(NetflixTitles.type.ilike("tv show"))
        results = [
            {
                "show_id": title.show_id,
                "title": title.title,
                "type": title.type,
                "director": title.director,
                "cast": title.cast,
                "country": title.country,
                "date_added": title.date_added,
                "release_year": title.release_year,
                "rating": title.rating,
                "duration": title.duration,
                "listed_in": title.listed_in,
                "description": title.description,

            } for title in Titles]

    return {"Number of titles of movies: ": len(results), "Titles: ": results}



if __name__ == '__main__':
    app.run()
