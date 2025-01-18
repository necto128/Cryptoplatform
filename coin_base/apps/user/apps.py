from django.apps import AppConfig


class UserConfig(AppConfig):
    """User app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.user"

    def ready(self):
        """Ready Option."""
        import apps.user.signals # noqa: F401
