from flask import render_template,session, request,redirect,url_for,flash,current_app
from flask_login import login_required, current_user, logout_user, login_user
from shop import app, db, search, bcrypt, login_manager #, photos
from .models import Category,Brand,Addproduct,fortnitesquads, fortnitesolo, fortnitesolops5, fortnitesoloxbox, fifaduo, fifasolo, codsolo, codsquads
from shop.customers.model import Register
from .forms import Addproducts, MyForm
from ..customers.forms import CustomerLoginFrom, CustomerRegisterForm
from ..customers.model import CustomerOrder
import os
import os,binascii
import secrets

# ###########  TEST FILE UPLOAD ###########################

from werkzeug.utils import secure_filename



################

from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet

#################### Functions to Add to STORE page ####################
def brands():
    brands = Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    return brands

def categories():
    categories = Category.query.join(Addproduct,(Category.id == Addproduct.category_id)).all()
    return categories

def single_page(id):
    product = Addproduct.query.get_or_404(id)
    return single_page(id)


def AddCart():
    try:
        product_id = request.form.get('product_id')
        T_Title = request.form.get('T_Title')
        quantity = int(request.form.get('quantity'))
        color = request.form.get('colors')
        product = Addproduct.query.filter_by(id=product_id).first()

        if request.method =="POST":
            DictItems = {product_id:{'name':product.name,'price':float(product.price),'discount':product.discount,'color':color,'quantity':quantity,'image':product.image_1, 'colors':product.colors , 'T_Title':T_Title}}
            if 'Shoppingcart' in session:
                print(session['Shoppingcart'])
                if product_id in session['Shoppingcart']:
                    for key, item in session['Shoppingcart'].items():
                        if int(key) == int(product_id):
                            session.modified = True
                            item['quantity'] += 1
                else:
                    session['Shoppingcart'] = MagerDicts(session['Shoppingcart'], DictItems)
                    return redirect(request.referrer)
            else:
                session['Shoppingcart'] = DictItems
                return redirect(request.referrer)    
    except Exception as e:
        print(e) 
    finally:
        return redirect(request.referrer)

def MagerDicts(dict1,dict2):
    if isinstance(dict1, list) and isinstance(dict2,list): 
        return dict1  + dict2
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))

def grandtotal ():
    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return redirect(url_for('store'))
    subtotal = 0
    grandtotal = 0
    for key,product in session['Shoppingcart'].items():
        discount = (product['discount']/100) * float(product['price'])
        subtotal += float(product['price']) * int(product['quantity'])
        subtotal -= discount
        grandtotal = float("%.2f" % (1.06 * subtotal)) 
    return grandtotal 


####################### quick register ################################

@app.route('/quick_register')
def quick_register():
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc())
    product = Addproduct.query.get_or_404(6)
    p_id = 3
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    allresult = Addproduct.query.all()

        #Customer Login Logic 
    form = CustomerLoginFrom()

    form_R = CustomerRegisterForm()
    if form_R.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form_R.password.data)
        register = Register(name=form_R.name.data, username=form_R.username.data, email=form_R.email.data,password=hash_password,country=form_R.country.data, city=form_R.city.data,contact=form_R.contact.data, address=form_R.address.data, zipcode=form_R.zipcode.data)
        db.session.add(register)
        flash(f'Welcome {form_R.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('welcome'))

        
    return render_template('quick_register.html' ,products=products, product=product, allresult=allresult, filterd_resultr=filterd_resultr, form=form, form_R=form_R )




#################### Functions to Add to STORE page ####################

@app.route('/landing',methods =['GET' , 'POST'])
def landing():

    page = request.args.get('page',1, type=int)
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).paginate(page=page, per_page=16)
    product = Addproduct.query.get_or_404(1)
    sizes = Addproduct.query.filter(Addproduct.size)




    p_id = "1"
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()

    vi_product=filterd_resultr

    #Customer Login Logic 
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('landing'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('landing'))

    #Customer Register Logic
    form_R = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        flash(f'landing {form.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('landing'))  

    return render_template('landing.html', title='layout' , grandtotal=grandtotal(), products=products, brands=brands(), product=product, filterd_resultr=filterd_resultr, vi_product=vi_product, categories=categories(), form_R=form_R, form=form )


#################### Functions to Add to STORE page ####################
@app.route('/',methods =['GET' , 'POST'])
@app.route('/welcome',methods =['GET' , 'POST'])
def welcome():

    page = request.args.get('page',1, type=int)
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc())
    products = Addproduct.query.filter(Addproduct.stock > 0)

    p_id = "1"
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    product = Addproduct.query.get_or_404(1)
    vi_product=filterd_resultr

    #Customer Login Logic 
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('my_account'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('my_account'))

    #Customer Register Logic
    form_R = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('my_account'))  

    return render_template('home.html', title='layout',  grandtotal=grandtotal(), products=products, brands=brands(), product=product, filterd_resultr=filterd_resultr, vi_product=vi_product, categories=categories(), form_R=form_R, form=form)



