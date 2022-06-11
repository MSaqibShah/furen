from app import app, db
import datetime
from sqlalchemy.sql.functions import current_date,now


class Rent(db.Model):
    __tablename__ ='rent'
    rid = db.Column(db.Integer(), primary_key=True)
    rstart = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # rperiod = db.Column(db.Integer)
    rend = db.Column(db.DateTime) 
    rstatus = db.Column(db.String(3)) 
    pid = db.Column(db.Integer(), db.ForeignKey('product.pid',ondelete='SET NULL'))
    eid = db.Column(db.Integer(), db.ForeignKey('employee.eid',ondelete='SET NULL'))
    uid = db.Column(db.Integer(), db.ForeignKey('user.uid',ondelete='CASCADE'))

    def __repr__(self):
        return f'<Rent rid: {self.rid}, start_date: {self.rstart}>'
        # <Rent rid: 10, start_date: 2014-11-20, rperiod: 4>
    
    def __init__(self,rstart,rend,pid,uid,eid, rstatus='PP',rid=None):
        if rid!=None:
            self.rid = rid
        self.rstart = rstart
        self.rend = rend
        self.pid = pid
        self.uid = uid
        self.eid = eid
        self.rstatus = rstatus

    def checkPaymentTime(self):
        r = False #Payment is not due
        start = self.rstart
        start_day = int(start.strftime('%d'))
        # start_day = 5 
        current_date = datetime.datetime.utcnow
        today = int(current_date.strftime('%d'))
        # today = 5
        if(today - start_day) == 0:
            r =  True #Payment is due
        return r   

    # def calcDateEnd(self):
    #     self.rend = self.rstart + datetime.timedelta(weeks=self.rperiod*4)

