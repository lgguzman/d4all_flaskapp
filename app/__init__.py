from flask import Flask

app = Flask(__name__)
with app.app_context():
    # Import Flask routes
    from app import routes

    # Import Dash application
    from app.dashboard import dashboard

    app = dashboard.create_dashboard(app)


