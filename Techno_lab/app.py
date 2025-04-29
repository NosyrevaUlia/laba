from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, VARCHAR, Boolean, ForeignKey, TIMESTAMP, String
from dotenv import load_dotenv
import os
from datetime import timedelta

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'super-secret-key')

# Конфигурация базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'mysql+mysqlconnector://root:tYHjhgfT67GVbj24@localhost:3306/laba')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Модели
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

# Маршруты для главной страницы и API
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api')
def api():
    return render_template("api.html")

# Маршруты для работы с клиентами (User)
@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template("users.html", users=all_users)

@app.route('/users/add', methods=['POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        sername = request.form['sername']
        
        new_user = User(name_user=name, sername_user=sername)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Клиент успешно добавлен')
        return redirect(url_for('users'))

@app.route('/users/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    user = User.query.get_or_404(id)
    
    if request.method == 'POST':
        user.name_user = request.form['name']
        user.sername_user = request.form['sername']
        db.session.commit()
        
        flash('Данные клиента обновлены')
        return redirect(url_for('users'))
    
    return render_template("update_user.html", user=user)

@app.route('/users/delete/<int:id>')
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    
    flash('Клиент удален')
    return redirect(url_for('users'))

# Маршруты для работы с работниками (Worker)
@app.route('/workers')
def workers():
    all_workers = Worker.query.all()
    return render_template("workers.html", workers=all_workers)

@app.route('/workers/add', methods=['POST'])
def add_worker():
    if request.method == 'POST':
        name = request.form['name']
        sername = request.form['sername']
        salary = request.form['salary']
        
        new_worker = Worker(name_worker=name, sername_worker=sername, salary_worker=salary)
        db.session.add(new_worker)
        db.session.commit()
        
        flash('Работник успешно добавлен')
        return redirect(url_for('workers'))

@app.route('/workers/update/<int:id>', methods=['GET', 'POST'])
def update_worker(id):
    worker = Worker.query.get_or_404(id)
    
    if request.method == 'POST':
        worker.name_worker = request.form['name']
        worker.sername_worker = request.form['sername']
        worker.salary_worker = request.form['salary']
        db.session.commit()
        
        flash('Данные работника обновлены')
        return redirect(url_for('workers'))
    
    return render_template("update_worker.html", worker=worker)

@app.route('/workers/delete/<int:id>')
def delete_worker(id):
    worker = Worker.query.get_or_404(id)
    db.session.delete(worker)
    db.session.commit()
    
    flash('Работник удален')
    return redirect(url_for('workers'))

# API endpoints
@app.route('/api/users', methods=['GET'])
def api_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {
            'id': user.id_user,
            'name': user.name_user,
            'sername': user.sername_user
        }
        output.append(user_data)
    return jsonify({'users': output})

@app.route('/api/workers', methods=['GET'])
def api_workers():
    workers = Worker.query.all()
    output = []
    for worker in workers:
        worker_data = {
            'id': worker.id_worker,
            'name': worker.name_worker,
            'sername': worker.sername_worker,
            'salary': worker.salary_worker
        }
        output.append(worker_data)
    return jsonify({'workers': output})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создает таблицы, если они не существуют
    app.run(host='0.0.0.0', port=5000, debug=True)