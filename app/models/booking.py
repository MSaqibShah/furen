from app import db
import datetime
from sqlalchemy.sql.functions import current_date,now

class Booking(db.Model):
    __tablename__ ='booking'
    bid = db.Column(db.Integer(),primary_key=True)
    uid = db.Column(db.Integer(), db.ForeignKey('user.uid',ondelete='CASCADE'), primary_key=True)
    pid = db.Column(db.Integer(), db.ForeignKey('product.pid', ondelete='CASCADE'), primary_key=True)

    bstatus = db.Column(db.String(10))
    bdate = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    deliverydate = db.Column(db.DateTime)
    quantity = db.Column(db.Integer())


    def __repr__(self):
        return f'<Booking bid: {self.bid}, uid: {self.uid}, pid:{self.pid} status: {self.bstatus}>'
    
    def __init__(self,bstatus,uid,pid,quantity,bid=None,deliverydate=None):
        if bid != None:    
            self.bid = bid
        self.bstatus = bstatus
        # self.bdate = datetime.now()
        self.uid = uid
        self.pid = pid
        self.deliverydate = deliverydate
        self.quantity = quantity

# db.create_all()