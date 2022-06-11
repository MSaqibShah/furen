from sqlalchemy.orm import session
from app.models.user import User
from app import db, bcrypt
import os


def createUser(uname, uemail, password,upin, unumber='', uaddress='', ucity='', ustates='',uid=None):
    if (uid != None):
        u  = User(uname, uemail, password,upin, unumber, uaddress, ucity, ustates, uid)
    else:    
        u  = User(uname, uemail, password,upin, unumber, uaddress, ucity, ustates,)
    db.session.add(u)
    db.session.commit()
    print("------------------------------------")
    print(u, 'created!')
    print("------------------------------------")

     
def updateUser(uid,uname=None, uemail=None, password=None,upin=None, unumber=None, uaddress=None, ucity=None, ustates=None):
    u  = User.query.get(uid) 

    u.uname = uname or u.uname
    u.uemail = uemail or u.uemail  
    u.upin = upin or u.upin
    u.unumber = unumber or u.unumber                 
    u.uaddress = uaddress or u.uaddress
    u.ucity = ucity or u.ucity
    u.ustates = ustates or u.ustates
    if(password != None):
        u.setPassword(password)
    
    db.session.add(u)
    db.session.commit()
    print("------------------------------------")
    print(u, 'updated!')
    print("------------------------------------")


def deleteUser(uid):
    u = User.query.get(uid)
    db.session.delete(u)
    db.session.commit()
    print("------------------------------------")
    print(u, 'deleted!')
    print("------------------------------------")

def checkUser(email, password):
    t = f"SELECT * FROM user where uemail='{email}'"
    conn = db.session.connection()
    result = conn.execute(t)
    r = result.first()
    if(r is None):
        return {
                'uid': None,
                'status': "bad",
                'code': 400,
                'maessage': 'user not found'
                }
    try:
        p = bcrypt.check_password_hash(r[8], password)
        if p:
            print('Logged In')
            return {
                'uid': r[0],
                'status': "ok",
                'code': 200,
                'maessage': 'Logged In'
                }
        else: 
            return {
                'uid': None,
                'status': "bad",
                'code': 400,
                'state': 'Wrong password'
                }
    except:
        print("Exception")
    

def getUsers():
    t = f'SELECT * FROM USER'
    conn = db.session.connection()
    result = conn.execute(t)
    r = []
    for row in result:
        r.append(row._asdict())
    return r

def getUser(uid):
    t = f"SELECT * FROM USER WHERE UID = '{uid}'"
    conn = db.session.connection()
    result = conn.execute(t)
    res = result.first()
    r = res._asdict()
    return r