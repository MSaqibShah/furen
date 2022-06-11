from sqlalchemy.orm import session
from app.models.employee import Employee
from app import db, bcrypt

def createEmployee(ename,enumber,eemail, password,etype,esalary,eid=None,esup=None):
    if (eid != None):
        e  = Employee(ename,enumber,eemail,password,etype,esalary,eid,esup)
    else:    
        e  = Employee(ename,enumber,eemail,password,etype,esalary)
    db.session.add(e)
    db.session.commit()
    print("------------------------------------")
    print(e, 'created!')
    print("------------------------------------")

     
def updateEmployee(eid,ename=None,enumber=None,eemail=None,password=None,etype=None,esalary=None,esup=None):
    e  = Employee.query.get(eid) 

    e.ename = ename or e.ename
    e.eemail = eemail or e.eemail  
    e.etype = etype or e.etype
    e.salary = esalary or e.esalary                 
    e.esup = esup or e.esup
    if(password != None):
        e.setPassword(password)
    
    db.session.add(e)
    db.session.commit()
    print("------------------------------------")
    print(e, 'updated!')
    print("------------------------------------")


def deleteEmployee(eid):
    e = Employee.query.get(eid)
    db.session.delete(e)
    db.session.commit()
    print("------------------------------------")
    print(e, 'deleted!')
    print("------------------------------------")


def checkEmployee(email, password):
    t = f"SELECT * FROM employee where eemail='{email}'"
    conn = db.session.connection()
    result = conn.execute(t)
    r = result.first()
    if(r is None):
        return {
                'eid': None,
                'status': "bad",
                'code': 400,
                'maessage': 'Employee not found'
                }
    try:
        p = bcrypt.check_password_hash(r[7], password)
        if p:
            print('Logged In')
            return {
                'eid': r[0],
                'status': "ok",
                'code': 200,
                'maessage': 'Logged In'
                }
        else: 
            return {
                'eid': None,
                'status': "bad",
                'code': 400,
                'state': 'Wrong password'
                }
    except:
        print("Exception")
