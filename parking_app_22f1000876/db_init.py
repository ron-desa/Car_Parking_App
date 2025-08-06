from app import create_app, db
from models.models import *

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Database Initialized")
