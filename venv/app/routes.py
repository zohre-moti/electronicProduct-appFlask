from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import Product, UserComments
from app.forms import ProductForm, UserCommentsForm
from flask import flash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

    
# CRUD routes for products
@app.route('/product')
def product():
    products = Product.query.all() 
    return render_template('product.html', products=products) 


@app.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get(id)
    return render_template('product_detail.html', product=product)


@app.route('/delete_product/<int:id>')
def delete_product(id):
    product = Product.query.get(id)
    if product:
        db.session.delete(product)
        db.session.commit()
        flash('محصول با موفقیت حذف شد', 'success')
    else:
        flash('محصول مورد نظر یافت نشد', 'error')
    return redirect(url_for('product'))


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == "POST":
        print(type(request.form))
        form = ProductForm(request.form)
        if form.data is not None:
            product = Product(name=form.name.data, description=form.description.data, price=form.price.data, quantity=form.quantity.data)
            db.session.add(product)
            db.session.commit()
            flash('محصول با موفقیت ایجاد شد', 'success')
            return redirect(url_for('product'))
        else:
            flash('خطا در ارسال دیتا', 'error')
            return render_template('add_product.html')
            
    return render_template('add_product.html')

@app.route('/edit_product/<int:id>', methods=['POST'])
def edit_product(id):
    product = Product.query.get(id)
    if product:
        product.name = request.form['product_name']
        product.description = request.form['description']
        product.price = request.form['price']
        product.quantity = request.form['quantity']

        db.session.commit()
        flash('محصول با موفقیت ویرایش شد', 'success')
    else:
        flash('محصول مورد نظر یافت نشد', 'error')
    return redirect(url_for('product', id=id))
   
# CRUD routes for user comments
@app.route('/user_comments/<int:product>')
def user_comments(product):
    comments = UserComments.query.all()
    product = Product.query.get(product)
    return render_template('user_comments.html', comments=comments, product=product)

 
@app.route('/submit_comment', methods=['POST'])
def submit_comment():
    if request.method == 'POST':
        comment_text = request.form.get('comment')
        rating = request.form.get('rating')
        product_id = request.form.get('product_id')
        new_comment = UserComments(product_id=product_id,comment=comment_text, rating=rating)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('product'))

@app.route('/product_comments/<int:product_id>', methods=['GET'])
def product_comments(product_id):
    comments = UserComments.query.filter_by(product_id=product_id).all()
    return render_template('product_comments.html', comments=comments)



