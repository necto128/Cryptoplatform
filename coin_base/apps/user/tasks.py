from celery import shared_task

from apps.user.email import send_password_reset_email


@shared_task
def send_password_reset_email_celery_task(user_id: int, password: str) -> None:
    """Celery task for sending password reset email.

    Args:
        user_id (int): The user id of the user to whom the password reset email will be sent.
        password (str): Generated password that will be sent to the user
    Returns:
        Any: The return value of the send_password_reset_email function.
    """
    send_password_reset_email(user_id, password)
