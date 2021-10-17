
from sqlalchemy.ext.declarative import declarative_base
Base= declarative_base()

def create_classes(db):
    class Test(db.Model):
        __tablename__ = 'test'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50))        
        print ("Model Name ",name)
        def __repr__(self):
            return '<Test %r>' % (self.name)
    return Test

def create_rating_class(db):
    class Ratings(db.Model):
        __tablename__ = 'ratings'

        movie_id = db.Column(db.Integer(), primary_key=True)
        userId = db.Column(db.Integer())
        rating = db.Column(db.Integer())
    
        def __repr__(self):
            return '<Ratings %r>' % (self.name)
    return Ratings