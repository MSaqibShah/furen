from app import app
from app.controllers import \
    productController as pc, \
    userController as uc, \
    employeeController as ec, \
    paymentController as payc , \
    bookingController as bc, \
    rentController as rc, \
    cartCotroller as cc
from app.models.employee import Employee
from flask import render_template, request, session, redirect

cart_obj =  {}

# @app.route('/')
# def get():
#     # p = pc.updateProduct(52,pname="un2",pdesc='updated desc')
#     # p = pc.deleteProduct(51)
#     # print(p)
    # p =  uc.createUser("Gaurav","gaurav@gmail.com", "qwerty123", '10520')
#     # p =  uc.updateUser(1,uname="abc")
#     # p =  uc.deleteUser(1)
#     # p = ec.createEmployee('kush', "124521","aaaa", 'A', 5000)
#     # p = payc.createPayment('Payment For b', 3000, 'Pending')
#     # p = payc.deletePayment(2)
#     # p = payc.updatePayment(3, "Payment for B")
#     # p = bc.createBooking('asda',2,52)
#     # p = bc.deleteBooking(9)
#     # p = rc.createRent(10,52,2,1)
#     # p = rc.updateRent(2,7)
#     # p = rc.deleteRent(2)

#     return render_template('public/index.html', datasss=p )

@app.route("/", methods=['GET'])
def home():
    if 'emp_id' in session:
        return redirect('/ehome')
    data = pc.getProducts()
    return render_template('public/index.html', data = data)

@app.route("/product/<id>", methods=['GET'])
def product(id):
    product = pc.getProduct(id)
    relatedProducts = pc.getProducts()
    data = {
        'product': product,
        'relatedProducts': relatedProducts
    } 
    return render_template('public/product.html', data = data)

@app.route("/addtocart", methods=['POST'])
def addToCart():
    id = int(request.form.get('product_id'))
    quantity = int(request.form.get('product_quantity'))
    if 'user_id' in session:
        uid = session['user_id']
        pid = id
        cc.createEntry(uid,pid,quantity)
        session['CART'] = cc.getCart(uid)
    elif 'CART' in session:
        cart = session['CART']
        if f'{id}' in cart:
            cart[f'{id}']= cart[f'{id}'] + quantity
            session['CART']= cart 
        else:
            cart[f'{id}'] = quantity
            session['CART']= cart 
    else:
        cart = {}
        cart[f'{id}'] = quantity
        session['CART']= cart 
    
    return redirect('/product/'+str(id))

@app.route('/cart', methods=['GET'])
def cart():
    if'user_id' in session:
        uid = session['user_id']
        data = cc.getCart(uid)
        session['url'] = '/cart'
        cart_products = []
        for pid,quantity in data.items():
            prod = pc.getProduct(pid)
            p = prod._asdict()
            p['quantity'] = quantity
            cart_products.append(p)
        return render_template('public/cart.html', cart_products = cart_products)
    elif 'CART' in session:
        cart = session['CART']
        cart_products = []
        for pid,quantity in cart.items():
            prod = pc.getProduct(pid)
            p = prod._asdict()
            p['quantity'] = quantity
            cart_products.append(p)
        return render_template('public/cart.html', cart_products = cart_products)
    else:
        cart_products = []
        return render_template('public/cart.html', cart_products = cart_products)

@app.route("/handlequantity", methods=['POST'])
def handleQuantity():
    name, pid = request.form['name'],request.form['product_id']

    if name == 'inc':
        if 'user_id' in session:
            uid = session['user_id']
            c = cc.getEntry(uid,pid)
            quantity = c.quantity + 1
            cc.updateEntry(uid,pid,quantity)
            session['CART'] = cc.getCart(uid)
        elif "CART" in session:
                cart = session['CART']
                cart[f'{pid}'] +=1 
                session["CART"] = cart
    elif name== 'dec':
        if 'user_id' in session:
            uid = session['user_id']
            c = cc.getEntry(uid,pid)
            quantity = c.quantity - 1
            if quantity > 0:
                cc.updateEntry(uid,pid,quantity)
            else:
                cc.deleteEntry(uid,pid)
            session['CART'] = cc.getCart(uid)
        elif 'CART' in session:
            cart = session['CART']
            cart[f'{pid}'] -=1 
            if cart[f'{pid}'] <= 0:
                cart.pop(f'{pid}')
            session["CART"] = cart
    elif name == 'rem':
        if 'user_id' in session:
            uid = session['user_id']
            cc.deleteEntry(uid,pid)
            session['CART'] = cc.getCart(uid)
        elif 'CART' in session:
            cart = session['CART'] 
            cart.pop(f'{pid}')
            session["CART"] = cart
    return redirect('/cart')

@app.route('/about', methods=['GET'])
def about():
    return render_template('public/about.html')
