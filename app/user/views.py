"""
Views for the user API.
"""
# access base classes/methods django uses to create objects to override them
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


# CreateAPIView handes post req, just need to define serializer
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):  # customize default view
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer  # pass in our custom serialzer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES  # allows browsable api on new view


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]  # make user user is authentiated to use api

    def get_object(self):  # override get method
        """Retrieve and return teh authenticated user."""
        return self.request.user
