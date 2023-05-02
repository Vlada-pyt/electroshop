from rest_framework.permissions import BasePermission


class IsEmployeeActive(BasePermission):
    def has_permission(self, request, view):
        message = "Вы не имеете доступа"
        user = request.user
        if user.is_active == True:
            return True
        return message

