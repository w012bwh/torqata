# Netflix Movies and TV Shows

python libraries needed before running

    pip install flask

    pip install flask_sqlalchemy

    pip install flask_swagger_ui

Software could use but not required

    postman - send get/post/put/delete
    DataGrip / whatever you may use to connect to a database

Steps to setup environment

The PostgresSQL database is running in GoogleCloudDB however, you can edit the sql script to create new instance

make sure the project is a folder in your c:\ directory named torqata or else the script will fail otherwise edit the 
file to where the csv file is located. 

1) run the above pip commands

2) setup the database if you do not want to use the run currently running
psql -U postgres -h 34.135.240.167 -d netflix_data -f create-torqatadb.sql

3) run "flask run"

4) go to http://127.0.0.1:5000/api/docs/ for api information
   1) below are typed out requests for your convenience
      1) /filter/type
         1) ?type=movie or ?type=tv show
      2) /add
         1) ?id=8808&title=test&type=test&director=test&cast=test&country=test&date_added=test&release_year=test&rating=test&duration=test&listed_in=test&description=test
      3) /update
         1) ?id=8808&title=test2&type=test&director=test&cast=test&country=test&date_added=test&release_year=test&rating=test&duration=test&listed_in=test&description=test
      4) /delete
         1) ?id=8808
