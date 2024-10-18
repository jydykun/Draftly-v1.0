from collections.abc import Iterator
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed, FileSize, FileRequired
from wtforms import StringField, PasswordField, EmailField, BooleanField, \
    TextAreaField, SelectField, HiddenField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError
from app.models import db, User, Subscriber
from app import Config


class SignupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=6, max=25)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    email = EmailField("Email", validators=[DataRequired(), Email(check_deliverability=True)])
    recaptcha = RecaptchaField()

    def validate_username(self, username):
        user = db.session.scalar(db.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError("This username is already exist.")
        
    def validate_email(self, email):
        user = db.session.scalar(db.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError("This email address is already exist.")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")


class PostForm(FlaskForm):
    title = StringField(validators=[DataRequired(), Length(max=50)])
    body = TextAreaField(validators=[DataRequired()])
    category = SelectField("Category : ", choices=[])
    feature_image = FileField(
        "Featured Image : ",
        validators=[
            #FileRequired(),
            FileSize(
                Config.MAX_FILE_SIZE,
                message=f"File size must not exceed {int(Config.MAX_FILE_SIZE/1000000)}MB"
                ),
            FileAllowed(["jpg", "png", "jpeg", "webp"], "Images only!")
            ]
        )
    

class EditPostForm(FlaskForm):
    title = StringField(validators=[DataRequired(), Length(max=50)])
    body = TextAreaField(validators=[DataRequired()])
    category = SelectField("Category: ", choices=[])
    replace_image_picker = HiddenField("Replace Image")


class SubscribeForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email(check_deliverability=True)])

    def validate_email(self, email):
        subscriber = db.session.scalar(db.select(Subscriber).where(Subscriber.email == email.data))
        if subscriber is not None:
            raise ValidationError("This email address is already exist.")
        

class CategoryForm(FlaskForm):
    category = StringField("Add Category:", validators=[DataRequired(), Length(max=50)])