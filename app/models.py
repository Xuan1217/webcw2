from app import db


class Dishes(db.Model):
    Cid = db.Column(db.Integer, primary_key=True)
    dish = db.Column(db.String(100), nullable=False)
    pic = db.Column(db.String(100))
    price = db.Column(db.Integer)
    inventory = db.Column(db.Integer, default=0, nullable=False)
    likeNum = db.Column(db.Integer, default=0)


class Car(db.Model):
    Aid = db.Column(db.Integer, primary_key=True)
    Uid = db.Column(db.Integer, db.ForeignKey("user.Uid"))
    Cid = db.Column(db.Integer, db.ForeignKey("dishes.Cid"))
    pic = db.Column(db.String(100))
    dish = db.Column(db.String(100))
    price = db.Column(db.Integer)
    Num = db.Column(db.Integer, default=1)


class User(db.Model):
    Uid = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(500), nullable=False)
    Password = db.Column(db.String(500), nullable=False)
    Currency = db.Column(db.Integer, default=0)






