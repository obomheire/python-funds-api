from . import db
from sqlalchemy.sql import func

class Users(db.Model):
    __tablename__= 'Users'
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String(100), nullable = False)
    lastName = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(250), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    createdAt = db.Column(db.DateTime(timezone = True), server_default = func.now())
    funds = db.relationship('Funds', backref = 'Users')

    def __repr__(self):
        return f'<User {self.id} {self.firstName}>'


class Funds(db.Model):
    __tablename__ = "Funds"
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Numeric(10, 2), nullable = False)
    userId = db.Column(db.Integer, db.ForeignKey('Users.id'))
    createdAt = db.Column(db.DateTime(timezone = True), server_default = func.now())

    @property
    def serialize(self):

        return {
            'id': self.id,
            'amount': self.amount,
            'CreatedAt': self.createdAt
        }
