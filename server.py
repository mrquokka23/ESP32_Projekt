from flask import Flask, render_template, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Measurements(db.Model):
    idx = db.Column(db.Integer, primary_key=True)	
    MeasurementDate = db.Column(db.DateTime, nullable=False)
    MeasurementData = db.Column(db.String(), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/", methods=['GET', 'POST'])
def hello():
    data = Measurements.query.all()
    labels = []
    i = 0
    for row in data:
        if len(data) < 2000:
            labels.append(row.MeasurementDate.strftime("%m/%d/%Y, %H:%M"))
        elif i % 10 == 0 and i < 2000:
            labels.append(row.MeasurementDate.strftime("%m/%d/%Y, %H:%M"))
    values = [row.MeasurementData for row in data]
    
    return render_template('index.html', labels=labels, values=values)

class DataApi(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        gettableinx = Measurements.query.all()
        if len(gettableinx) == 0:
            idx = 0
        else:
            idx = gettableinx[-1].idx + 1
        measurement = Measurements(idx=idx, MeasurementDate=datetime.datetime.now(), MeasurementData=data['moisture'])
        db.session.add(measurement)
        db.session.commit()

api.add_resource(DataApi, '/data')