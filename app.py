from flask import Flask
from models.database import db

app = None

def create_app():
      app = Flask(__name__, template_folder="templates")
      app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_master.db'
      db.init_app(app)
      app.app_context().push()
      return app

app = create_app()

from controllers.user_controller import *
from controllers.admin_controller import *
from controllers.login_signup import *

if __name__ == '__main__':
  # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)