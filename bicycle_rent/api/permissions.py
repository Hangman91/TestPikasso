from rest_framework import permissions


class UserHasNoBicycle(permissions.BasePermission):
    """пермиссион для вью функций аренды если пользователь СВОБОДЕН"""

    def has_permission(self, request, view):
        """Доступ только свободному юзверю"""

        return (
            request.user.rent_now == False
        )


class UserHasBicycle(permissions.BasePermission):
    """пермиссион для вью функций аренды если пользователь ЗАНЯТ"""

    def has_permission(self, request, view):
        """Доступ только свободному юзверю"""

        return (
            request.user.rent_now == True
        )