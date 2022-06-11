from app import app, db
import datetime
from sqlalchemy.sql.functions import current_date,now

# from app.views.loginviews import payment

        
class Payment(db.Model):
    __tablename__ ='payment'
    paymentid = db.Column(db.Integer(), primary_key=True)
    paymentdate = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    paymentamount = db.Column(db.Integer())
    # paymentstatus = db.Column(db.String(1))
    
    uid = db.Column(db.Integer(), db.ForeignKey('user.uid',ondelete='CASCADE'))
    eid = db.Column(db.Integer(), db.ForeignKey('employee.eid',ondelete='SET NULL'))
    rid = db.Column(db.Integer(), db.ForeignKey('rent.rid',ondelete='SET NULL'))
    def __repr__(self):
        return f'<Payment paymentid: {self.paymentid}, uid: {self.uid},rid: {self.rid}, date: {self.paymentdate}>'
    
    def __init__(self, uid, eid,rid, paymentamount,paymentid=None):
        if paymentid!=None:
            self.paymentid = paymentid
        self.uid = uid
        self.eid = eid
        self.rid = rid
        self.paymentamount = paymentamount
        # self.paymentdate = datetime.now()
