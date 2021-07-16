"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


default_image = 'https://photolibrary.usap.gov/Tools/DrawImage.aspx?filename=emperor-penguin-noble.jpg'


class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                     nullable=False)
    photo_url = db.Column(db.Text, 
                    nullable=False, 
                    default=default_image)
    age = db.Column(db.Text, 
                    nullable=False)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                        default=True)
    
    
    
    # = db.relationship('Post', backref='user')

    def __repr__(self):
        u = self
        return f"<Pet{u.id} {u.name} {u.species} {u.age}>"