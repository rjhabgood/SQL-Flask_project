import datetime as dt
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resource/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def welcome():
        return(
                f"Welcome to the Hawaii Climate Analysis API<br/>"
                f"Available Routes<br/>"
                f"/api/v1.0/percipitation<br/>"
                f"/api/v1.0/stations<br/>"
                f"/api/v1.0/tobs<br/>"
                f"/api/v1.0/temp/start<br/>"
                f"/api/v1.0/temp/start/end<br/>"
                f"<p>'start' and 'end' date should be in the format MMDDYYYY.</p>"
        )
@app.route("/api/v1.0/percipitation")
def percipitation():
        prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)

        percipitation= session.queary(Measurement.date, Measurement.prcp).\
            filter(Measurement. date >= prev_year).all()
        
        session.close()
        percip = { date: prcp for date, prcp in percipitation}
        
        return jsonify(precip)

if __name__ == "__main__":
        app.run(debug=True)