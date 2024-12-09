from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, login_required, current_user, logout_user
from .models import User, Post
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

main_bp = Blueprint('main', __name__)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('login.html')

@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        foto = request.form['foto']
        bio = request.form['bio']
        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password, foto=foto, bio=bio)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('cadastro.html')

@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        posts = Post.query.order_by(Post.timestamp.desc()).limit(5).all()
        return render_template('index.html', posts=posts)
    return render_template('index.html')

@main_bp.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        body = request.form['body']
        new_post = Post(body=body, author=current_user)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('post.html')
