from flask import Flask
from flask import render_template
from datetime import datetime
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)
GoogleMaps(app, key="AIzaSyC-IaoIh43rhygYYBAfbhHJuuzbZWKkhII")


@app.route('/')
def index():
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year)
        
@app.route('/results')
def results(): 
    mymap = Map(
        identifier="view-side",
        varname='mymap',
        lat=40.1940632,
        lng=-74.1592278,
        zoom=11,
        style="height:500px;width:1000px;margin:0;"
    )
    return render_template(
        'results.html',
        mymap=mymap
    )

if __name__ == "__main__":
    app.run()
