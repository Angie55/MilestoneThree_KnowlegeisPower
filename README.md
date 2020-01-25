# [Knowledge is Power](https://knowledge-is-power-milestone.herokuapp.com/)

Knowledge is Power is a app for users to view fundraiser focused on raising money to educate people around the world. 
The idea comes from the belief that teaching even basic skills is the key to getting people out of poverty and able to
support themselves as well as pass on knowledge.  Users can collaborate on raising awareness as fundraisers can be added,
edited and deleted by the users so everyone can get involved and help keep things up to date. The hope is by having a 
collection of education fundraisers in one place people are more likely to contribute to a few or help spread awareness 
on any they really resonate with them.

## Developer goals

- To create a app with Flask and MongoDB that has the CRUD operations of Create, Read, Update and Delete to showcase skills 
learnt in the data centric development module of the [Code Institute](https://codeinstitute.net/) course I am taking. This app was created 
for the 3rd milestone project.

- To create an aesthetically pleasing and easy to navigate app with clear feedback for users.

- To create a basic log in feature 

- To gain knowledge and improve on what I have learnt on the creation of a CRUD application from start to finish.

---

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Color Scheme**](#color-scheme)
        - [**Typography**](#typography)
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

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Acknowledgements**](#acknowledgements)
    - [**Media**](#media)
    - [**Code**](#code)
    
---

## UX


### User Stories (#user-stories)

"**_Users who would be interested in the app_** ____"

- Philanthropists and genera charity donors looking for ways they can help spread the word or contribute to education funds.

- Fundraisers who have create a donation page and would like to raise awareness.


"**_As a user I would like to_** ____"
- View the site on various devices from a large desktop to a mobile.
- See a homepage with information about the site and how I can get involved/what I can do.
- To add fundraisers with an easy to follow form.
- To edit fundraisers added by myself or others if I have an update.
- To delete fundraisers that have ended
- To view the newest first and see added ones appear at the top.
- To be able to search by title to see if a fundraiser I know is there. 
- To be able to search by country of the fundraisers beneficiaries. 
- View a limited number of fundraisers at a time so I don’t have to scroll forever if there are a lot of fundraisers.
- View a range of fundraisers at a glance on one page and read more if I choose.
- Read about the fundraisers- the target to raise, country of beneficiaries and have some details about it.
- Have a clear link to the page I can donate to the fundraiser on.

### Design-

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

### Wireframes

My wireframes for this project can be found [here](https://github.com/Angie55/MilestoneThree_KnowlegeisPower/tree/master/static/images/Wireframes).

##### back to [top](#table-of-contents)

---

## Features

### Existing Features

**Create**
- Add a recipe allows users to add fundraisers. The form has a defensive design as all forms are required to submit and the user
sill see guided feedback to support them. Minimum characters are set where needed to ensure some information is added.

**Read**
- All fundraisers can be viewed with 6 visible on page at a time. They are displayed newest to oldest so users see the latest 
addition first and see newly added fundraisers immediately at the top. More information and details of each fundraiser can be 
viewed when the link is clicked. 

**Update**
- All fundraisers can be edited from the fundraiser info page. The defensive designs follows the same rules as when adding a fundraiser.

**Delete**
- Fundraisers can be removed after 2 clicks with a warning on the first. The defensive design ensures it is not too easy for users to delete a fundraiser.

**Search**
- The fundraisers can be searched by a keyword in the title if by the country. These display on a new page. The user stays on 
the fundraisers page if no results are found or there is no input.


### Features Left to Implement
These features are things I had planned to implement but did not have the time, some basic parts of this project took me longer than expected
as I'm very new to backend coding and need a lot more practice to get my head around things. With the knowledge I have now I could plan my time 
a lot better to allow time for all planned features. The features in this list are not part of the grading but were features I wanted to add for 
development.

**Register/Login**
- An attempt was made to set this up but I spent alot of time researching to get my head around the basics that there was not time to implement to 
a good enough standard before submission.

I have included some details of my attempt [here](https://github.com/Angie55/MilestoneThree_KnowlegeisPower/blob/master/static/images/readme-docs/login-register-writeup.pdf)

**Users image upload** 
- I wanted users to be able to upload an image from file as this would be more reliable and predictable in terms the way it displays on the app. 
It would have size guides and restrictions as well as still display even if the link is broken or images changed on the fundraiser page. 

**Filters**
- This would include the choice of displaying the fundraisers as newest or oldest first, by order of target amount. As the app potentially
grows with alot of fundraisers it would be good to have a choice of ways to search

**Contact us**
- I wanted to add a contact page that users could fill in that would send me an email.

### Possible future development ideas
This developments were not planned as part of the project but are ideas that could maybe be considered in future.

**Fundraiser default image**
- It could be a good idea for users who have difficulty finding a good image to be able to choose from a few attracive images in place of uploading one 
themselves. The images would be education themed.

**Categories**
- Potentially there could be seperate categories for fundraiser for childrena dn adults.

**Close to target tick box**
- It would be good is users could click a star icon when fundraisesr are close to target and user could also filter to them. This would be to inspire a last push 
to get the fundraiser to it's target quicker.

**Info on who add,edited or deleted and the date**
- If users had accounts there could be a display of who uploaded or last edited a fundraiser as a way to monitor miss-use.  

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

- HTML- [W3C HTML Validator](https://validator.w3.org/)- All pages pass, errors show due to jinja code but this is expected.
- CSS- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator)- Passed.
- Python- [PEP8 Online](http://pep8online.com/checkresult)- I fixed any under/over indented, trailing white space and or other unneeded spaces.
 I found some changes seemed to effect the code and I can't risk changing something that effects the app working right now. I will use the 
validator as I go in future as I do with CSS and HTML to ensure my code is fully complient.

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

### Images

- Favicon and logo display on all pages. Images are responsive and resize well. See bugs and fixes for slight issue. 

### Links and buttons

- All links go to the correct page when clicked and open in a new tab where this is set.
- All links and button have hover effects that work and give the user feedback that they can click.

### Bugs and known issues

- Fundraisers images are not centered when the screen width is 830px-1025px wide.
- When on the edit fundraiser form, if the user did not edit it and navigates away form the page, a flash message still appears that it has been successfully updated.
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

I have created a spreadsheet of my testing and results that you can view [here](https://github.com/Angie55/MilestoneThree_KnowlegeisPower/blob/master/static/images/readme-docs/testing-matrix.pdf)

##### back to [top](#table-of-contents)

---

## Deployment

### Local deployment

The following will need to be installed on your own system/IDE in order to run this project locally:

- Python 3 to run the application.
- PIP to install all the app requirements.
- GIT for version control and cloning.

- Sign up to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)- to create the database.
You will need to create a cluster and then in collections create a new database which should be called ‘knowledge_is_power'.
Then create a collection called ‘fundraisers'. You can change this name but must be sure to amend the python file where these collection 
name occurs in order to connect with the database. 

<img src="https://github.com/Angie55/MilestoneThree_KnowlegeisPower/blob/master/static/images/readme-docs/mongo_fundraisers.png" alt="MongoDB collection screen shot" width="800">

- Clone this GitHub repository by either clicking the green *Clone or download* button and downloading the project as a zip-file (unzip it first), or by entering the following into the Git CLI terminal:
    - `https://github.com/Angie55/MilestoneThree_KnowlegeisPower.git`.
- Install all requirements from the requirements.txt file using this command:
    - `pip -r requirements.txt.`
- Create a secret key and put this in the .bashrc and set it as an environment variable as *SECRET_KEY*.
- Set the Mongo URI as an environment variable in the .bashrc 
- You should now be able to run the app.

### Remote deployment

This site has been deployed on Heroku using the master branch on Github. The following steps were taken to deploy this project:

- A requirement.txt file was created so Heroku can install the required dependencies to run the app. This was created by typing 
`sudo pip3 freeze –local > requirements.txt` into the git bash terminal. It is 
important this is done before attempting to deploy on Heroku is order for it to work.
- A Profile was created which tells Heroku what type of application is being deployed and how to run it. This was created with the command `echo web: python run.py > Profile`.
- I logged into my Heroku account, a free account can be created, then created a new app named 'knowledge-is-power-milestone'.
- I went to the ‘Setting' tab and clicked ‘Reveal Config Vars’ to add the following environment variables:
   - IP: 0:0:0:0
   - PORT: 8080
   - MONGO_URI: <pasted link to my MongoDB> (the same link that is in the bash.rc saved as an environment variable)
   - SECRET_KEY: <pasted my secret key> (the same link that is in the bash.rc saved as an environment variable)
- I went to the 'Deploy' tab and selected the option to ‘Connect Github’ as the deployment method and also selected ‘Enable Automatic Deployment’. This means each time I commit changes to GitHub once the app 
is deployed it will be up-to-date with the latest chnages.  
- I clicked ‘Deploy Branch’ on the 'Deploy' page in the 'Manual deploy' section and my project was successfully deployed.

##### back to [top](#table-of-contents)

## Acknowledgements

### Media

Images were sourced from:

- [Save the children](https://www.savethechildren.org.uk/what-we-do/education) - (one image on the homepage)

- [Pixabay](https://pixabay.com/)- All other images apart from fundraisers added by users.

### Credits

- The CRUD functions were created following tutorials by [Code Institute](https://codeinstitute.net/)

- Slack was used a s source of information. Many questions I entered in the search had already been answered and I 
looked at the suggested code from mentors and students.  All code had to be modified to fit my project. The 
pagination and search are examples or looking at various fellow students code and putting together what worked for me.


**Disclaimer**- This app was created for education purposes.

##### back to [top](#table-of-contents)
