from django.core.mail import send_mail
import random
from portal import settings
from .models import Account


def send_otp_via_email(email):
    subject = "Your account verification email"
    otp = random.randint(1000, 9999)
    message = f"Your otp is {otp}"
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
    user_obj = Account.objects.get(email = email)
    user_obj.otp = otp
    user_obj.save()