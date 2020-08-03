# d4all_flaskapp
The backend and Front end is managed by Dash framework, encapsulated in a general server python application (Flask).

## Repository
[Github]( https://github.com/lgguzman/d4all_flaskapp)
##Architecture
The general architecture is composed by some services: 
Front-end: We use Dash Framework to generate the interactive web-ui with Python . 
Back-end: The Dash App is encapsulated in a Flask Server (The main idea is to use a general server, which lets us scale the project).
Database: RDS (POSTGRESQL) only accessible by EC2

### Development environment
#### Dependencies
scikit-learn
flask
dash
pandas
numpy
sqlalchemy

#### Enironment variables
FLASK_APP=data4all.py
ENV_PATH=app/
DB_PASSWORD=**The db password**


#### File structure
- app
    - \_\_init__.py: code for serving application
    - routes: contains example for general api using flask  
    - assets: images
    - data: csv and json files
    - libpage
        - content.py: general components
        - map_cluster.py: map component layout
        - modal_info.py: modal component to show information
        - ui_inputs: inputs components
    - dashboard
        -utils: utilities like Database Connection, reading files, etc
        -locator_dashboard: handle information and callbacks between ui and cluster algorithm
    
- data4all.py: the main file (you can use flask run or gunicorn)


### Production 
The Web application is deployed in [AWS](http://ec2-3-16-168-18.us-east-2.compute.amazonaws.com/). In addition for the general configuration, production environment needs some configuration:
Web Serving and Reverse Proxying: We use Nginx for web serving and load balancing.
Wsgi Server: We use Gunicorn in order to handle simultaneous requests. The number of workers is configured to four.
