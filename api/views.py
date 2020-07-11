import json

from django_celery_beat.models import IntervalSchedule, PeriodicTask
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
        if created:
            schedule, created = IntervalSchedule.objects.get_or_create(every=10, period=IntervalSchedule.SECONDS)
            PeriodicTask.objects.create(interval=schedule,
                                        task='api.tasks.ping_site',
                                        name=f'id{site.site_id}',
                                        args=json.dumps([site.site_id]))

    def perform_update(self, serializer):
        site_url = self.request.POST['site']
        site, created = Site.objects.get_or_create(site_url=site_url)
        serializer.save(owner=self.request.user, site=site)

    def list(self, request, *args, **kwargs):
        queryset = CheckList.objects.filter(owner=request.user)
        serializer = CheckListSerializer(queryset, many=True)
        return Response({'data': serializer.data})


