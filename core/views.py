from core.models import *
from django.db.models import Q
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from core.utils import *

# Create your views here.

class loginView(APIView):
    
    def post(self,request):
        mobile_no = request.data['mobile_no']
        password = request.data['password']
        return_data = {}
        print(mobile_no,password)
        try:
            user = User.objects.get(contact_no=mobile_no)

            authuser = authenticate(username=user.username,password=password)
            if authuser is not None:
                refresh = RefreshToken.for_user(user)
                return_data['token'] = str(refresh.access_token)
                return_data['Message'] = "Login Successful"
                return Response(status=status.HTTP_200_OK,data=return_data)
            else:
                return_data['Message'] = "Credentials are Wrong"
                return Response(status=status.HTTP_404_NOT_FOUND,data=return_data)
        except:
            return_data['Message'] = "User Not Found."
            return Response(status=status.HTTP_404_NOT_FOUND,data=return_data)
        
class GetData(APIView):
    permissions = [permissions.IsAuthenticated]

    def get(self,request):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        context = {}
        context['address'] = decryptdata(user.address)
        context['address1']= decryptdata(user.address1)
        context['address2']= decryptdata(user.address2)
        return Response(status=status.HTTP_404_NOT_FOUND,data=context)

class CreateUser(APIView):

    def post(self,request):
        contact_no = request.data['contact_no']
        try:
            user = User.objects.get(contact_no = contact_no)
            return Response(status=status.HTTP_200_OK,data={
                "Message":"User Already Exists"
            })
        except:
            user = User(
                first_name = request.data['first_name'],
                last_name = request.data['last_name'],
                contact_no = contact_no,
                email = request.data['email'],
                address = encryptdata(request.data['address']),
                address1 = encryptdata(request.data['address1']),
                address2 = encryptdata(request.data['address2']),
                username = request.data['email'],
                address_text = request.data['address_text']
            )
            user.set_password(request.data['password'])
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        