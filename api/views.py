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
        site_url = self.request.POST['site']
        site, created = Site.objects.get_or_create(site_url=site_url)
        serializer.save(owner=self.request.user, site=site)

    def perform_update(self, serializer):
        site_url = self.request.POST['site']
        site, created = Site.objects.get_or_create(site_url=site_url)
        serializer.save(owner=self.request.user, site=site)

    def list(self, request, *args, **kwargs):
        queryset = CheckList.objects.filter(owner=request.user)
        serializer = CheckListSerializer(queryset, many=True)
        return Response({'data': serializer.data})


