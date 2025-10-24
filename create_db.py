from app import app, db

with app.app_context():
    db.create_all()
    print("✅ SQLite database and tables created!")
