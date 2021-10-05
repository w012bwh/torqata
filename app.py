from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:EIhk4vxIwBd3gdPo@34.135.240.167:5432/netflix_data"
db = SQLAlchemy(app)

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Netflix application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)



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
        titles = NetflixTitles.query.all()
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

            } for title in titles]

    return {"Number of titles: ": len(results),
            "Titles: ": results}


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



    return {"Number of titles: ": len(paginated_results),
            "Titles: ": results}

#?type=movie
#?type=tv show
@app.route('/filter/type', methods=['GET'])
def filter_type():
    input_type = request.args.get('type')
    if request.method == 'GET':
        titles = NetflixTitles.query.filter(NetflixTitles.type.ilike(input_type))
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

            } for title in titles]

    return {"Number of titles of movies: ": len(results),
            "Titles: ": results}

#?id=8808&title=test&type=test&director=test&cast=test&country=test&date_added=test&release_year=test&rating=test&duration=test&listed_in=test&description=test
@app.route('/add', methods=['POST'])
def add_record():
    input_show_id = request.args.get('id')
    input_title = request.args.get('title')
    input_type = request.args.get('type')
    input_director = request.args.get('director')
    input_cast = request.args.get('cast')
    input_country = request.args.get('country')
    input_date_added = request.args.get('date_added')
    input_release_year = request.args.get('release_year')
    input_rating = request.args.get('rating')
    input_duration = request.args.get('duration')
    input_listed_in = request.args.get('listed_in')
    input_description = request.args.get('description')

    if request.method == 'POST':
        new_record=NetflixTitles(show_id=input_show_id,
                                 title=input_title,
                                 type=input_type,
                                 director=input_director,
                                 cast=input_cast,
                                 country=input_country,
                                 date_added=input_date_added,
                                 release_year=input_release_year,
                                 rating=input_rating,
                                 duration=input_duration,
                                 listed_in=input_listed_in,
                                 description=input_description)

        db.session.add(new_record)
        db.session.commit()

    return "Successfully added to database"



#?id=s1&title=test&type=test&director=test&cast=test&country=test&date_added=test&release_year=test&rating=test&duration=test&listed_in=test&description=test
@app.route('/update', methods=['PUT'])
def update_record():
    input_show_id = request.args.get('id')
    input_title = request.args.get('title')
    input_type = request.args.get('type')
    input_director = request.args.get('director')
    input_cast = request.args.get('cast')
    input_country = request.args.get('country')
    input_date_added = request.args.get('date_added')
    input_release_year = request.args.get('release_year')
    input_rating = request.args.get('rating')
    input_duration = request.args.get('duration')
    input_listed_in = request.args.get('listed_in')
    input_description = request.args.get('description')

    if request.method == 'PUT':

        get_title = NetflixTitles.query.get(input_show_id)

        get_title.title = input_title
        get_title.type = input_type
        get_title.director = input_director
        get_title.cast = input_cast
        get_title.country = input_country
        get_title.date_added = input_date_added
        get_title.release_year = input_release_year
        get_title.rating = input_rating
        get_title.duration = input_duration
        get_title.listed_in = input_listed_in
        get_title.description = input_description

        db.session.commit()

    return "Successfully updated record in database"



#?id=s1
@app.route('/delete', methods=['DELETE'])
def delete_record():
    input_show_id = request.args.get('id')

    if request.method == 'DELETE':

        get_title = NetflixTitles.query.get(input_show_id)
        db.session.delete(get_title)
        db.session.commit()

    return "Successfully removed record in database"




@app.route('/stats/release_year/', methods=['GET'])
def release_year_stats():
    if request.method == 'GET':
        years = NetflixTitles.query.with_entities(NetflixTitles.release_year).all()

        release_year_count = {}

        for year in years:

            if year[0] not in release_year_count:
                release_year_count[year[0]] = 1

            else:
                oldCount = release_year_count[year[0]]
                release_year_count[year[0]] = oldCount + 1

    return release_year_count

@app.route('/stats/country/', methods=['GET'])
def country_stats():
    if request.method == 'GET':
        group_countrys = NetflixTitles.query.with_entities(NetflixTitles.country).all()

        country_count = {}

        for countrys in group_countrys:
            countrys = countrys[0].split(',')

            for country in countrys:
                if country not in country_count:
                    country_count[country] = 1

                else:
                    oldCount = country_count[country]
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



if __name__ == '__main__':
    app.run()
