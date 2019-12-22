import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
#connecting app to MongoDB using a environment variable
app.config["MONGO_DBNAME"] = 'knowledge_is_power'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

#creating an instance of PyMongo to set up making the connection MongoDB
mongo = PyMongo(app)

#decorators and function that will display fundraisers from MongoDB on fundraisers page
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/get_fundraisers')
def get_fundraisers():
    return render_template("fundraisers.html", fundraisers=mongo.db.fundraisers.find())
    
    
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)  
        


