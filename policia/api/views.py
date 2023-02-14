from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions


from policia.api.serializers import RegisterSerializer


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