@app.route('/footer')
def footer():
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc())
    product = Addproduct.query.get_or_404(6)
    p_id = 3
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    allresult = Addproduct.query.all()
    return render_template('footer.html' ,products=products, product=product, allresult=allresult, filterd_resultr=filterd_resultr)


@app.route('/about')
def about():
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc())
    product = Addproduct.query.get_or_404(6)
    p_id = 3
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    allresult = Addproduct.query.all()

        #Customer Login Logic 
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('my_account'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('my_account'))

    #Customer Register Logic
    form_R = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('my_account'))  

        
    return render_template('aboutus.html' ,products=products, product=product, allresult=allresult, filterd_resultr=filterd_resultr, form=form, form_R=form_R )



@app.route('/rules')
def rules():
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc())
    product = Addproduct.query.get_or_404(6)
    p_id = 3
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    allresult = Addproduct.query.all()

        #Customer Login Logic 
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('store'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('store'))

    #Customer Register Logic
    form_R = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('store'))  

        
    return render_template('rules.html' ,products=products, product=product, allresult=allresult, filterd_resultr=filterd_resultr, form=form, form_R=form_R )


@app.route('/tournaments')
def tournaments():
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc())
    product = Addproduct.query.get_or_404(6)
    p_id = 3
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    allresult = Addproduct.query.all()

        #Customer Login Logic 
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('store'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('store'))

    #Customer Register Logic
    form_R = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('store'))  

        
    return render_template('tournaments.html' ,products=products, product=product, allresult=allresult, filterd_resultr=filterd_resultr, form=form, form_R=form_R )




# ########################
ALLOWED_EXTENSIONS = {'mp4', 'jpg', 'png'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/my_account' ,  methods=['GET', 'POST'])
def my_account():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # game_key = request.files['game_key']
        game_key = request.form['game_key']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # UPLOAD USERS FILE AND ADD NAME OF FILE TO PLAYER 1 
            d_filename = secure_filename(file.filename)
            name_split = d_filename.split(".", 1)
            file_ext = '.'+name_split[1]
            uni_hex = binascii.b2a_hex(os.urandom(6))
            filename = str(game_key)+'-'+str(current_user.id)+'-'+str(uni_hex)+file_ext

            player =  fortnitesoloxbox.query.filter_by(Participant_User_Id = current_user.id,game_key=game_key).order_by(fortnitesoloxbox.id.desc()).first()
            player.player1_video = str(filename)

            # opponent =  fortnitesoloxbox.query.filter_by(Participant_User_Id != current_user.id,game_key=game_key).order_by(fortnitesoloxbox.id.desc()).first()
            # player.player_video = str(filename)
            # all_participants = fortnitesoloxbox.query.all()

            # all_p = len(all_participants)
            # counter = 0
            # while counter < all_p:
            #     counter += 1
            
            # if counter > 1 :               
            #     opponent = fortnitesoloxbox.query.filter_by(Participant_User_Id != current_user.id,game_key=game_key).order_by(fortnitesoloxbox.id.desc()).first()
            #     player.player2_video = str(filename)
            #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))    
            #     db.session.commit()

            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))    

            db.session.commit()
            flash(f'YOUR VIDEO WAS UPLOADED','success')
            return redirect(url_for('home'))  

# #########################

    page = request.args.get('page',1, type=int)
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc())
    products = Addproduct.query.filter(Addproduct.stock > 0)

    p_id = "1"
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    product = Addproduct.query.get_or_404(1)
    vi_product=filterd_resultr

    customer_order = CustomerOrder.query.filter(CustomerOrder.customer_id == current_user.id)
    fortnite_solo = fortnitesoloxbox.query.filter(CustomerOrder.customer_id == current_user.id)
    
    # fortnite_solo = fortnitesoloxbox.query.filter(fortnitesolo.Participant_User_Id == current_user.id)
