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
from   flask       import request , url_for, redirect , flash 
from   flask       import session
from   flask_googlemaps import GoogleMaps
import json
'''-----------------------------------------------------------------------------------------------------------------'''

app = Flask(__name__)
'''Initiate google maps api with api key'''
# GoogleMaps(app, key="AIzaSyC-IaoIh43rhygYYBAfbhHJuuzbZWKkhII")
# AIzaSyATSFUHDfiDzp025aBPEHJbJjbCYhi2CFo
GoogleMaps(app, key="AIzaSyATSFUHDfiDzp025aBPEHJbJjbCYhi2CFo")

'''Authorization values client_id and api_key provided by yelp'''
client_id = 'ULxccklBxmMHp6URHv4khw'
api_key = 'LBycV4T66AgIxeNuMZlq3lqKCV3eH_T2W4QDR8f0fIYK3HGkxq8_mpvBoCF5aaLuQTL_-yDgEJdgdl_gHQ7PyvdyPJ6Cz2_vVbxRJbNTZhNKTpdCx8tPl5JxaaNWXnYx'

'''Yelp fusion API endpoint'''
url = 'https://api.yelp.com/v3/businesses/search'
                

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method =="POST":        
         zipcode = request.form['zip']
         searchTerm = request.form['searchTerm']
         pprint(zipcode)
         session['zipcode'] = zipcode
         session['searchTerm'] = searchTerm
         return redirect(url_for('results'))
    return render_template(
        'index.html')
        
        
@app.route('/results')
def results(): 
    headers = {'Authorization': 'bearer %s' % api_key}
    params = {'location': session.get('zipcode'),
          'term': session.get('searchTerm'),
          'pricing_filter': '1, 2',
          'sort_by': 'rating'
         }
    '''send GET http request with all authorization info to obtain search reults based on params.'''
    resp = requests.get(url=url, params=params, headers=headers)
    if resp.status_code == 200 or resp.status_code == 302:
        '''JSONify response for use in logic'''
        response = resp.json() 
        if response.get('total') > 0:
            print(json.dumps(response, indent=4))
            businesses = response.get('businesses')
            mymap = Map(
                    identifier="view-side",
                    varname = 'mymap',
                    lat= dig(businesses[0], 'coordinates', 'latitude'),
                    lng= dig(businesses[0], 'coordinates', 'longitude'),
                    zoom = 11,
                    style= "height:500px;width:auto;margin:0;"
                )  
            userMessage = 'Click the Markers to see their Info Boxes pop up with their Data'
            for places in businesses:  
                '''store needed info for each markers infobox & turn each into string type'''
                nameString = str(dig(places,'display_phone'))
                numString = "<h2>"+dig(places,'name')+"</h2>"
                str(numString)
                imgString = "<img src='"+dig(places,'image_url')+"'width='300px' height='300px'>"
                str(imgString)
                x = {'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                        'lat' : (dig(places, 'coordinates','latitude')),
                        'lng' : (dig(places, 'coordinates','longitude')),
                        'infobox' :( nameString  +  
                                    numString  +
                                    imgString                              
                        )}         
                mymap.markers.append(x)
            return render_template('results.html', mymap=mymap, marks = mymap.markers, userMessage=userMessage)
        else:
            # handle error
            mymap = Map(
                    identifier="view-side",
                    varname = 'mymap',
                    lat= 37.0902,
                    lng= -95.7129,
                    zoom = 4,
                    style= "height:500px;width:auto;margin:0;"
                )
            userMessage = 'Apologies, there were no results returned by Yelp. Please check your search parameters and try again'
            return render_template('results.html', mymap=mymap, marks=mymap.markers, userMessage=userMessage)
    else:
        # handle error
        mymap = Map(
                    identifier="view-side",
                    varname = 'mymap',
                    lat= 37.0902,
                    lng= -95.7129,
                    zoom = 4,
                    style= "height:500px;width:auto;margin:0;"
                ) 
        userMessage = 'Apologies, there was an issue connecting to yelp. Please check your search parameters try again'
        return render_template('results.html', mymap=mymap, marks=mymap.markers , userMessage=userMessage)


'''secret key for sessions package'''    
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run()

