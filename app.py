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
    
    
#displays the edit fundraiser page with the form    
@app.route('/edit_fundraiser/<fundraiser_id>')
def edit_fundraiser(fundraiser_id):
    the_fundraiser =  mongo.db.fundraisers.find_one({"_id": ObjectId(fundraiser_id)})
    return render_template('edit-fundraiser.html', fundraiser=the_fundraiser) 

#updates the fundraiser with the details that were submitted  
@app.route('/update_fundraiser/<fundraiser_id>', methods=["POST"])
def update_fundraiser(fundraiser_id):
    fundraisers = mongo.db.fundraisers
    fundraisers.update( {'_id': ObjectId(fundraiser_id)},
    {
        'fundraiser_name':request.form.get('fundraiser_name'),
        'fundraiser_target':request.form.get('fundraiser_target'),
        'fundraiser_country': request.form.get('fundraiser_country'),
        'fundraiser_image': request.form.get('fundraiser_image'),
        'fundraiser_website_link':request.form.get('fundraiser_website_link'),
        'fundraiser_intro':request.form.get('fundraiser_intro'),
        'fundraiser_details':request.form.get('fundraiser_details')
    })
    return redirect(url_for('get_fundraisers'))  


#deletes the fundraiser   
@app.route('/delete_fundraiser/<fundraiser_id>')
def delete_fundraiser(fundraiser_id):
    mongo.db.fundraisers.remove({'_id': ObjectId(fundraiser_id)})
    return redirect(url_for('get_fundraisers')) 
    
@app.route('/contact_us')
def contact_us():
    return render_template("contact-us.html")    
 

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)  
        


