from .models import User
from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    def has_permission(self, request, view):
        # get for permission
        if request.method == 'GET':
            if isinstance(request.user, User):
                # print(f"in IsUser check {request.user.user_name}, {request.user.user_password}")
                print(User.objects.get(user_name=request.user.user_name))

                try:
                    temp_user = User.objects.get(user_name=request.user.user_name)
                    if temp_user.id == request.user.id:
                        print('user have permission')
                except:
                    return False
                return True
            return False
        return True
