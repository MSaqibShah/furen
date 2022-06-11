# from sqlalchemy.sql.functions import user
from app import app
from flask import render_template,request, redirect, session
from app.controllers import \
    userController as uc, \
        cartCotroller as cc, \
        bookingController as bc, \
        productController as pc, \
        triggerControllers as tc, \
        paymentController as payc,\
        rentController as rc,\
        employeeController as ec
import os
import datetime

from app.views.views import product
app.secret_key = os.urandom(24)



@app.route('/login/', methods=['GET', 'POST'])
def login():
    if 'emp_id' in session:
        return redirect('/ehome')

    if (request.method == 'GET'):
        if ('user_id' in session):
            # print(session)
            return redirect('/')
        else:
            return render_template('public/login.html')
    elif (request.method == 'POST'):
        if('emp_id' in session):
            session.pop('emp_id')
        email = request.form.get("email")
        password = request.form.get("password")
        auth = uc.checkUser(email,password)
        if auth['code'] == 200:
            # succesful login 
            session['user_id'] = auth['uid']
            uid = session['user_id']
            # Add session cart items to database

            if 'CART' in session:
                # get all items from the cart
                cart = session['CART']
                # add cart items to db ( or update quantity -> handled by cart controller)  
                for pid,quantity in cart.items():
                    cc.createEntry(uid,pid,quantity)
            
            
            # get items from cart and put them in session
            session['CART'] = cc.getCart(uid)
                     
            # Return to the previous page
            if 'url' in session:
                u = session['url']
                session.pop('url')
                return redirect(u)
            else:
                return redirect('/')
        return redirect('/login')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if (request.method == 'GET'):
        if 'user_id' in session:
                return redirect('/')
        else:
            return render_template('public/register.html')
    elif (request.method == 'POST'):
        if('emp_id' in session):
            session.pop('emp_id')
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        pin = request.form.get("pin")
        number = request.form.get("number")
        state = request.form.get("state")
        p =  uc.createUser(name,email,password, pin, number, address, city, state)
        return redirect('/login/')

@app.route('/logout', methods=['GET'])
def logout():
    if('user_id' in session):
        session.pop('CART')
        session.pop('user_id')
    if('emp_id' in session):
        session.pop('emp_id')
    return redirect('/')

@app.route('/profile', methods=['GET'])
def profile():
    if 'user_id' in session:
        return '<h2>Profile<h2>'
    else: 
        session['url'] = '/profile'
        return redirect('/login')

@app.route('/checkout',methods=['GET','POST'])
def checkout():
    if 'user_id' in session:
        uid = session['user_id']
        cart = session['CART']
        # 'PD' 'D' ''
        for pid,quantity in cart.items():
            bc.createBooking('PD',uid,pid,quantity)
            cc.deleteEntry(uid,pid)
        cart=cc.getCart(uid)
        session['CART'] = cart
        return render_template("public/checkout.html")
    else:
        return redirect('/login')

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if(request.method == 'GET'):
        if 'user_id' in session:
            uid = session['user_id']
            b = bc.getAllBookings(uid)
            products =[]
            
            for row in b:
                new_row ={}
                pid = row[2]
                result = pc.getProduct('pid')
                p = result._asdict()
                p.pop('pid')
                new_row.update(row._asdict())
                new_row.update(p)
                products.append(new_row)
            return render_template('public/orders.html', products=products)
        else:
            return redirect('/login')
    elif request.method == 'POST':
        btn = request.form.get('btn')
        pid = request.form.get('pid')
        bid = request.form.get('bid')
        print('btn', pid, bid)
        # handle cancel 
        if btn == 'cancel':
            if 'user_id' in session:
                uid = session['user_id']
                bc.updateBooking(bid,uid,pid,bstatus='CS')
                return redirect('/orders')
        elif btn == 'return':
            if 'user_id' in session:
                uid = session['user_id']
                bc.updateBooking(bid,uid,pid,bstatus='RR')
                return redirect('/orders')

