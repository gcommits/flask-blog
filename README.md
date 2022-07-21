# flask-blog
A full-stack blog built with Flask.
[demo.mov]

# What I learned

(1) **Don't repeat code** - In past projects I would have every html template with boostrap5 css and javascript. For this project, I created a layout.html file that created the base structure of the website, including the navigation, main content, and sidebar. For every page, I then was able to wrap content within a block and inherit the layout template. Overall, it was very satisfying to see how clean every template became.

(2) **Bootstrap 5** - This project was my second time using Bootstrap 5 after upgrading from Bootstrap 4. I found creating an offcanvas navbar to be easier than Bootstrap4 because Bootstrap 5 offered the new offcanvas component. In the future, I will be exploring React + Bootstrap 5.

(3) **Don't reinvent the wheel** - I explored new libraries. Although it was helpful knowing how to create login and registration from scratch in my last project, using FlaskForm from flask_wtf made the process much quicker. For the profile pic image upload, I also used flask_wtf.

(4) **Clean commits** - I triple checked everything before committing this project to Github. I did not want to push the code just to fix a simple error and push it again. For my last project, I had 8 commits within 20 minutes which I now find embrassing. Lastly, I noticed on my last project I pushed the project in debug mode which allows for vulnerabilities because error messages will display with too much information about my application. I wont make that mistake again!

(5) **Improved readability** - First, this was my first time using 'url_for' and it would make changing urls in the future easier. No more having to find and change all the links. Second, for the database, I used an ORM and this made my code more pythonic. Lastly, instead of having all the forms be HTML, I created a registration and login class (forms.py).

# Challenges

(1) **Form Valdiation** - Because I built the form differently than my last project, I struggled with proper valdiation. Specifically, I could not get the registration errors to display to the user. To finally resolve this issue, I discovered that the registration form required an attrbiute 'novalidate'. 

(2) **Database** - In the last project I exlcusively used MySQL and was stuck with the SQL dialect. SQLAlchemy is an object relational mapper (ORM) that allows me to access data in an object oriented way. Instead of SELECT * FROM database, with this ORM I can use pythonic code: query = db.select([data]). Specifically, I used Flask-SQLAlchemy and paired it with SQLite for development.

(3) **Circular Imports** - I did not use a MVC structure from the start, and when I first attempted to split up the models, I ran into a circular import. Resolving this was done through Miguel Greenberg's advise of creating a package. 

# Future

(1) Sub-templates to handle some repeated code

(2) Password Reset Email

(3) Admin backend for user management


# Resources

Miguel Grinburg's 2017 talk called 'Flask at Scale' given at a Python conference. Miguel gave an exceptional description of import issues. Overall, Miguel Grinburg's talks and youtube videos continue to provide new ways to optimize and understand flask.

Corey Schafer's Flask course was instrumental to expanding my Flask knowledge for this project. His project used Bootstrap 4 which led to minor discrepencies that Bootstrap 5's documentation was more than helpful in resolving.  

