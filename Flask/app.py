from flask import Flask, request
from flask_pymongo import PyMongo
from bson import json_util
import re

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://admin:pass@mongodb:27017/movie_db?authSource=admin"
mongo = PyMongo(app)

@app.route('/')
def default():
    return '<h1>Hello, you are connected</h1>'

@app.route('/search/names', methods=['GET'])
def search_names():
    
    # Get query parameters from the request
    name = request.args.get('name')
    name_id = request.args.get('name_id')
    yearBorn = request.args.get('yearBorn')
    yearDied = request.args.get('yearDied')
    

    # Get the collection
    collection = mongo.db.names

    # Initialize query dictionary
    query = {}

    # Check if name or id is provided in the request
    if name:
        query['name'] = name
    elif name_id:
        query['name_id'] = name_id
    elif yearBorn:
        query['yearBorn'] = yearBorn
    elif yearDied:
        query['yearDied'] = yearDied
        
    # Perform the query
    results = collection.find(query)

    # Convert the cursor to a list of dictionaries
    matching_records = list(results)

    if not matching_records:
        return '<h1>Invalid Result</h1>'

    # Use json_util to handle MongoDB specific objects (like ObjectId)
    return json_util.dumps(matching_records), 200

@app.route('/search/titles', methods=['GET'])
def search_titles():
    
    # Get query parameters from the request
    title = request.args.get('title')
    title_id = request.args.get('title_id')
    year = request.args.get('year')
    runtime = request.args.get('runtime')
    genre = request.args.get('genre')
    

    # Get the collection
    collection = mongo.db.titles

    # Initialize query dictionary
    query = {}

    # Check if name or id is provided in the request
    if title:
        query['title'] = title
    elif title_id:
        query['title_id'] = title_id
    elif year:
        query['year'] = year
    elif runtime:
        query['runtime'] = runtime
    elif genre:
        # Construct a regex pattern for substring searching and make it case insensitive
        regex_pattern = re.compile(genre, re.IGNORECASE)
        query['genre'] = regex_pattern
        
    # Perform the query
    results = collection.find(query)

    # Convert the cursor to a list of dictionaries
    matching_records = list(results)

    if not matching_records:
        return '<h1>Invalid Result</h1>'

    # Use json_util to handle MongoDB specific objects (like ObjectId)
    return json_util.dumps(matching_records), 200  

@app.route('/search/roles', methods=['GET'])
def search_roles():
    
    # Get query parameters from the request
    title_id = request.args.get('title_id')
    name_id = request.args.get('name_id')
    category = request.args.get('category')
    characters = request.args.get('characters')
    

    # Get the collection
    collection = mongo.db.roles

    # Initialize query dictionary
    query = {}

    # Check if name or id is provided in the request
    if title_id:
        query['title_id'] = title_id
    elif name_id:
        query['name_id'] = name_id
    elif category:
        query['category'] = category
    elif characters:
        # Construct a regex pattern for substring searching and make it case insensitive
        regex_pattern = re.compile(characters, re.IGNORECASE)
        query['characters'] = regex_pattern
        
    # Perform the query
    results = collection.find(query)

    # Convert the cursor to a list of dictionaries
    matching_records = list(results)

    if not matching_records:
        return '<h1>Invalid Result</h1>'

    # Use json_util to handle MongoDB specific objects (like ObjectId)
    return json_util.dumps(matching_records), 200  



if __name__ == "__main__":
    app.run(debug=True)