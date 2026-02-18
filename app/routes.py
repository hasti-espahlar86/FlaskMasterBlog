from flask import Blueprint, render_template, redirect, url_for, flash
from .models import db, User, Post, Comment
from .forms import *
from .utils import generate_otp, send_otp, generate_pdf
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint("main", __name__)

@main.route("/")
def home():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template("home.html", posts=posts)

@main.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed = generate_password_hash(form.password.data)
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=hashed)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful!")
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)

@main.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if form.method.data == "password":
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("main.home"))
        else:
            code = generate_otp()
            user.otp = code
            db.session.commit()
            send_otp(user.email, code)
            return redirect(url_for("main.verify"))

    return render_template("login.html", form=form)

@main.route("/verify", methods=["GET","POST"])
def verify():
    form = VerifyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(otp=form.code.data).first()
        if user:
            login_user(user)
            user.otp = None
            db.session.commit()
            return redirect(url_for("main.home"))
    return render_template("verify.html", form=form)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))

@main.route("/post/new", methods=["GET","POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data,
                    author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("main.home"))
    return render_template("create_post.html", form=form)

@main.route("/post/<int:post_id>", methods=["GET","POST"])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()

    if form.validate_on_submit() and current_user.is_authenticated:
        comment = Comment(content=form.content.data,
                          post_id=post.id,
                          user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()

    pdf_path = generate_pdf(post.title, post.content)

    return render_template("post.html",
                           post=post,
                           form=form,
                           pdf_path=pdf_path)
