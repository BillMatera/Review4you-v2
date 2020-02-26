#  Review4You-

Review4You! website - Flask Micro Framework - Python  3.6



###  Pre-requisites

1. Install python 3 :
    - Can use homebrew for this with the command : `brew install python3`
    - In terminal try typing `python3` and press enter 
    - if python3 is not recongized, try linking to python3 by running `brew link python3` in terminal
    - if that gives an error, try unlinking python2 first with command `brew unlink python@2` , then run `brew link python3` 


2. Once python3 is set up , after pulling the repo down for the first time, need to download dependencies locally
    - The dependencies are declared in the requirments.txt at the root of the project
    - To download these locally , run `pip3 install -r requirements.txt` at the root of the project


3. For deploying to Heroku :
    - Need to create an account on Heroku , then create an app through the dashboard
    - Then download the Heroku CLI, run command `brew tap heroku/brew && brew install heroku`
    - Now if no local git repo has been created run `git init` , if one has been created already skip this step
    - Run `heroku git:remote -a (app-name)` where (app-name) is the name you gave the app in the Heorku dashboard
    - Once code is ready , push to the Heroku remote (see the "Serving Production Code" step below)



###  Serving Development Code

  - run `python3 app.py`

    Serves the development code to localhost server



###  Serving Production Code

  - run `git push heroku master`

    Deploys current branch to remote heroku repo for hosting 



###  Languages and Tools

  - Python 3.6 with built in pip3 

  - Flask micro-framework

  - `flask_googlemaps` package for google map on results page

  - Yelp Fusion API - business search endpoint : `api.yelp.com/v3/businesses/search`

  - Heroku for hosting
