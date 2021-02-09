from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)
mail = Mail(app)

csrf = CSRFProtect(app)


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')
    email = db.Column(db.String(255), nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime())


db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)


@app.route('/')
@login_required
def home():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'method not allowed'
    return render_template('login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if '_user_id' in session:
        return 'wla wla wla'
    if request.method == 'POST':
        return 'method not allowed on register route'
    return render_template('register.html')


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
