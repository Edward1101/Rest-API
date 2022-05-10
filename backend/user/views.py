from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework import status, exceptions

from rest_framework.response import Response
from cfehome.settings import SUPER_USER
from.constants import HTTP_ACTION_LOGIN,HTTP_ACTION_REGISTER
import uuid
from django.core.cache import cache
from .auth import UserAuth
from .permissions import IsSuperUser

# ListCreateAPIView
# get all user
class UsersAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # authentication_classes
    authentication_classes = (UserAuth,)
    # permission_class
    permission_classes = (IsSuperUser,)


    # def get(self, request, *args, **kwargs):
    #     if isinstance(request.user, User):
    #         return self.list(request, *args, **kwargs)
    #     else:
    #         raise exceptions.NotAcceptable

    # handle register and login, use action to separate
    def post(self, request, *args, **kwargs):
        action = request.query_params.get('action')
        print(f"get action is {action}")
        # register
        if action == HTTP_ACTION_REGISTER:
            print(f"going to create")
            return self.create(request, *args, **kwargs)

        # login
        elif action == HTTP_ACTION_LOGIN:
            user_name = request.data.get('user_name')

            user_password = request.data.get('user_password')
            print(f"user name is {user_name}")
            print(f"user password is {user_password}")
            try:
                user = User.objects.get(user_name=user_name)
                print(f"get user is {user}, user password is {user.user_password}")
                if user.user_password == user_password:
                    # get mark
                    print(f" ###in create token")
                    token = uuid.uuid4().hex
                    # save to cache
                    # cache.set(key, value)
                    print(f"token is {token}")
                    cache.set(token, user.id)
                    print(f" set cache done ")
                    data = {
                        'msg': 'login success',
                        'status': 200,
                        'token': token,
                    }

                    return Response(data)
                else:
                    # authentication failed
                    raise exceptions.AuthenticationFailed
            # user not found
            except User.DoesNotExist:
                # raise error
                print("not found error")
                raise exceptions.NotFound
        # action not list
        else:
            # ValidationError
            print(f"valid error")
            raise exceptions.ValidationError

    def create(self, request, *args, **kwargs):
        # print(f"creating")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data = serializer.data
        user_name = data.get("user_name")
        # print(f"data is {data}")
        # print(f"user name is {user_name}")

        # set superuser account
        if user_name in SUPER_USER:
            user_id = data.get('id')
            user = User.objects.get(pk=user_id)
            user.is_super = True
            user.save(is_super=True)
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


# get single user
class UserAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


