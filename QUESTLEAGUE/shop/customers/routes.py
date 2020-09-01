from flask import render_template,session, request,redirect,url_for,flash,current_app,make_response
from flask_mail import Mail, Message
from flask_login import login_required, current_user, logout_user, login_user
from shop import app, db, search, bcrypt, login_manager #, photos
from .forms import CustomerRegisterForm, CustomerLoginFrom,GtagActivision ,GtagPs4,GtagXbox,GtagUnreal
from .model import Register,CustomerOrder

from ..products.models import fortnitesquads, fortnitesolo, fortnitesolops5, fortnitesoloxbox, fifaduo, fifasolo, codsolo, codsquads

import secrets
import os
import json
import pdfkit
import stripe

import os,binascii

Publishable_key = 'pk_test_51H5WRmCdlu629vZwtLwbPk7Q86Gj9xWmlXTfYgsLyrMwxvn0c0vbk1acu6SUQ4xZW3TJCidRjg9e1nTzVGXSLy4L00RwfjQbOx'
stripe.api_key = 'sk_test_51H5WRmCdlu629vZwEzW4zHbqGKkSxykwZAE4gg3SdGu8vR8phXEgH63w6uaeJg4G6mibp1QYM14A7WZcvvn3IFoj00yMIEVZa8'

