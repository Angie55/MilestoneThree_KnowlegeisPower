import os
import math
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

# creating instance of flask
app = Flask(__name__)

# connecting app to MongoDB using a environment variable
app.config["MONGO_DBNAME"] = 'knowledge_is_power'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# creating an instance of PyMongo
mongo = PyMongo(app)

# displays home page
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    return render_template("contact-us.html")
    
# Read

# displays fundraisers from the database on the fundraisers page
@app.route('/get_fundraisers')
def get_fundraisers():
    """
    The code below displays a limited number of fundraisers on a page
    with pagination.
    It also sorts the fundraisers by ID in decending order so the newest
    one added is at the top of page 1.
    """
    page_limit = 6
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.fundraisers.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    fundraiser = mongo.db.fundraisers.find().sort('_id', pymongo.DESCENDING).skip(
        (current_page - 1)*page_limit).limit(page_limit)
        
    return render_template("fundraisers.html",
                          fundraisers=fundraiser,
                          current_page=current_page,
                          pages=pages)
    
# display of individual fundraiser using id
@app.route('/get_fundraisers/<fundraisers_id>')
# uses the id to display the details for the selected fundraiser when read more clicked
def fundraiser(fundraisers_id):
    fundraiser_info = mongo.db.fundraisers.find_one({"_id": ObjectId(fundraisers_id)})
    return render_template("fundraiser-info.html",
                            fundraiser=fundraiser_info)
                              
# Create

# displays page to add a fundraiser form
@app.route('/add_fundraiser')
def add_fundraiser():
    return render_template("add-fundraiser.html")
    
# inserts new fundraiser when form submitted
@app.route('/insert_fundraiser', methods=['POST'])
def insert_fundraiser():
    fundraisers = mongo.db.fundraisers
    fundraisers.insert_one(request.form.to_dict())
    flash('Success! The fundraiser has been added')
    return redirect(url_for('get_fundraisers'))
    
# Update

# displays the edit fundraiser page with the form that is filled in with that fundraisers current details
@app.route('/edit_fundraiser/<fundraiser_id>')
def edit_fundraiser(fundraiser_id):
    the_fundraiser = mongo.db.fundraisers.find_one({"_id": ObjectId(fundraiser_id)})
    flash('Success! The fundraiser has been updated')
    return render_template('edit-fundraiser.html', fundraiser=the_fundraiser)

# updates the fundraiser with the details that were submitted
@app.route('/update_fundraiser/<fundraiser_id>', methods=["POST"])
# uses id of the fundraiser created by MongoDB to target and just update that fundraiser details
def update_fundraiser(fundraiser_id):
    fundraisers = mongo.db.fundraisers
    fundraisers.update({'_id': ObjectId(fundraiser_id)},
        {
        'fundraiser_name': request.form.get('fundraiser_name'),
        'fundraiser_target': request.form.get('fundraiser_target'),
        'fundraiser_country': request.form.get('fundraiser_country'),
        'fundraiser_image': request.form.get('fundraiser_image'),
        'fundraiser_website_link': request.form.get('fundraiser_website_link'),
        'fundraiser_intro': request.form.get('fundraiser_intro'),
        'fundraiser_details': request.form.get('fundraiser_details')
        })
    return redirect(url_for('get_fundraisers'))

# Delete

# deletes the fundraiser from the database using it's id
@app.route('/delete_fundraiser/<fundraiser_id>')
def delete_fundraiser(fundraiser_id):
    mongo.db.fundraisers.remove({'_id': ObjectId(fundraiser_id)})
    flash('Success! The fundraiser has been deleted')
    return redirect(url_for('get_fundraisers'))
    
# Search
    
# searches fundraisers and displays any that have the input value in the title or country
@app.route('/search', methods=['GET', 'POST'])
def search():
    # gets the value of the search input from the fundraisers page
    search_input = request.form.get("search_input")
    search_string = str(search_input)
    
    # narrows down search to just use name and counrty in search for input in fundraisers
    mongo.db.fundraisers.create_index([('fundraiser_name', 'text'),
                                      ('fundraiser_country', 'text')])
    
    # Searches results and sorts by id
    search_results = mongo.db.fundraisers.find(
        {"$text": {"$search": search_string}}).sort([("_id", -1)])
        
    # counts number of results for if statement below
    results_count = mongo.db.fundraisers.count_documents(
        {"$text": {"$search": search_string}})
    
    if request.method == 'POST':
        
        # If there is no search input flash the message
        if search_string == '':
            
            flash('You have not provided any search input! Please type in a word or take a look at the fundraisers below.')
            
            return redirect('/get_fundraisers')
        
        # If no results display then flash this message showing their input
        elif results_count == 0:
            
            flash(f'No matching results found for "{search_input}". Please try a different search or browse through our fundraisers below')
            
            return redirect('/get_fundraisers')
            
        # Display search result
        else:
            search_results
    return render_template("search-results.html", fundraisers=search_results)
    
# runs the app
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
        