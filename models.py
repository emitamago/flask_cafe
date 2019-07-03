"""Data models for Flask Cafe"""


from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


bcrypt = Bcrypt()
db = SQLAlchemy()


class City(db.Model):
    """Cities for cafes."""

    __tablename__ = 'cities'

    def __repr__(self):
        city = self
        return f"<song  {city.id} {city.name} {city.state} >"
    

    code = db.Column(
        db.Text,
        primary_key=True,
    )

    name = db.Column(
        db.Text,
        nullable=False,
    )

    state = db.Column(
        db.String(2),
        nullable=False,
    )
    
    @classmethod
    def get_all_cities(cls):
        """get all cities from database, return list of turple """
        cities = cls.query.all()
        choices = [(city.code, city.name) for city in cities]
        return choices

    
class Cafe(db.Model):
    """Cafe information."""

    __tablename__ = 'cafes'

    def __repr__(self):
        return f'<Cafe id={self.id} name="{self.name}">'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    name = db.Column(
        db.Text,
        nullable=False,
    )

    description = db.Column(
        db.Text,
        nullable=False,
    )

    url = db.Column(
        db.Text,
        nullable=False,
    )

    address = db.Column(
        db.Text,
        nullable=False,
    )

    city_code = db.Column(
        db.Text,
        db.ForeignKey('cities.code'),
        nullable=False,
    )

    image_url = db.Column(
        db.Text,
        nullable=False,
        default="/static/images/default-cafe.jpg",
    )

    city = db.relationship("City", backref='cafes')

    
    

    def get_city_state(self):
        """Return 'city, state' for cafe."""

        city = self.city
        return f'{city.name}, {city.state}'


class User():
    """ Model for users"""
    __tablename__ = 'users'

    def __repr__(self):
        return f'<User id={self.id} username="{self.username}">'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    
    username =  db.Column(
        db.String,
        nullable=False,
        unique=True
    )
    
    admin = db.Column(
        db.Boolean,
        nullable=False,
        default=False,
    )

    email = db.Column(
        db.String,
        nullable=False,
        unique=True
    )

    first_name = db.Column(
        db.String,
        nullable=False,
    )

    last_name = db.Column(
        db.String,
        nullable=False,
    )
    
    description = db.Column(
        db.Text,
        nullable=True
    )
   
    image_url = db.Column(
       db.String,
       nullable=False,
       default= '/static/images/default-pic.png'
   )
    
    hashed_password = db.Column(
        db.String,
        nullable=False,
        unique=True
    )
    
    @classmethod
    def register_user(username,
                                admin,
                                email,
                                first_name,
                                last_name,
                                description,
                                image_url,
                                password,
                                ):
        """ """
        hashed_password = bcrypt.generate_password_hash(password)



def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
