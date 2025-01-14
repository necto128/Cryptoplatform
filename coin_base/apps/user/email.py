from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_password_reset_email(user: int, password: str):
    """Sends a password reset email to the user."""
    mail_subject = "DROP PASSWORD"
    message = render_to_string(
        "reset-password-confirm.html",
        {
            "user": user,
            "password": password
        },
    )
    to_email = "pamgame1212@mail.ru"
    is_sent = send_mail(
        mail_subject,
        message,
        recipient_list=[to_email],
        from_email=settings.EMAIL_HOST_USER,
    )

    return is_sent
