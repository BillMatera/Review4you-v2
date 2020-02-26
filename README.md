#  Review4You-

Review4You! website - Flask Micro Framework - Python  3.6


##  Pre-requisites

1. Install python 3
  - Can use homebrew for this with the command : `brew install python3`
  - In terminal try typing `python3` and press enter 
  - if python3 is not recongized, try linking to python3 by running `brew link python3` in terminal
  - if that gives an error, try unlinking python2 first with command `brew unlink python@2` , then run `brew link python3` 

2. Once python3 is set up , after pulling the repo down for the first time, need to download dependencies locally
  - The dependencies are declared in the requirments.txt at the root of the project
  - To download these locally , run `pip3 install -r requirements.txt` at the root of the project


###  Serving Development Code

  - run `python3 app.py`

    Serves the development code to localhost server


###  Languages and Tool

  - Python 3.6 with built in pip3 

  - Flask micro-framework

  - `flask_googlemaps` package for google map on results page

  - Yelp Fusion API - business search endpoint : `api.yelp.com/v3/businesses/search`
