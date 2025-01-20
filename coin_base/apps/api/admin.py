from django.contrib import admin


class CustomAdminSite(admin.AdminSite):
    """Custom admin site."""

    def has_permission(self, request):
        """Func for checking if the user has permission to access the admin site."""
        return request.user.is_active


admin_site = CustomAdminSite(name='custom_admin')
