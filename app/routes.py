from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from . import db
from .models import User, Product
from .forms import RegistrationForm, LoginForm, ProductForm

main = Blueprint("main", __name__)

@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful!", "success")
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)

@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("main.inventory"))
        else:
            flash("Login unsuccessful. Check email and password.", "danger")
    return render_template("login.html", form=form)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.login"))

@main.route("/inventory")
@login_required
def inventory():
    products = Product.query.all()
    return render_template("inventory.html", products=products)

@main.route("/product/new", methods=["GET", "POST"])
@login_required
def new_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            description=form.description.data,
            category=form.category.data,
            price=form.price.data,
            quantity=form.quantity.data,
            low_stock_threshold=form.low_stock_threshold.data
        )
        db.session.add(product)
        db.session.commit()
        flash("Product added!", "success")
        return redirect(url_for("main.inventory"))
    return render_template("product_form.html", form=form)

@main.route("/product/<int:product_id>/edit", methods=["GET", "POST"])
@login_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        form.populate_obj(product)
        db.session.commit()
        flash("Product updated!", "success")
        return redirect(url_for("main.inventory"))
    return render_template("product_form.html", form=form)

@main.route("/product/<int:product_id>/delete", methods=["POST"])
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash("Product deleted!", "success")
    return redirect(url_for("main.inventory"))
