from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    """
    Permission check for user users.

    Allows access only to users.
    """

    def has_permission(self, request, view):
        """Check if the currently authenticated user is a user."""
        user = request.user
        return bool(
            user.type_of_user == "user"
            and user.is_active
            and request.user.is_authenticated
        )


class IsAdmin(BasePermission):
    """
    Permission check for admin users.

    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        """Check if the currently authenticated user is a user."""
        user = request.user
        return bool(
            user.type_of_user == "admin"
            and user.is_active
            and user.is_authenticated
        )


class IsAnalyst(BasePermission):
    """
    Permission check for analyst users.

    Allows access only to analyst users.
    """

    def has_permission(self, request, view):
        """Check if the currently authenticated user is an analyst."""
        user = request.user
        return bool(
            user.type_of_user == "analyst"
            and user.is_active
            and user.is_authenticated
        )
