from sqlalchemy.sql import func

from . import db


class Funds(db.Model):
    __tablename__ = "Funds"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey("Users.id"))
    createdAt = db.Column(db.DateTime(timezone=True), server_default=func.now())

    @property
    def serialize(self):

        return {"id": self.id, "amount": self.amount, "CreatedAt": self.createdAt}
