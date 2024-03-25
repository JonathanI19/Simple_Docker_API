from flask import Flask, request
from flask_pymongo import PyMongo
from bson import json_util

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


    # Use json_util to handle MongoDB specific objects (like ObjectId)
    return json_util.dumps(matching_records), 200 

    
if __name__ == "__main__":
    app.run(debug=True)