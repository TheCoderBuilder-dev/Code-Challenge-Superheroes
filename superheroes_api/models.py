
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

# Hero model
class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    # relationship
    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade="all, delete-orphan")

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    # relationship
    hero_powers = db.relationship('HeroPower', back_populates='power', cascade="all, delete-orphan")

    @validates('description')
    def validate_description(self, key, desc):
        if not desc or len(desc) < 20:
            raise ValueError("Description must be at least 20 characters long!")
        return desc

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    # relationships back
    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    # VALIDATE again 
    @validates('strength')
    def validate_strength(self, key, stren):
        if stren not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be either Strong, Weak or Average")
        return stren