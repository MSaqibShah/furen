from sqlalchemy.orm import session
from app.models.rent import Rent
from app import db

def createRent(rstart,rend,pid,uid,eid,rstatus='PP',rid=None):
    # rend,pid,uid,eid,rid
    if (rid != None):
        r  = Rent(rstart,rend,pid,uid,eid,rstatus,rid)
    else:    
        r  = Rent(rstart,rend,pid,uid,eid,rstatus)
    db.session.add(r)
    db.session.commit()
    print("------------------------------------")
    print(r, 'created!')
    print("------------------------------------")

     
def updateRent(rid,rstart=None,rend=None,pid=None,uid=None, eid=None,rstatus=None):
    r  = Rent.query.get(rid) 
    # rend,pid,uid,eid

    r.rstart = rstart or r.rstart
    r.rend = rend or r.rend
    r.pid = pid or r.pid
    r.uid = uid or r.uid  
    r.eid = eid or r.eid  
    r.rstatus = rstatus or r.rstatus  
    
    db.session.add(r)
    db.session.commit()
    print("------------------------------------")
    print(r, 'updated!')
    print("------------------------------------")


def deleteRent(rid):
    r = Rent.query.get(rid)
    db.session.delete(r)
    db.session.commit()
    print("------------------------------------")
    print(r, 'deleted!')
    print("------------------------------------")

def getRent(rid):
    t = f"SELECT * FROM RENT WHERE rid ='{rid}'"
    conn = db.session.connection()
    r = conn.execute(t)
    r = r.first()
    r = r._asdict()
    return r

def getAllRent(uid):
    t = f"SELECT * FROM RENT WHERE uid ='{uid}'"
    conn = db.session.connection()
    result = conn.execute(t)
    r = []
    for row in result:
        r.append(row._asdict())
    return r