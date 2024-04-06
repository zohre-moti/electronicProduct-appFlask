from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # کلید مخفی برای امنیتی

# تنظیمات پایگاه داده
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes
