from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

import psycopg2




def get_db(app):

    try:
        app=app
        engine = create_engine('postgresql+psycopg2://postgres:mmb252974@127.0.0.1:5432/tiger_report_db')
        app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mmb252974@localhost:5432/tiger_report_db'
        db = SQLAlchemy(app)

    except:
        app.config['SQLALCHEMY_DATABASE_URI'] = create_engine('sqlite:////ressources/data.db')
        db = SQLAlchemy(app)
    return db