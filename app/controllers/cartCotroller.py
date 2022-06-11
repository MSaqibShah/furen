from sqlalchemy.orm import session
from app.models.cart import Cart
from app import db

def createEntry(uid,pid,quantity):
    c = Cart.query.get((uid,pid)) 

    if c is not None:
        print("Already Exists", c)
        quantity += c.quantity 
        c.quantity = quantity
        db.session.add(c)
        db.session.commit()
        print("------------------------------------")
        print(c, 'updated!')
        print("------------------------------------") 

    else:
        c  = Cart(uid,pid,quantity)
        db.session.add(c)
        db.session.commit()
        print("------------------------------------")
        print(c, 'created!')
        print("------------------------------------")

     
def updateEntry(uid,pid,quantity):
    c  = Cart.query.get((uid,pid)) 

    c.quantity = quantity    
    
    db.session.add(c)
    db.session.commit()
    print("------------------------------------")
    print(c, 'updated!')
    print("------------------------------------")


def deleteEntry(uid,pid):
    c = Cart.query.get((uid,pid))
    db.session.delete(c)
    db.session.commit()
    print("------------------------------------")
    print(c, 'deleted!')
    print("------------------------------------")


def getEntry(uid,pid):
    c = Cart.query.get((uid,pid))
    return c

def getEntries(uid):
    entries = Cart.query.all()
    c = []
    for e in entries:
        if e.uid == uid:
            c.append(e) 
    # print(entries)
    return c

def getCart(uid):
    entries = Cart.query.all()
    c = []
    for e in entries:
        if e.uid == uid:
            c.append(e) 
    cart ={}
    for item in c:
                pid, quatity = item.pid, item.quantity
                cart[f'{pid}']= quatity
    return cart