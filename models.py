import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, Numeric, DateTime
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base


def create_classes(db):
    class Pet(db.Model):
        __tablename__ = 'pets'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64))
        lat = db.Column(db.Float)
        lon = db.Column(db.Float)

    class movies_and_ratings(db.Model):
        __tablename__ = 'movies_and_ratings'
        imdb_title_id = db.Column(db.String(), primary_key=True)
        weighted_average_vote = db.Column(db.Float())
        total_votes = db.Column(db.Integer())
        mean_vote  = db.Column(db.Float())
        median_vote = db.Column(db.Integer())
        votes_10 = db.Column(db.Integer())
        votes_9 = db.Column(db.Integer())
        votes_8 = db.Column(db.Integer())
        votes_7 = db.Column(db.Integer())
        votes_6 = db.Column(db.Integer())
        votes_5 = db.Column(db.Integer())
        votes_4 = db.Column(db.Integer())
        votes_3 = db.Column(db.Integer())
        votes_2 = db.Column(db.Integer())
        votes_1 = db.Column(db.Integer())
        allgenders_0age_avg_vote = db.Column(db.Float())
        allgenders_0age_vote = db.Column(db.Integer())
        allgenders_18age_avg_vote = db.Column(db.Float())
        allgenders_18age_votes = db.Column(db.Integer())
        allgenders_30age_avg_vote = db.Column(db.Float())
        allgenders_30age_votes = db.Column(db.Integer())
        allgenders_45age_avg_vote = db.Column(db.Float())
        allgenders_45age_votes = db.Column(db.Integer())
        males_allages_avg_vote = db.Column(db.Float())
        males_allages_votes = db.Column(db.Integer())
        males_0age_avg_vote = db.Column(db.Float())
        males_0age_votes = db.Column(db.Integer())
        males_18age_avg_vote = db.Column(db.Float())
        males_18age_votes = db.Column(db.Integer())
        males_30age_avg_vote = db.Column(db.Float())
        males_30age_votes = db.Column(db.Integer())
        males_45age_avg_vote = db.Column(db.Float())
        males_45age_votes = db.Column(db.Integer())
        females_allages_avg_vote = db.Column(db.Float())
        females_allages_votes = db.Column(db.Integer())
        females_0age_avg_vote = db.Column(db.Float())
        females_0age_votes = db.Column(db.Integer())
        females_18age_avg_vote = db.Column(db.Float())
        females_18age_votes = db.Column(db.Integer())
        females_30age_avg_vote = db.Column(db.Float())
        females_30age_votes = db.Column(db.Integer())
        females_45age_avg_vote = db.Column(db.Float())
        females_45age_votes = db.Column(db.Integer())
        top1000_voters_rating = db.Column(db.Float())
        top1000_voters_votes  = db.Column(db.Integer())
        us_voters_rating = db.Column(db.Float())
        us_voters_votes = db.Column(db.Integer())
        non_us_voters_rating = db.Column(db.Float())
        non_us_voters_votes  = db.Column(db.Integer())
        title = db.Column(db.String())
        year = db.Column(db.Integer())
        genre = db.Column(db.String())
        duration = db.Column(db.Integer())
        country = db.Column(db.String())
        language = db.Column(db.String())
        director = db.Column(db.String())
        writer = db.Column(db.String())
        production_company = db.Column(db.String())
        actors = db.Column(db.String())
        description = db.Column(db.String())
        avg_vote = db.Column(db.Float())
        votes = db.Column(db.Integer())
        reviews_from_users = db.Column(db.Integer())
        reviews_from_critics = db.Column(db.Integer())
        month_published = db.Column(db.Integer())
        genre_2 = db.Column(db.String())
        genre_3 = db.Column(db.String())

    class names_data(Base):
        __tablename__ = 'names_data'
        imdb_title_id = db.Column(db.String(), primary_key=True)
        name = db.Column(db.String())
        bio = db.Column(db.String())
        spouses = db.Column(db.Integer())
        divorces = db.Column(db.Integer())
        spouces_with_childern = db.Column(db.Integer())
        childern = db.Column(db.Integer())

    class tp_data(db.Model):
        __tablename__ = 'tp_data'
        imdb_title_id = db.Column(db.String(), primary_key=True)
        ordering = db.Column(db.Integer())
        imdb_name_id = db.Column(db.String())
        category = db.Column(db.String())

    class ratings(db.Model):
        __tablename__ = 'ratings'
        movie_id = db.Column(db.Integer(), primary_key=True)
        userId = db.Column(db.Integer())
        rating = db.Column(db.Integer())
        timestamp = db.Column(db.Integer())

    class ratings(db.Model):
        __tablename__ = 'ratings'
        movie_id = db.Column(db.Integer(), primary_key=True)
        title = db.Column(db.String())
        genres = db.Column(db.String())
        def __repr__(self):
            return '<Pet %r>' % (self.name)
    return Pet
