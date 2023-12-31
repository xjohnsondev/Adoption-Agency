from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, 
                          default="data:image/jpeg;base64,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")
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)