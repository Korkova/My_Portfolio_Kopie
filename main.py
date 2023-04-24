from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired, Email
# from flask_bootsrap import Bootstrap
import smtplib

# class LoginForm(FlaskForm):
#     email = StringField(label="Email", validators=[DataRequired(), Email()])
#     password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
#     submit = SubmitField(label="Log In")

OWN_EMAIL = "laraparako@gmail.com"
OWN_PASSWORD = "123456"


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__ == "__main__":
    app.run(debug=True)
