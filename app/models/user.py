from app import db, bcrypt 
import datetime
from sqlalchemy.sql.functions import current_date,now
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):
    __tablename__ ='user'
    uid = db.Column(db.Integer(), primary_key=True)
    uname = db.Column(db.String(30) )
    uemail = db.Column(db.String(240) )
    unumber = db.Column(db.String(15))
    uaddress = db.Column(db.String(250))
    ucity = db.Column(db.String(250))
    ustates = db.Column(db.String(250))
    upin = db.Column(db.Integer())
    _password = db.Column(db.String(255))

    def __repr__(self):
        return f'<User uid: {self.uid}, name: {self.uname}>'
    
    def __init__(self, uname, uemail, password,upin, unumber='', uaddress='', ucity='', ustates='',uid=None):
        # print(bcrypt.generate_password_hash(password))
        # print(len(bcrypt.generate_password_hash(password)))
        # print(type(bcrypt.generate_password_hash(password)))

        if uid != None:
            self.uid = uid
        self.uname = uname
        self.uemail = uemail
        self.unumber = unumber
        self.uaddress = uaddress
        self.ucity = ucity
        self.ustates = ustates
        self.upin = upin
        self._password = bcrypt.generate_password_hash(password)

    # @hybrid_property
    # def password(self):
    #     return self.password

    def setPassword(self,plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)
    def checkPassword(self, plaintext):
        return bcrypt.generate_password_hash(plaintext)

