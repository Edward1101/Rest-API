from .models import User
from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication


class UserAuth(BaseAuthentication):
    # override authenticate method
    def authenticate(self, request):
        # get for authenticate, then can use post for login or register
        if request.method == 'GET':
            # request.query_params typoe is django QueryDict type
            token = request.query_params.get('token')
            try:
                # get token from cache
                user_id = cache.get(token)
                # match the user
                user = User.objects.get(pk=user_id)
                # return user , token
                return user, token
            except:
                return
