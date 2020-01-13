import os
import math
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

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
    
# displays to home page  
@app.route('/contact_us')
def contact_us():
    return render_template("contact-us.html")    
    
# route to login page      
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Function for handling the logging in of users"""
    if 'logged_in' in session:  # Check is already logged in
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        user = mongo.db.users
        logged_in_user = user.find_one({
                                'name': request.form['username'].title()})

        if logged_in_user:
            if check_password_hash(logged_in_user['pass'],
                                   request.form['password']):
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('index'))
            flash('Sorry incorrect password!')
            return redirect(url_for('login'))
    return render_template('login.html')  
    
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Function for handling the registration of users"""
    if 'logged_in' in session:  # Check is user already logged in
        return redirect(url_for('index'))

    if request.method == 'POST':

        user = mongo.db.users
        dup_user = user.find_one({'username': request.form['username'].title()})

        if dup_user is None:
            hash_pass = generate_password_hash('password')
            user.insert_one({'username': request.form['username'].title(),
                             'password': hash_pass})
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('index'))

        flash('Sorry, username already taken. Please try another. If you have an account please login')
        return redirect(url_for('register'))
    return render_template('register.html')
    
@app.route('/logout')
def logout():
    """Logs the user out and redirects to home"""
    session.clear()  # Kill session
    return redirect(url_for('login'))    
    
    
# Read

# displays fundraisers from the database on the fundraisers page  
@app.route('/get_fundraisers')
def get_fundraisers():
    
    """
    The code below displays a limited number of fundraisers on a page
    with pagination. The num of fundraisers is counted and a limit per
    page set with a number added each time the page limit is exceeded
    view that page would be added.
    It also sorts the fundraisers by ID in decending order so the newset
    one added is at the top of page 1.
    """
    page_limit = 4  # Logic for pagination
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
    fundraiser_info =  mongo.db.fundraisers.find_one({"_id": ObjectId(fundraisers_id)})
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
    flash('The fundraiser has been added')
    return redirect(url_for('get_fundraisers')) 
    
# Update   

# displays the edit fundraiser page with the form that is filled in with that fundraisers current details   
@app.route('/edit_fundraiser/<fundraiser_id>')
def edit_fundraiser(fundraiser_id):
    the_fundraiser =  mongo.db.fundraisers.find_one({"_id": ObjectId(fundraiser_id)})
    flash('The fundraiser has been updated')
    return render_template('edit-fundraiser.html', fundraiser=the_fundraiser) 

# updates the fundraiser with the details that were submitted  
@app.route('/update_fundraiser/<fundraiser_id>', methods=["POST"])
# uses id of the fundraiser created by MongoDB to target and just update that fundraiser details
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

# Delete

# deletes the fundraiser from the database using it's id  
@app.route('/delete_fundraiser/<fundraiser_id>')
def delete_fundraiser(fundraiser_id):
    mongo.db.fundraisers.remove({'_id': ObjectId(fundraiser_id)})
    flash('The fundraiser has been deleted')
    return redirect(url_for('get_fundraisers')) 
    
    
 
# runs the app
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)  
        


