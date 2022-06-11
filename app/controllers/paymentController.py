from sqlalchemy.orm import session
from app.models.payment import Payment
from app import db

def createPayment(uid, eid,rid, paymentamount,paymentid=None):
    # uid, eid,rid, paymentamount,paymentid=None
    if (paymentid != None):
        paymentid  = Payment(uid, eid,rid, paymentamount,paymentid,paymentstatus)
    else:    
        p  = Payment(uid, eid,rid, paymentamount,paymentstatus)
    db.session.add(p)
    db.session.commit()
    print("------------------------------------")
    print(p, 'created!')
    print("------------------------------------")

     
def updatePayment(paymentid,uid=None, eid=None,rid=None, paymentamount=None):
    p  = Payment.query.get(paymentid) 

    p.uid = uid or p.uid
    p.eid = eid or p.eid
    p.rid = rid or p.rid
    p.paymentamount = paymentamount or p.paymentamount 
    # p.paymentstatus = paymentstatus or p.paymentstatus 

    db.session.add(p)
    db.session.commit()
    print("------------------------------------")
    print(p, 'updated!')
    print("------------------------------------")


def deletePayment(paymentid):
    p = Payment.query.get(paymentid)
    db.session.delete(p)
    db.session.commit()
    print("------------------------------------")
    print(p, 'deleted!')
    print("------------------------------------")

def getAllPayments(uid):
    t = f"SELECT * FROM payment WHERE uid='{uid}'"
    conn = db.session.connection()
    result = conn.execute(t)
    # print(result)
    return result