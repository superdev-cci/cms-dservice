from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.authentication.legacy import BasicAuthDefault
from core.pagination import AdaptivePagination
from ..models import NoticeInformation
from ..serializers import NoticeInformationSerializer


class NoticeInformationView(viewsets.ModelViewSet):
    queryset = NoticeInformation.objects.all().order_by('-dates')
    serializer_class = NoticeInformationSerializer
    filter_backends = (SearchFilter,)
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)
    pagination_class = AdaptivePagination

    def retrieve(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)