#   VIDEO FILE UPLOAD
# from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import FileField
# from flask_uploads import configure_uploads, IMAGES, UploadSet

# app = Flask(__name__)

# app.config['SECRET_KEY'] = 'thisisasecret'
# app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'

    images = UploadSet('images', IMAGES)
    configure_uploads(app, images)

# # class MyForm(FlaskForm):
# #     image = FileField('image')
# # @app.route('/', methods=['GET', 'POST'])
# # def index():

    formVU = MyForm()
    if formVU.validate_on_submit():
        filename = images.save(formVU.image.data)
        return f'Filename: { filename }'

    # return render_template('index.html', formVU=formVU)

    #Customer Login Logic 
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('store'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('store'))

    #Customer Register Logic
    form_R = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('store'))  

    return render_template('my_account.html', title='layout',  grandtotal=grandtotal(), products=products, brands=brands(), product=product, filterd_resultr=filterd_resultr, vi_product=vi_product, categories=categories(), form_R=form_R, form=form, customer_order=customer_order, fortnite_solo=fortnite_solo,formVU=formVU)




@app.route('/ourgames')
def ourgames():
    page = request.args.get('page',1, type=int)
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc())
    products = Addproduct.query.filter(Addproduct.stock > 0)

    p_id = "1"
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    product = Addproduct.query.get_or_404(1)
    vi_product=filterd_resultr

    #Customer Login Logic 
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('store'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('store'))

    #Customer Register Logic
    form_R = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('store'))  

    return render_template('ourgames.html', title='layout',  grandtotal=grandtotal(), products=products, brands=brands(), product=product, filterd_resultr=filterd_resultr, vi_product=vi_product, categories=categories(), form_R=form_R, form=form)





@app.route('/order_history')
def order_history():
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc())
    product = Addproduct.query.get_or_404(6)
    p_id = 3
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    allresult = Addproduct.query.all()
    return render_template('order_history.html' ,products=products, product=product, allresult=allresult, filterd_resultr=filterd_resultr)

@app.route('/settings')
def settings():
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc())
    product = Addproduct.query.get_or_404(6)
    p_id = 3
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    allresult = Addproduct.query.all()
    return render_template('settings.html' ,products=products, product=product, allresult=allresult, filterd_resultr=filterd_resultr)
	
@app.route('/test')
def test():
    product = Addproduct.query.get_or_404(6)
    p_id = 3
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    allresult = Addproduct.query.all()
    return render_template('test.html' , product=product, allresult=allresult, filterd_resultr=filterd_resultr)

 
@app.route('/layout',methods =['GET' , 'POST'])
def layout():
    product = Addproduct.query.get_or_404(6)
    return render_template('layout.html', title='layout', product=product)

@app.route('/layout_store',methods =['GET' , 'POST'])
def layout_store():
    filterd_resultr="filterd_resultr"
    product = Addproduct.query.get_or_404(6)
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc())
    return render_template('layout_store.html', title='layout', product=product, filterd_resultr=filterd_resultr, products= products)

@app.route('/store',methods =['GET' , 'POST'])
def store():
    page = request.args.get('page',1, type=int)
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).paginate(page=page, per_page=16)
    product = Addproduct.query.get_or_404(1)
    sizes = Addproduct.query.filter(Addproduct.size)

    p_id = "1"
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    product = Addproduct.query.get_or_404(4)
    vi_product=filterd_resultr

    #Customer Login Logic 
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('store'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('store'))

    #Customer Register Logic
    form_R = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(FirstName=form.FirstName.data, SecondName=form.SecondName.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('store'))  

    return render_template('store.html', title='layout',sizes=sizes, grandtotal=grandtotal(), products=products, brands=brands(), product=product, filterd_resultr=filterd_resultr, vi_product=vi_product, categories=categories(), form_R=form_R, form=form)


@app.route('/store2',methods =['GET' , 'POST'])
def store2():
    page = request.args.get('page',1, type=int)
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).paginate(page=page, per_page=16)
    product = Addproduct.query.get_or_404(1)
    sizes = Addproduct.query.filter(Addproduct.size)

    p_id = "1"
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    # product = Addproduct.query.get_or_404(4)
    vi_product=filterd_resultr

    #Customer Login Logic 
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('store'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('store'))

    #Customer Register Logic
    form_R = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('store'))  

    return render_template('store2.html', title='layout',sizes=sizes, grandtotal=grandtotal(), products=products, brands=brands(), product=product, filterd_resultr=filterd_resultr, vi_product=vi_product, categories=categories(), form_R=form_R, form=form)





