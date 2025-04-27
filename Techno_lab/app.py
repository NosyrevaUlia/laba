from flask import render_template, Flask, jsonify, request
from flask_jwt_extended import JWTManager  
from sqlalchemy import Column, Integer, VARCHAR, Boolean, ForeignKey, TIMESTAMP, String
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from datetime import timedelta


load_dotenv()



app = Flask(__name__)


db = SQLAlchemy()
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'mysql+mysqlconnector://root:tYHjhgfT67GVbj24@localhost:3306/laba')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET', 'super-secret-key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

#-------------------------Models--------------------------------------------------
class User(db.Model):  
    __tablename__ = "users"
    id_user = db.Column(Integer, primary_key=True)
    name_user = db.Column(VARCHAR(45))
    sername_user = db.Column(VARCHAR(45))
    

class Worker (db.Model):
    __tablename__ = "workers"
    id_worker = db.Column(Integer, primary_key=True)
    name_worker = db.Column(VARCHAR(45))
    sername_worker = db.Column(VARCHAR(45))
    salary_worker = db.Column(Integer)


db.init_app(app)

#-------------------------Routers--------------------------------------------------
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api')
def home():
    return render_template("home.html")


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []

    for user in users:
        user_list.append({
            'id': user.id_user,
            'name': user.name_user,
            'sername': user.sername_user
        })

    return jsonify(user_list)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    new_user = User(
        name_user=data['name'],
        sername_user=data['sername']
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201


@app.route('/workers', methods=['GET'])
def get_workers():
    workers = Worker.query.all()
    worker_list = []

    for worker in workers:
        worker_list.append({
            'id': worker.id_worker,
            'name': worker.name_worker,
            'sername': worker.sername_worker,
            'salary': worker.salary_worker
        })

    return jsonify(worker_list)

@app.route('/workers', methods=['POST'])
def create_worker():
    data = request.get_json()

    new_worker = Worker(
        name_worker=data['name'],
        sername_worker=data['sername'],
        salary_worker=data['salary']
    )

    db.session.add(new_worker)
    db.session.commit()

    return jsonify({'message': 'Worker created successfully'}), 201



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)