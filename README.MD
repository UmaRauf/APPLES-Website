TO RESET DB (python console)

-from application import app
-from models import init_db
-with app.app_context():
     init_db(app)
enter 