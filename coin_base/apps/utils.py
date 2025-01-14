from celery import current_app as celery_app
from passlib.pwd import genword


def ping_celery_redis(app):
    """Checking if a celery + redis connection is active."""
    # Get status - Celery worker
    app_celery = app.control
    celery_status = app_celery.ping()
    # Check Celery worker
    assert bool(celery_status)
    celery_app.connection().heartbeat_check()


def generate_password():
    """Generate password."""
    return genword()
