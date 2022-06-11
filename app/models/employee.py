from app import app, db,bcrypt
import datetime
from sqlalchemy.sql.functions import current_date,now

class Employee(db.Model):
    __tablename__ ='employee'
    eid = db.Column(db.Integer(), primary_key=True)
    ename = db.Column(db.String(30) )
    enumber = db.Column(db.String(15))
    eemail = db.Column(db.String(240))
    etype = db.Column(db.String(20))
    esalary = db.Column(db.Integer())
    esup = db.Column(db.Integer(), db.ForeignKey('employee.eid', ondelete='SET NULL'),nullable=True)
    _password = db.Column(db.String(255))

    def __repr__(self):
        return f'<Employee eid: {self.eid}, name: {self.ename}>'
    
    def __init__(self,ename,enumber,eemail, password,etype,esalary,eid=None,esup=None):
        if eid != None:
            self.eid = eid
        self.ename = ename 
        self.enumber = enumber
        self.eemail = eemail
        self.etype = etype
        self.esalary = esalary
        if esup != None:
            self.esup =esup
        
        self._password = bcrypt.generate_password_hash(password)

    def setPassword(self,plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)
        
    def checkPassword(self, plaintext):
        return bcrypt.generate_password_hash(plaintext)