@app.route('/payment',methods = ['GET' , 'POST'])
@login_required
def payment():
    invoice = request.form.get('invoice')
    amount = request.form.get('amount')
    customer = stripe.Customer.create(
      email=request.form['stripeEmail'],
      source=request.form['stripeToken'],
    )
    charge = stripe.Charge.create(
      customer=customer.id,
      description='Myshop',
      amount=amount,
      currency='gbp',
    )

    # register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
    orders =  CustomerOrder.query.filter_by(customer_id = current_user.id,invoice=invoice).order_by(CustomerOrder.id.desc()).first()
 
    t_name = request.form.get('T_Title')

    if t_name == "fortnite_battle_royal_solo" :
      
        getopponent = db.session.query(fortnitesolo).order_by(fortnitesolo.id.desc()).first()
        if getopponent.opponent == 'ADMIN':
            tournaments = fortnitesolo(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            orders.ttitle = 'fortnitesolo'            
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 
        elif getopponent.opponent == 'NULL' :
            getopponent.opponent = current_user.id 
            tournaments = fortnitesolo(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent=getopponent.Participant_User_Id )
            orders.status = 'Paid'
            orders.ttitle = 'fortnitesolo'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 
        else:
            # getopponent.opponent == '':
            tournaments = fortnitesolo(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            orders.ttitle = 'fortnitesolo'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 
    
    elif t_name == "fifa_1V1_solo" :
        getopponent = db.session.query(fifasolo).order_by(fifasolo.id.desc()).first()
        if getopponent.opponent == 'ADMIN':
            tournaments = fifasolo(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 
        elif getopponent.opponent == 'NULL' :
            getopponent.opponent = current_user.id 
            tournaments = fifasolo(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent=getopponent.Participant_User_Id )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks'))
        else:
            # getopponent.opponent == '':
            tournaments = fifasolo(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 

    elif t_name == "cod_team_death_match_solo" :

        getopponent = db.session.query(codsolo).order_by(codsolo.id.desc()).first()
        if getopponent.opponent == 'ADMIN':
            tournaments = codsolo(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 
        elif getopponent.opponent == 'NULL' :
            getopponent.opponent = current_user.id 
            tournaments = codsolo(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent=getopponent.Participant_User_Id )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks'))
        else:
            # getopponent.opponent == '':
            tournaments = codsolo(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 

    elif t_name == "fortnite_battle_royal_squads" :

        tournaments = fortnitesquads(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' )
        getopponent = db.session.query(fortnitesquads).order_by(fortnitesquads.id.desc()).first()
        if getopponent.opponent == 'ADMIN':
            tournaments = fortnitesquads(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 
        elif getopponent.opponent == 'NULL' :
            getopponent.opponent = current_user.id 
            tournaments = fortnitesquads(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent=getopponent.Participant_User_Id )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks'))
        else:
            # getopponent.opponent == '':
            tournaments = fortnitesquads(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 

    elif t_name == "fifa_2v2_duo" :

        getopponent = db.session.query(fifaduo).order_by(fifaduo.id.desc()).first()
        if getopponent.opponent == 'ADMIN':
            tournaments = fifaduo(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks'))         
        elif getopponent.opponent == 'ADMIN':
            tournaments = fifaduo(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 
        else:
            # getopponent.opponent == '':
            tournaments = fifaduo(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 


    elif t_name == "cod_team_death_match" :

        getopponent = db.session.query(codsquads).order_by(codsquads.id.desc()).first()
        if getopponent.opponent == 'ADMIN':
            tournaments = codsquads(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 
        elif getopponent.opponent == 'NULL' :
            getopponent.opponent = current_user.id 
            tournaments = codsquads(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent=getopponent.Participant_User_Id )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks'))
        else:
            # getopponent.opponent == '':
            tournaments = codsquads(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 


    elif t_name == "fortnite_battle_royal_solo_ps5" :

        getopponent = db.session.query(fortnitesolops5).order_by(fortnitesolops5.id.desc()).first()
        if getopponent.opponent == 'ADMIN':
            tournaments = fortnitesolops5(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 
        elif getopponent.opponent == 'NULL' :
            getopponent.opponent = current_user.id 
            tournaments = fortnitesolops5(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent=getopponent.Participant_User_Id )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks'))
        else:
            # getopponent.opponent == '':
            tournaments = fortnitesolops5(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 

    elif t_name == "fortnite_battle_royal_solo_xboxX" :

        getopponent = db.session.query(fortnitesoloxbox).order_by(fortnitesoloxbox.id.desc()).first()
        if getopponent.opponent == 'ADMIN':
            uni_hex = binascii.b2a_hex(os.urandom(15))
            tournaments = fortnitesoloxbox(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' , opponent_gamertag='NULL' , player1_video='NULL' , player2_video='NULL' , player1_time='NULL' , player2_time='NULL' , game_key=uni_hex, winner='NULL' )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks'))         
        elif getopponent.opponent == 'NULL' :
            getopponent.opponent = current_user.id 
            tournaments = fortnitesoloxbox(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent=getopponent.Participant_User_Id , opponent_gamertag=getopponent.opponent_gamertag , player1_video='NULL' , player2_video='NULL' , player1_time='NULL' , player2_time='NULL' , game_key= getopponent.game_key , winner='NULL'  )
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks'))
        else:
            # getopponent.opponent == '':
            tournaments = fortnitesoloxbox(Participant_User_Id=current_user.id , Participant_State='in' , Gamertag_PC='test' , Gamertag_XBOX='test' , Gamertag_PS4='test' , Team_member_1='test' , Team_member_2='test' , Team_member_3='test' , opponent='NULL' ,  opponent_gamertag='NULL' , player1_video='NULL' , player2_video='NULL' , player1_time='NULL' , player2_time='NULL' , game_key=uni_hex , winner='NULL'  ) 
            orders.status = 'Paid'
            db.session.add(tournaments)
            db.session.commit()
            return redirect(url_for('thanks')) 



    return redirect(url_for('sorry'))




@app.route('/thanks')
def thanks():
    return render_template('customer/thank.html')

@app.route('/sorry')
def sorry():
    return render_template('customer/sorry.html')


@app.route('/Email')
def email():
    msg = Message('Shape-It Test', recipients=['meson93702@aprimail.com'])
    mail.send(msg)
    return 'Message Has Been Sent'

@app.route('/landing2',methods =['GET' , 'POST'])
def landing2():
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('store'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('customerLogin'))
    
    return render_template('landingtest.html', title='layout', form=form)

@app.route('/layout_landing',methods =['GET' , 'POST'])
def layout_landing():

    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('store'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('customerLogin'))
                    
    return render_template('layout_landing.html', title='layout_landing' , form=form)



@app.route('/customer/register', methods=['GET','POST'])
def customer_register():
    formR = CustomerRegisterForm()
    if formR.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(formR.password.data)
        register = Register(FirstName=formR.FirstName.data, SecondName=formR.SecondName.data, username=formR.username.data, email=formR.email.data, password=hash_password)
        db.session.add(register)
        flash(f'Welcome {formR.username.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('customerLogin'))
    return render_template('customer/register.html', formR=formR)


@app.route('/customer/login', methods=['GET','POST'])
def customerLogin():
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('landing'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('customerLogin'))
            
    return render_template('customer/login.html', form=form)


@app.route('/customer/gamertag', methods=['GET','POST'])
def gamertag():
    formg = GtagActivision()
    if formg.validate_on_submit():
        # hash_password = bcrypt.generate_password_hash(formg.password.data)
        gtag = Register(gtag_activision=formg.gtag_activision.data )
        db.session.add(gtag)
        flash(f'{formg.gtag_activision.data} has been added as you activision gamer tag', 'success')
        db.session.commit()
        return redirect(url_for('customer/gamertag'))
    return render_template('customer/add_gamer_tag.html', formg=formg)


@app.route('/customer/logout')
def customer_logout():
    logout_user()
    return redirect(url_for('landing'))

######## Remove unwanted Details from Shopping Cart ########
def updateshoppingcart():
    for key, shopping in session['Shoppingcart'].items():
        session.modified = True
        del shopping['image']
        del shopping['colors']
    return updateshoppingcart

@app.route('/getorder', methods= ['GET' , 'POST'])
@login_required
def get_order():
    if current_user.is_authenticated:
        customer_id = current_user.id
        invoice = secrets.token_hex(5)

        ttitle = request.form.get('T_Title')
        
        updateshoppingcart
        try:
            order = CustomerOrder( ttitle=ttitle, invoice=invoice,customer_id=customer_id, orders=session['Shoppingcart'])
            db.session.add(order)
            db.session.commit()
            session.pop('Shoppingcart')
            flash('Your order has been sent successfully','success')
            return redirect(url_for('orders',invoice=invoice))
        except Exception as e:
            print(e)
            flash('Some thing went wrong while get order', 'danger')
            return redirect(url_for('getCart'))
        

@app.route('/orders/<invoice>')
@login_required
def orders(invoice):
    if current_user.is_authenticated:  
        grandTotal = 0
        subTotal = 0
        customer_id = current_user.id
        customer = Register.query.filter_by(id=customer_id).first()
        orders = CustomerOrder.query.filter_by(customer_id=customer_id, invoice=invoice).order_by(CustomerOrder.id.desc()).first()
        # msg = Message('Sucessfull Send', sender='reggie1997@hotmail.co.uk', recipients=['reggie1997@hotmail.co.uk'] )
        # mail.send(msg)

        
        for _key, product in orders.orders.items():
            discount = (product['discount']/100) * float(product['price'])
            subTotal += float(product['price']) * int(product['quantity'])
            subTotal -= discount
            tax = ("%.2f" % (.06 * float(subTotal)))
            grandTotal = ("%.2f" % (1.06 * float(subTotal)))

    else:
        return redirect(url_for('customerLogin'))

    return render_template('customer/order.html', invoice=invoice, tax=tax,subTotal=subTotal,grandTotal=grandTotal,customer=customer,orders=orders)

@app.route('/myorder')
@login_required
def myorders():
    if current_user.is_authenticated:  
        grandTotal = 0
        subTotal = 0
        customer_id = current_user.id
        customer = Register.query.filter_by(id=customer_id).first()
        # orders = CustomerOrder.query.all()
        orders = CustomerOrder.query.filter_by(customer_id=customer_id).order_by(CustomerOrder.id.desc()).first()

        for key, product in orders.orders.items():
            discount = (product['discount']/100) * float(product['price'])
            subTotal += float(product['price']) * int(product['quantity'])
            subTotal -= discount
            tax = ("%.2f" % (.06 * float(subTotal)))
            grandTotal = float("%.2f" % (1.06 * subTotal))

    else:
        return redirect(url_for('customerLogin'))

    return render_template('myorder.html',grandTotal=grandTotal,customer=customer,orders=orders)


@app.route('/get_pdf/<invoice>', methods=['POST'])
@login_required
def get_pdf(invoice):
    if current_user.is_authenticated:
        grandTotal = 0
        subTotal = 0
        customer_id = current_user.id
        if request.method =="POST":
            customer = Register.query.filter_by(id=customer_id).first()
            orders = CustomerOrder.query.filter_by(customer_id=customer_id, invoice=invoice).order_by(CustomerOrder.id.desc()).first()
            for _key, product in orders.orders.items():
                discount = (product['discount']/100) * float(product['price'])
                subTotal += float(product['price']) * int(product['quantity'])
                subTotal -= discount
                tax = ("%.2f" % (.06 * float(subTotal)))
                grandTotal = float("%.2f" % (1.06 * subTotal))

            rendered =  render_template('customer/pdf.html', invoice=invoice, tax=tax,grandTotal=grandTotal,customer=customer,orders=orders)
            pdf = pdfkit.from_string(rendered, False)
            response = make_response(pdf)
            response.headers['content-Type'] ='application/pdf'
            response.headers['content-Disposition'] ='inline; filename='+invoice+'.pdf'
            return response
    return request(url_for('orders'))



