from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, DateField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=150)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class OrderForm(FlaskForm):
    client_name = StringField("Client Name", validators=[DataRequired()])
    description = StringField("Description")
    total_value = FloatField("Total Value", validators=[DataRequired()])
    date = DateField("Date", validators=[DataRequired()])
    submit = SubmitField("Save")
