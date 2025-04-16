from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import settings

app = Flask(__name__)


@app.route('/')
def home():
    return "Добро пожаловать в веб-приложение автомойки!"

@app.route('/api') 
def api():
    return "здесь будет информация об автомойке!"

@app.route('/api/users')
def users():
    return "здесь будет список пользователей и информация о них!" 

@app.route('/api/services')
def services():
    return "здесь будет список услуг и информация о них!"

@app.route('/api/users/workers')
def workers():
    return "здесь будет информация о работниках!"


# Configure the database connection using SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = settings.db_conn.DATABASE_URL
if __name__ == '__main__':
    app.run(debug=True)