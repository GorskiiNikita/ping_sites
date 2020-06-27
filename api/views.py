from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import CheckList
from api.permissions import IsOwner
from api.serializers import CheckListSerializer
from rest_framework import viewsets

from .models import Site


class CheckListViewSet(viewsets.ModelViewSet):
    queryset = CheckList.objects.all()
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        # Сохранить соответствующий сайт из sites
        # Если там такого сайта нет - создать и тогда сохранить его
        site = Site.objects.all()[0]
        serializer.save(owner=self.request.user, site=site)

    def list(self, request, *args, **kwargs):
        queryset = CheckList.objects.filter(owner=request.user)
        serializer = CheckListSerializer(queryset, many=True)
        return Response({'data': serializer.data})


