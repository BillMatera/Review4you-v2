"""
Routes and views for the flask application.
First import python packages from virtual enviorment

"""
from   flask       import Flask, render_template, Blueprint, Markup
from   datetime    import datetime
from   flask       import render_template
from   flask_googlemaps import Map
from   yelpapi     import YelpAPI
import argparse
from   pprint      import pprint
import requests
from   dict_digger import dig
from   flask       import request , url_for, redirect  
from   flask       import session
from   flask_googlemaps import GoogleMaps
'''-----------------------------------------------------------------------------------------------------------------'''

app = Flask(__name__)
'''Initiate google maps api with api key'''
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