@app.route('/home')
def home():
    page = request.args.get('page',1, type=int)
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).paginate(page=page, per_page=8)
    product = Addproduct.query.get_or_404(1)

    return render_template('products/index.html', products=products,brands=brands(),categories=categories(), product=product)

@app.route('/result')
def result():
    searchword = request.args.get('q')
    products = Addproduct.query.msearch(searchword, fields=['name','desc'] , limit=6).all()
    return render_template('products/result.html',products=products,brands=brands(),categories=categories())

@app.route('/product/<int:id>')
def single_page(id):

    product = Addproduct.query.get_or_404(id)

    page = request.args.get('page',1, type=int)
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc())
    products = Addproduct.query.filter(Addproduct.stock > 0)
    
    fortnite_Squads = fortnitesquads.query.filter(fortnitesquads.id > 0).order_by(fortnitesquads.id.desc()).paginate(page=page, per_page=16)
    # fortnite = fortnitesquads.query.filter(fortnitesquads.id > 0).order_by(fortnitesquads.id.desc()).paginate(page=page, per_page=16)


    fortnite = fortnitesquads.query.filter(fortnitesquads.id > 0).order_by(fortnitesquads.id.desc()).paginate(page=page, per_page=16)
    fortnite_solo = fortnitesolo.query.filter(fortnitesquads.id > 0).order_by(fortnitesquads.id.desc()).paginate(page=page, per_page=16)

    cod_squads = fortnitesolo.query.filter(fortnitesquads.id > 0).order_by(fortnitesquads.id.desc()).paginate(page=page, per_page=16)
    cod_solo = codsolo.query.filter(codsolo.id > 0).order_by(codsolo.id.desc()).paginate(page=page, per_page=16)

    fifa_squads = fortnitesolo.query.filter(fortnitesquads.id > 0).order_by(fortnitesquads.id.desc()).paginate(page=page, per_page=16)
    fifa_solo = fortnitesolo.query.filter(fortnitesquads.id > 0).order_by(fortnitesquads.id.desc()).paginate(page=page, per_page=16)

    p_id = "1"

    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    product = Addproduct.query.get_or_404(id)
    vi_product=filterd_resultr

    #Customer Login Logic 
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('store'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('store'))

    #Customer Register Logic
    form_R = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('store'))

    return render_template('products/single_page.html',fortnite_solo=fortnite_solo, cod_squads=cod_squads, cod_solo=cod_solo, fifa_squads=fifa_squads, fifa_solo=fifa_solo, product=product,brands=brands(),categories=categories(),grandtotal=grandtotal(), products=products, filterd_resultr=filterd_resultr, vi_product=vi_product, form=form, form_R=form_R, fortnite=fortnite)


@app.route('/brand/<int:id>')
def get_brand(id):
    page = request.args.get('page',1, type=int)
    get_brand = Brand.query.filter_by(id=id).first_or_404()
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).paginate(page=page, per_page=16)
    brand = Addproduct.query.filter_by(brand=get_brand).paginate(page=page, per_page=8)

    p_id = "1"
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    product = Addproduct.query.get_or_404(1)
    vi_product=filterd_resultr

    #Customer Login Logic 
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('store'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('store'))

    #Customer Register Logic
    form_R = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('store')) 

    return render_template('store.html',brand=brand,brands=brands(), categories=categories(),get_brand=get_brand,grandtotal=grandtotal(), filterd_resultr=filterd_resultr, vi_product=vi_product, form_R=form_R, form=form)


@app.route('/categories/<int:id>')
def get_category(id):
    page = request.args.get('page',1, type=int)
    get_cat = Category.query.filter_by(id=id).first_or_404()
    products = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).paginate(page=page, per_page=16)
    get_cat_prod = Addproduct.query.filter_by(category=get_cat).paginate(page=page, per_page=8)

    p_id = "1"
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    product = Addproduct.query.get_or_404(1)
    vi_product=filterd_resultr

    #Customer Login Logic 
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('store'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('store'))

    #Customer Register Logic
    form_R = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('store')) 
        
    return render_template('store.html',get_cat_prod=get_cat_prod,brands=brands(),categories=categories(),get_cat=get_cat, grandtotal=grandtotal(), filterd_resultr=filterd_resultr, vi_product=vi_product, form_R=form_R, form=form)

