from sqlalchemy.orm import session
from app.models.product import Product
from app import db

def createProduct(pname, pdesc, ptype, price,pid=None):
    if (pid != None):
        p  = Product(pname, pdesc, ptype, price, pid)
    else:    
        p  = Product(pname, pdesc, ptype, price)
    db.session.add(p)
    db.session.commit()
    print(p, 'created!')
     
def updateProduct(pid, pname=None, pdesc=None, ptype=None, price=None):
    p  = Product.query.get(pid) 

    p.pname = pname or p.pname
    p.pdesc = pdesc or p.pdesc                  
    p.ptype = ptype or p.ptype
    p.price = price or p.price

    db.session.add(p)
    db.session.commit()
    print(p, 'updated!')

def deleteProduct(pid):
    p = Product.query.get(pid)
    db.session.delete(p)
    db.session.commit()
    print(p, 'deleted!')

def getProducts():
    q = 'SELECT * from product'
    conn = db.session.connection()
    result = conn.execute(q)
    r = result.all()
    return r
def getProduct(pid):
    q = f'SELECT * from product where pid = {pid}'
    conn = db.session.connection()
    result = conn.execute(q)
    r = result.first()
    return r
