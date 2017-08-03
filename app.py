
from flask import Flask
from flask import render_template
from datetime import datetime
from flask_googlemaps import GoogleMaps

app = Flask(__name__)
GoogleMaps(app, key="AIzaSyC-IaoIh43rhygYYBAfbhHJuuzbZWKkhII")

@app.route('/')
def index():
	return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
    
if __name__ == "__main__":
	app.run()