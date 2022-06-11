import re
from sqlalchemy.orm import session
from app.models.booking import Booking
from app import db

def createBooking(bstatus,uid,pid,quantity,bid=None,deliverydate=None):
    pb = getBookings(uid,pid)
    
    bid =0 
    for row in pb:
        bid +=1
    bid+=1
    print(bid)
    if deliverydate == None:
        b  = Booking(bstatus,uid,pid,quantity,bid)
    else:
        b  = Booking(bstatus,uid,pid,quantity,bid,deliverydate)
    

    db.session.add(b)
    db.session.commit()
    print("------------------------------------")
    print(b, 'created!')
    print("------------------------------------")

     
def updateBooking(bid,uid,pid,quantity=None, bstatus=None,deliverydate=None):
    
    b  = Booking.query.get((bid,uid,pid)) 

    b.bstatus = bstatus or b.bstatus
    b.deliverydate = deliverydate or b.deliverydate
    b.quantity = quantity or b.quantity
    
    
    db.session.add(b)
    db.session.commit()
    print("------------------------------------")
    print(b, 'updated!')
    print("------------------------------------")


def deleteBooking(bid,uid,pid):
    b = Booking.query.get((bid,uid,pid))
    db.session.delete(b)
    db.session.commit()
    print("------------------------------------")
    print(b, 'deleted!')
    print("------------------------------------")

def getBookings(uid,pid):
    t = f"SELECT * FROM booking WHERE uid='{uid}' AND pid='{pid}'"
    conn = db.session.connection()
    result = conn.execute(t)
    # print(result)
    return result

def getAllBookings(uid):
    t = f"SELECT * FROM booking WHERE uid='{uid}'"
    conn = db.session.connection()
    result = conn.execute(t)
    # print(result)
    return result