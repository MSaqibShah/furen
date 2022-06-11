from app import app, db
import datetime
# from sqlalchemy.sql.functions import now

class Product(db.Model):
    __tablename__ ='product'
    pid = db.Column(db.Integer(), primary_key=True)
    pname = db.Column(db.String(50) )
    pdesc = db.Column(db.String(500))
    ptype = db.Column(db.String(20))
    price = db.Column(db.Integer() )

    def __repr__(self):
        return f'<Product pid: {self.pid}, name: {self.pname}>'
    def __init__(self, pname, pdesc, ptype, price,pid=None):
        if pid != None:
            self.pid = pid
        self.pname = pname
        self.pdesc = pdesc
        self.ptype = ptype
        self.price = price
