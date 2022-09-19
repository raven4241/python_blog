from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

name = "Atharva"

app.route('/')
def home():
  return render_template('home.html', name=name)

if __name__ == "__main__":
  app.run()
