**APPLES WEBSITE** ver 1.0

first download the requirements listed in requirements.txt

TO RESET DB (python console)

-from application import app  
-from models import init_db  
-with app.app_context():  
-init_db(app)  
enter 

1. Images **for the website** will be in static/images  
2. Images uploaded when making blog posts will be placed in static/uploads

  

**IMPORTANT**  

1. All database info is placed in the .env file and locally (sqlite). This means that the database should work
independently on anyone's machine. However, this is not secure and not for web publishing _yet_. This will require a proper database preferably 
by using the university's (or any kind donor's) server.  
2. Additional functions such as a newsletter service can be added if there is a club email available  
3. If the university is interested in further development (https setting,database setup etc.) I will be able
to assist with major changes for the following month only.
4. Changes such as designs are easy and I will be able to help anytime.

