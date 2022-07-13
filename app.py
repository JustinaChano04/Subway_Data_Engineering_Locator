from ensurepip import bootstrap
from re import L
from flask import Flask, render_template
from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


app = Flask(__name__)

# db_name = '/Users/justinchan/Desktop/devrep/summer-2022/subways.db'
db_name = 'subways.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class subways(db.Model):
    __tablename__ = 'subway'
    title = db.Column(db.String, primary_key=True)
    address_1 = db.Column(db.String)
    open_hours = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    postal_code = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)


# @app.route('/')
# def testdb():
#     try:
#         db.session.query(text('1')).from_statement(text('SELECT 1')).all()
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         # e holds description of the error
#         error_text = "<p>The error:<br>" + str(e) + "</p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text


@app.route('/query/<state>')
def ak_subway(state):
    subway = subways.query.filter_by(state=state).all()
    return render_template('list.html', subway=subway, state=state)

if __name__ == '__main__':
    boostrap = Bootstrap(app)
    app.run(debug=True)