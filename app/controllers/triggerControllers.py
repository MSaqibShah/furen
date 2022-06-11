from sqlalchemy.orm import session
from app.models.rent import Rent
from app.models.payment import Payment
from app.models.product import Product
from app.controllers import paymentController as payc
from app import db

def createMonthlyPaymentTrigger(rid):
    r = Rent.query.get(rid)
    uid = r.uid
    eid = r.eid
    rid = r.rid
    pid = r.pid
    product = Product.query.get(pid)
    paymentamount = product.price
    check = r.checkPaymentTime()
    if check == True:
        payc.createPayment(uid, eid,rid, paymentamount,'p')
    
