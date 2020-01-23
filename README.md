# [Knowledge is Power](https://knowledge-is-power-milestone.herokuapp.com/)

Knowledge is Power is a app for users to view fundraiser focused on raising money to educate people around the world. 
The idea comes from the belief that teaching even basic skills is the key to getting people out of poverty and able to
support themselves as well as pass on knowledge.  Users can collaborate on raising awareness as fundraisers can be added,
edited and deleted by the users so everyone can get involved and help keep things up to date. The hope is by having a 
collection of education fundraisers in one place people are more likely to contribute to a few or help spread awareness 
on any they really resonate with them.

## Developer goals

-To create a app with Flask and MongoDB that has the CRUD operations of Create, Read, Update and Delete to showcase skills 
learnt in the data centric development module of the [Code Institute](https://codeinstitute.net/) course I am taking. This app was created 
for the 3rd milestone project.

-To create an aesthetically pleasing and easy to navigate app with clear feedback for users.

-To create a basic log in feature 

-To gain knowledge and improve on what I have learnt on the creation of a CRUD application from start to finish.

---

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Color Scheme**](#color-scheme)
        - [**Layout**](#layout)
        - [**Typography**](#typography)
        - [**Imagery**](#imagery)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
    - [**Possible future development ideas**](#possible-future-development-ideas)

3. [**Technologies Used**](#technologies-used)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)

4. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Add a fundraiser**](#add-a-fundraiser)
    - [**Edit a fundraiser**](#edit-a-fundriaser)
    - [**Delete a fundraiser**](#delete-a-fundraiser)
    - [**Search**](#search)
    - [**Pagination**](#pagination)
    - [**General tests**](#general-tests)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

---

## UX


### User Stories (#user-stories)

"**_Users who would be interested in the app_** ____"

-Philanthropists and genera charity donors looking for ways they can help spread the word or contribute to education funds.

-Fundraisers who have create a donation page and would like to raise awareness.


"**_As a user I would like to_** ____"
-View the site on various devices from a large desktop to a mobile
-See a homepage with information about the site and how I can get involved/what I can do.
-To add fundraisers with an easy to follow form
-To edit fundraisers added by myself or others if I have an update.
-To delete fundraisers that have ended
-To view the newest first and see added ones appear at the top.
-To be able to search by title to see if a fundraiser I know is there. 
-To be able to search by country of the fundraisers beneficiaries. 
-View a limited number of fundraisers at a time so I don’t have to scroll forever if there are a lot of fundraisers.
-View a range of fundraisers at a glance on one page and read more if I choose.
-Read about the fundraisers- the target to raise, country of beneficiaries and have some details about it.
-Have a clear link to the page I can donate to the fundraiser on.
-See feedback when I submit a form/login or out/register etc.
-Be able to log in and log out
-Register an account

### Design


#### Color Scheme

The colours were chosen after looking at a range of websites of charities that focus on raising money for education. I found a 
warm orange is used a lot perhaps to create a sense or urgency and chose this as the main colour. For this colour to stand out
well it was best to keep a white background throughout. The blues and greens are also colours seen across the sites I looked at
on buttons and features.  They are friendly and green is good for an action buttons and making certain information stand out.

- ![#ff8500](https://placehold.it/15/ff8500/ff8500) `#ff8500` (**Orange** )
- ![#505050](https://placehold.it/15/505050/505050) `#505050` (**Dark Grey** )
- ![#03ADDF](https://placehold.it/15/03ADDF/03ADDF) `#03ADDF` (**Bright Blue** )
- ![#94c83d](https://placehold.it/15/94c83d/94c83d) `#94c83d` (**Bright Green** )

#### Typography

I used Oswald is the font for headers, it was a free font that is comparable to fonts I had seen on charity sites. It is clear 
and bold and works well with the theme of urgency and giving. Lato was used as the main text has a soft friendly feel to keep a 
chirpy feel to the details of what good will come from supporting the fundraisers.


#### Layout

#### Imagery


### Wireframes

My wireframes for this project can be found [here](https://github.com/Angie55/MilestoneThree_KnowlegeisPower/tree/master/static/images/Wireframes).

##### back to [top](#table-of-contents)

---

## Features

### Existing Features

**Create**
-Add a recipe allows users to add fundraisers. The form has a defensive design as all forms are required to submit and the user
sill see guided feedback to support them. Minimum characters are set where needed to ensure some information is added.

**Read**
-All fundraisers can be viewed with 6 visible on page at a time. They are displayed newest to oldest so users see the latest 
addition first and see newly added fundraisers immediately at the top. More information and details of each fundraiser can be 
viewed when the link is clicked. 

**Update**
-All fundraisers can be edited from the fundraiser info page. The defensive designs follows the same rules as when adding a fundraiser.

**Delete**
-Fundraisers can be removed after 2 clicks with a warning on the first. The defensive design 

**Search**
-The fundraisers can be searched by a keyword in the title if by the country. These display on a new page. The user stays on 
the fundraisers page if no results are found or there is no input.

**Register**

**Login**

### Features Left to Implement
These features are things I had planned to implement but did not have the time, some basic parts of this project took me longer than expected
as I'm very new to backend coding and need a lot more practice to get my head around things. With the knowledge I have now I could plan my time 
a lot better to allow time for all planned features. I do not believe any features in this list are part of the grading, to my knowledge I have
for filled the project requirements.

**Users image upload** 
-I wanted users to be able to upload an image from file as this would be more reliable and predictable in terms the way it displays on the app. 
It would have size guides and restrictions as well as still display even if the link is broken or images changed on the fundraiser page. 

**Filters**
-This would include the choice of displaying the fundraisers as newest or oldest first, by order of target amount. As the app potentially
grows with alot of fundraisers it would be good to have a choice of ways to search

**Contact us- email sends**
-I wanted to add a contact page that users could fill in that would send me an email.

**Password match check and change password**
The current login/ register is very basic as a first practice, it was not part of the requirements for the project but i wanted to give it a go.
As a basic standard i would add:
- a confirm password to make sure the user is sure of their password.
- more restriction/rules on the password such as it having to have a cap letter and number.
- an option to reset the password
- the use of email in registering
- a uer account page to update details

**Username displayed on main nav**
-It would be helpful for the user to have information in the main nav that they are logged in and the username they are logged in as.

### Possible future development ideas
This developments were not planned as part of the project but are ideas that could maybe be considered in future.

**Fundraiser default image**
It could be a good idea for users who have difficulty finding a good image to be able to choose from a few attracive images in place of uploading one 
themselves. The images would be education themed.

**Categories**
-Potentially there could be seperate categories for fundraiser for childrena dn adults.

**Close to target tick box**
-it would be good is users could click a star icon when fundraisesr are close to target and user could also filter to them. This would be to inspire a last push 
to get the fundraiser to it's target quicker.

**Info on who add,edited or deleted and the date**
If users had accounts there could be a display of who uploaded or last edited a fundraiser as a way to monitor mis-use.  

##### back to [top](#table-of-contents)

---

## Technologies Used

- [AWS Cloud9](https://aws.amazon.com/cloud9/) - IDE for coding.
- [GitHub](https://github.com/) - Used as remote storage of my code online.
- [Photoshop CS6](https://www.adobe.com/Photoshop) - Used for editing images.
- [git](https://git-scm.com/)- used as a respository.

### Front-End Technologies

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [Google fonts](https://fonts.google.com/) – a link to Google fonts is used to style fonts on the website.
- [Bootstrap](https://getbootstrap.com/) - Used to help with the layout, navigation and making the site responsive as main design framework.
- [jQuery 3.4.1](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality in Bootsrap framework.
- [Popper.js ](https://popper.js.org/) - Used through bootstrap for responsive navigation.

### Back-End Technologies

- **Flask**
    - [Flask 1.1.1](http://flask.pocoo.org/) - Used as a microframework.
    - [Jinja2 2.10.3](http://jinja.pocoo.org/docs/2.10/) - Used for templating with Flask.
    - [Werkzeug 0.16.0](https://werkzeug.palletsprojects.com/en/0.16.x/) - Used for password hashing and checking the password.
- **Heroku**
    - [Heroku](https://www.heroku.com) - Used for app hosting.
- **Python**    
    - [Python 3.6.8](https://www.python.org/) - Used as the back-end programming language.
    - [MongoDB Atlas](https://www.mongodb.com/) - Used to store my database.
    - [PyMongo 3.10.0](https://api.mongodb.com/python/current/) - Used as the Python API for MongoDB.
    
##### back to [top](#table-of-contents)

---

## Testing

### Validators

### Add a fundraiser

"**_Users are able to_** ____"

- Easily locate the add a fundraiser links that appear in relevant pages.
- See a clear responsive form on any size device.
- Get clear feedback if form field that is required not filled in.
- Type or increment by one on the target amount number field and can’t enter less than '0'. Only numbers can be typed except for 'e' for which is 
standard on number input fields. This is noted a something to remove as when put on the field it displays as 5e3.
- See how many characters they need to add take away to fit the correct range for the introduction.
- See how many characters they need to add for the minimum on the fundraiser details.
- On clicking submit if all input fields have been validated the new fundraiser is added to the top of the fundraisers page. So the user can see
it immediately when they are redirected to the fundraisers page. All the details are then available when they click to read more.

### Edit a fundraiser-

"**_Users are able to_** ____"

- See a clear responsive form on any size device.
- See the current details for that fundraiser displayed within the form ready to edit including the correct country from the list. 
- Get feedback if they delete the input and leave it blank that it is required. This includes feedback if the character count is too high or low for a particular field.
- See clear feedback that the fundraiser has been updated with an alert they can close if they want to.
- See the changes from the edit immediately.

### Delete a fundraiser-

"**_Users are able to_** ____"

- Avoid hastily deleted or deleting by accident with an extra step/warning modal. This makes it clear that the fundraiser will be permanently deleted when the second delete button is clicked. 
- Close the modal if they decide not to delete the fundraiser in various ways such as the close button, X and by clicking anywhere on the page outside the modal.
- See clear feedback that the fundraiser has been deleted with an alert they can close if they want to.

### Search

"**_Users are able to_** ____"

- Search by using either the country or a key word on the title.
- If a result is found all the fundraisers with that word or for that country will show in that same layout as the main fundraisers page.
- Read more about that fundraiser from the search results page.
- Access the add a fundraiser from the search results page is they were checking if the one they want to add already exists.
- Click a link after the last result to go back to fundraiser page from there.
- See clear feedback for their search when no results found with a message that shows their search such as ‘No matching results found for "susa". Please try a different search or browse through 
our fundraisers below’. This helps them see if they have miss spelled/typed the word.
- See clear feedback if they do not type anything in the search input.


**Search word test-**

- Partial words do not give a result, it currently has to be a full word for most searches. It did show me the results for words missing the last letter such as ‘Beliz’ for ‘Belize’ and  ‘fundraise’ 
for ‘fundraiser’ but missing one letter did not work on other searches like ‘susa’ for ‘susan’
- I did not get a result for words such as ‘to’ or ‘not’ even though it is in a title. I then checked to make sure it was not just finding the first word and it did get results for words such a ‘build’ 
and ‘Scholarship’ and ‘restoring’ that where in the middle or end of the title.
- ‘kingdom’ was searched for with the ‘united’ missing for the country and it still found the fundraiser with that country. Just ‘King’ did not give a result.
- ‘Hong was searched and found the result for ‘Hong Kong’
- Whether the word is typed upper, lower or mixed does not matter.

### Pagination

Enough fundraisers were added and deleted to create 3 pages and bring it back down to 1 for testing.

- Displays 6 fundraisers at a time
- Creates a new page as soon as the number of fundraisers go to 7 then another once it reaches 13 and so on when the number reaches the page limit +1.
- A page is removed when deleting a fundraisers bring the number down to 6 from 7 for example.
- The current page is clearly highlighted and the page switches to the page number that is clicked on.

### General tests

### Homepage, Fundraisers page and fundraiser info pages

### Images

- Favicon and logo display on all pages. Images are responsive and resize well. 

### Links and buttons

- All links go to the correct page when clicked and open in a new tab where this is set.
- All links and button have hover effects that work and give the user feedback that they can click.


### Bug, fixes and future ideas

- Edit form- had some issue displaying the intro and details in the form fields.
- User feedback (for add,edit etc)- this site currently uses the same green alert to let the user know when forms are submitted but also when search results.
- Search- full words need to be typed, this could be developed to search for partial words to help with miss typing/spelling.
- Pagination could be added to the search in future in anticipation that there will be enough for it to be too many to scroll through at a time.

### Compatibility

I tested the latest version 6 of the main browsers to ensure a broad range of users can successfully use this site in both desktop and mobile configuration.

- Chrome 
- Edge 
- Firefox 
- Safari 
- Opera 
- Internet Explorer 

I have created a spreadsheet of my testing and results:

<add link>

##### back to [top](#table-of-contents)

---

# Deployment

## Local deployment

The following will need to be installed on your own system/IDE in order to run this project locally:

- Python 3 to run the application.
- PIP to install all the app requirements.
- GIT for version control and cloning.

- Sign up to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)- to create the database.
You will need to create a cluster and then in collections create a new database which should be called ‘knowledge_is_power'.
Then create 2 collections called ‘fundraisers' and 'users'. You can change these names but must be sure to amend the python file where these collection 
names occur in order to connect with the database.

- Clone this GitHub repository by either clicking the green *Clone or download* button and downloading the project as a zip-file (unzip it first), or by entering the following into the Git CLI terminal:
    - `https://github.com/Angie55/MilestoneThree_KnowlegeisPower.git`.
- - Install all requirements from the requirements.txt file using this command:
    - `pip -r requirements.txt.`
- Create a secret key and put this in the .bashrc and set it as an environment variable as *SECRET_KEY*.
- Set the Mongo URI as an environment variable in the .bashrc 
- You should now be able to run the app.

