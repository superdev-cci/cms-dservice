from account.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework.response import Response
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import permission_classes, action

from core.pagination import StandardResultsSetPagination
from ..models import UserAccount
from ..serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAdminUser, TokenHasReadWriteScope]
    queryset = UserAccount.objects.filter(member__isnull=True)
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination

    @action(detail=True, methods=['PUT'], )
    def password(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.set_password(request.data['password'])
            instance.save()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)
