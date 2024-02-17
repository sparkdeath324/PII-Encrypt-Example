from django.urls import path,include
from core.views import *

urlpatterns = [
    path('login/', loginView.as_view(), name='login-view'),
    path('get_data/', GetData.as_view(), name='get-data'),
    path('create_user/', CreateUser.as_view(), name='create-user'),
    
]