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


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/get_fundraisers')
def get_fundraisers():
    return render_template("fundraisers.html",
                            fundraisers=mongo.db.fundraisers.find())
    
    
#display of individual fundraiser using id   
@app.route('/get_fundraisers/<fundraisers_id>')
def fundraiser(fundraisers_id):
    fundraiser_info =  mongo.db.fundraisers.find_one({"_id": ObjectId(fundraisers_id)})
    return render_template("fundraiser-info.html",
                              fundraiser=fundraiser_info)  
    
#displays the add fundraiser page with the form
@app.route('/add_fundraiser')
def add_fundraiser():
    return render_template("add-fundraiser.html")
    
#inserts new fundraiser when form submitted    
@app.route('/insert_fundraiser', methods=['POST'])
def insert_fundraiser():
    fundraisers = mongo.db.fundraisers
    fundraisers.insert_one(request.form.to_dict())
    return redirect(url_for('get_fundraisers')) 
    
    
    
@app.route('/edit_fundraiser/<fundraiser_id>')
def edit_fundraiser(fundraiser_id):
    the_fundraiser =  mongo.db.fundraisers.find_one({"_id": ObjectId(fundraiser_id)})
    the_country = mongo.db.fundraisers.find_one("fundraiser_country")
    return render_template('edit-fundraiser.html', fundraiser=the_fundraiser,
                                                   country=the_country)    
   
                
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)  
        


