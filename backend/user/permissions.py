from .models import User
from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        # get for permission
        if request.method == 'GET':
            print(request.user)
            if isinstance(request.user, User):
                print(f"{request.user.user_name}, {request.user.user_password}")
                print(request.user.is_super)
                return request.user.is_super
            return False
        return True
