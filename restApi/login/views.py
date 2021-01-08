from django.shortcuts import render

# Create your views here.
import jwt, json
from rest_framework import views
from rest_framework.response import Response
# from models import User
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import JsonResponse
# from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import status,exceptions
from rest_framework.response import Response
from django.db import connection


class Login(views.APIView):

        def post(self, request, *args, **kwargs):
            with connection.cursor() as cursor:
                if not request.data:
                    return Response({'Error': "Please provide username/password"}, status="400")

                username = request.data['username']
                password = request.data['password']
                try:

                      user = """SELECT id,email,username FROM auth_user WHERE username='{username}' AND password={password}"""
                      sql_command = user.format(username=username, password=password)
                      data = cursor.execute(sql_command)
                      userData = cursor.fetchone()

                      print('userdata',userData)
                      payload = {
                          'id': userData[0],
                          'email': userData[1],
                      }
                      print(payload)
                      if payload:
                          jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
                          print(jwt_token)
                          return Response(data={
                              'token': jwt_token,
                              'username': userData[2]
                          }, status=status.HTTP_200_OK)
                      else:
                          return Response({'Error': "Invalid credentials"}, status=400, content_type="application/json")
                except:
                    return Response({'Error': "Invalid username/password"}, status="400")

        # class TokenAuthentication(BaseAuthentication):
        #
        #     model = None
        #
        #     def get_model(self):
        #         return User
        #
        #     def authenticate(self, request):
        #         auth = get_authorization_header(request).split()
        #         if not auth or auth[0].lower() != b'token':
        #             return None
        #
        #         if len(auth) == 1:
        #             msg = 'Invalid token header. No credentials provided.'
        #             raise exceptions.AuthenticationFailed(msg)
        #         elif len(auth) > 2:
        #             msg = 'Invalid token header'
        #             raise exceptions.AuthenticationFailed(msg)
        #
        #         try:
        #             token = auth[1]
        #             if token == "null":
        #                 msg = 'Null token not allowed'
        #                 raise exceptions.AuthenticationFailed(msg)
        #         except UnicodeError:
        #             msg = 'Invalid token header. Token string should not contain invalid characters.'
        #             raise exceptions.AuthenticationFailed(msg)
        #
        #         return self.authenticate_credentials(token)
        #
        #     def authenticate_credentials(self, token):
        #         model = self.get_model()
        #         payload = jwt.decode(token, "SECRET_KEY")
        #         email = payload['email']
        #         userid = payload['id']
        #         msg = {'Error': "Token mismatch", 'status': "401"}
        #         try:
        #
        #             user = User.objects.get(
        #                 email=email,
        #                 id=userid,
        #                 is_active=True
        #             )
        #
        #             if not user.token['token'] == token:
        #                 raise exceptions.AuthenticationFailed(msg)
        #
        #         except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
        #             return HttpResponse({'Error': "Token is invalid"}, status="403")
        #         except User.DoesNotExist:
        #             return HttpResponse({'Error': "Internal server error"}, status="500")
        #
        #         return (user, token)
        #
        #     def authenticate_header(self, request):
        #         return 'Token'






        # else:

