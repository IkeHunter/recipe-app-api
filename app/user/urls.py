"""
URL mappings for the user API.
"""
from django.urls import path

from user import views


app_name = 'user'

"""
path arg1: defines the endpoint that will be handled by the specifications
path arg2: pass in the view that will handle req, django expects fn so as_view
    converts view to necessary format
path arg3: allows for "reverse lookup", ie user:create
"""
urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]

