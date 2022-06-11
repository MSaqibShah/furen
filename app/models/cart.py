from app import db
import datetime
from sqlalchemy.sql.functions import current_date,now

class Cart(db.Model):
    __tablename__ ='cart'
    uid = db.Column(db.Integer(), db.ForeignKey('user.uid',ondelete='CASCADE'), primary_key=True)
    pid = db.Column(db.Integer(),  db.ForeignKey('product.pid', ondelete='CASCADE'), primary_key=True)
    quantity = db.Column(db.Integer())
    
    def __repr__(self):
        return f'<Cart uid: {self.uid} pid: {self.pid}>'
    
    def __init__(self,uid,pid, quantity):
        self.uid = uid
        self.pid = pid
        self.quantity = quantity

