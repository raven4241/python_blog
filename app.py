from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.route('/')
def landing_page():
  return render_template('home.html')

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