@app.route('/payments', methods=['GET', 'POST'])
def payments():
    if 'user_id' in session:
        uid = session['user_id']
        p = payc.getAllPayments(uid)
        data =[]
        
        for row in p:
            # print(row)
            new_row ={}

            rid = row[5]
            r = rc.getRent(rid)

            pid = r['pid']
            p = pc.getProduct(pid)

            new_row['paymentid'] = row[0]
            new_row['paymentDate'] = row[1].date()
            new_row['paymentAmount'] = row[2]
            new_row['pname'] = p[1]

            data.append(new_row)
            
        return render_template('public/payments.html', data=data)
    else:
        return redirect('/login')

@app.route('/rentals', methods=['GET', 'POST'])
def rental():
    if request.method == "GET":
        if 'user_id' in session:
            uid = session['user_id']
            rentals = rc.getAllRent(uid)
            data = []
            for r in rentals:
                new_row ={}

                rid = r['rid']
                pid = r['pid']

                product = pc.getProduct(pid)
                new_row['rid'] = rid
                new_row['pid'] = pid
                new_row['rstart'] = r['rstart']
                new_row['rend'] = r['rend']
                new_row['rstatus'] = r['rstatus']
                new_row['pname'] = product['pname']
                
                data.append(new_row)


            return render_template('public/rentals.html', data=data)
        else:
            return redirect('/login')
    
# ******************************************************************
# ******************************************************************
# ******************************************************************
# ******************** EMPLOYEE ROUTES *****************************
# ******************************************************************
# ******************************************************************
# ******************************************************************

@app.route('/elogin/', methods=['GET', 'POST'])
def elogin():
    if (request.method == 'GET'):
        if ('emp_id' in session):
            return redirect('/ehome')
        else:
            return render_template('employee/login.html')
    elif (request.method == 'POST'):
        email = request.form.get("email")
        password = request.form.get("password")
        print("CHECK ********************")           
        auth = ec.checkEmployee(email,password)
        if auth['code'] == 200:
            # succesful login 
            session['emp_id'] = auth['eid'] 
            print("Logged in")           
                     
            # Return to the previous page
            # if 'url' in session:
            #     u = session['url']
            #     session.pop('url')
            #     return redirect(u)
            # else:
            #     return redirect('/ehome')
            return redirect('/elogin')
        else:
            return redirect('/elogin')

@app.route('/elogout', methods=['GET'])
def elogout():
    if('emp_id' in session):
        session.pop('emp_id')
    return redirect('/elogin')

@app.route('/ehome',methods=['GET', 'POST'])
def ehome():
    if request.method == 'GET':
        if('emp_id' in session):
            users = uc.getUsers()
            return render_template('employee/home.html',users=users)
        else:
            return redirect('/elogin')
    elif(request.method == "POST"):
        uid = request.form.get('uid')

@app.route('/user/<uid>',methods=['GET', 'POST'])
def user(uid):
    if('emp_id' in session):
        ur = uc.getUser(uid)
        pr = payc.getAllPayments(uid)
        br = bc.getAllBookings(uid)
        products = []
        payments = []
            
        for row in br:
            new_row ={}
            pid = row[2]
            result = pc.getProduct('pid')
            p = result._asdict()
            p.pop('pid')
            new_row.update(row._asdict())
            new_row.update(p)
            products.append(new_row)

        for row in pr:
            payments.append(row._asdict())

        data = [ur, products,payments]

        return render_template('employee/userdetails.html', data=data)
    else:
        return redirect('/elogin')


@app.route('/delivered', methods=['GET', 'POST'])
def delivered():
    if 'emp_id' in session:
        uid = request.form.get('uid')
        pid = request.form.get('pid')
        bid = request.form.get('bid')
        eid = session['emp_id']



        now = datetime.datetime.utcnow()
        rday = now.strftime('%d')
        rmonth = now.strftime('%m')
        ryear = now.strftime('%y')
        rstart = f'{rday}-{rmonth}-{ryear}'
        rend = f'{rday}-{str(int(rmonth)+1)}-{ryear}'
        rc.createRent(rstart,rend,pid,uid,eid)
        bc.updateBooking(bid,uid,pid, bstatus='DC')
        return redirect(f'/user/{uid}')
    else:
        return redirect('/ehome')

