from account.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import permissions, viewsets


class GroupViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
