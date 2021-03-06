from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
with app.app_context():
    # Import Flask routes
    from app import routes

    # Import Dash application
    from app.dashboard import locator_dashboard

    app = locator_dashboard.create_dashboard(app)


