from flask import render_template
import connexion 
from flask_sqlalchemy import SQLAlchemy
from config import settings

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api')
def home():
    return render_template("home.html")






#app.config['SQLALCHEMY_DATABASE_URI'] = settings.db_conn.DATABASE_URL
if __name__ == '__main__':
    app.run(debug=True)