@app.route('/Discount')
def get_Discount():
    page = request.args.get('page',1, type=int)
    products = Addproduct.query.filter(Addproduct.stock > 0, Addproduct.discount).order_by(Addproduct.id.desc()).paginate(page=page, per_page=16)
    product = Addproduct.query.get_or_404(1)

    p_id = "1"
    filterd_resultr=Addproduct.query.filter_by(id=p_id).first()
    product = Addproduct.query.get_or_404(1)
    vi_product=filterd_resultr

    #Customer Login Logic 
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You are login now!', 'success')
            next = request.args.get('next')
            return redirect(next or url_for('store'))
        flash('Incorrect email and password','danger')
        return redirect(url_for('store'))

    #Customer Register Logic
    form_R = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('store'))  

    return render_template('store.html', title='layout', grandtotal=grandtotal(), products=products, brands=brands(), product=product, filterd_resultr=filterd_resultr, vi_product=vi_product, categories=categories(), form_R=form_R, form=form)

@app.route('/addbrand',methods=['GET','POST'])
def addbrand():
    if request.method =="POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', title='Add brand',brands='brands')

@app.route('/updatebrand/<int:id>',methods=['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method =="POST":
        updatebrand.name = brand
        flash(f'The brand {updatebrand.name} was changed to {brand}','success')
        db.session.commit()
        return redirect(url_for('brands'))
    brand = updatebrand.name
    return render_template('products/addbrand.html', title='Udate brand',brands='brands',updatebrand=updatebrand)


@app.route('/deletebrand/<int:id>', methods=['GET','POST'])
def deletebrand(id):
    brand = Brand.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(brand)
        flash(f"The brand {brand.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"The brand {brand.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))

@app.route('/addcat',methods=['GET','POST'])
def addcat():
    if request.method =="POST":
        getcat = request.form.get('category')
        category = Category(name=getcat)
        db.session.add(category)
        flash(f'The brand {getcat} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addbrand.html', title='Add category')


@app.route('/updatecat/<int:id>',methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')  
    if request.method =="POST":
        updatecat.name = category
        flash(f'The category {updatecat.name} was changed to {category}','success')
        db.session.commit()
        return redirect(url_for('categories'))
    category = updatecat.name
    return render_template('products/addbrand.html', title='Update cat',updatecat=updatecat)



@app.route('/deletecat/<int:id>', methods=['GET','POST'])
def deletecat(id):
    category = Category.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(category)
        flash(f"The brand {category.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"The brand {category.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))


@app.route('/addproduct', methods=['GET','POST'])
def addproduct():
    form = Addproducts(request.form)
    brands = Brand.query.all()
    categories = Category.query.all()
    if request.method=="POST"and 'image_1' in request.files:
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        size = form.size.data
        colors = form.colors.data
        desc = form.discription.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        addproduct = Addproduct(name=name,price=price,size=size,discount=discount,stock=stock,colors=colors,desc=desc,category_id=category,brand_id=brand,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(addproduct)
        flash(f'The product {name} was added in database','success')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('products/addproduct.html', form=form, title='Add a Product', brands=brands,categories=categories)



@app.route('/updateproduct/<int:id>', methods=['GET','POST'])
def updateproduct(id):
    form = Addproducts(request.form)
    product = Addproduct.query.get_or_404(id)
    brands = Brand.query.all()
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')
    if request.method =="POST":
        product.name = form.name.data 
        product.price = form.price.data
        product.discount = form.discount.data
        product.stock = form.stock.data 
        product.size = form.size.data
        product.colors = form.colors.data
        product.desc = form.discription.data
        product.category_id = category
        product.brand_id = brand
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        flash('The product was updated','success')
        db.session.commit()
        return redirect(url_for('admin'))
    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.size.data = product.size
    form.colors.data = product.colors
    form.discription.data = product.desc
    brand = product.brand.name
    category = product.category.name
    return render_template('products/addproduct.html', form=form, title='Update Product',getproduct=product, brands=brands,categories=categories)


@app.route('/deleteproduct/<int:id>', methods=['POST'])
def deleteproduct(id):
    product = Addproduct.query.get_or_404(id)
    if request.method =="POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
        except Exception as e:
            print(e)
        db.session.delete(product)
        db.session.commit()
        flash(f'The product {product.name} was delete from your record','success')
        return redirect(url_for('admin'))
    flash(f'Can not delete the product','success')
    return redirect(url_for('admin'))
