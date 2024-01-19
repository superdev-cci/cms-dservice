from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ..serializers import MemberDiscountSerializer
from ..models import MemberDiscount
from member.models import Member

# Not variable for now
class MemberDiscountView(viewsets.ModelViewSet):
    queryset = MemberDiscount.objects.all()
    serializer_class = MemberDiscountSerializer

    def create(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['GET'])
    def get_discount(self, request, *args, **kwargs):
        data = request.query_params
        mem_code = data.get('member', None)
        queryset = MemberDiscount.objects.filter(member_id=Member.objects.get(mcode=mem_code).id)
        result = MemberDiscountSerializer(queryset, many=True).data
        print(result)
        return Response(result, status.HTTP_200_OK)
