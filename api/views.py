import json

from django.db.models import Count
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import CheckList
from api.permissions import IsOwner
from api.serializers import CheckListSerializer
from api.tasks import ping_site
from rest_framework import viewsets

from .models import Site


class CheckListViewSet(viewsets.ModelViewSet):
    queryset = CheckList.objects.all()
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        site_url = self.request.POST['site']
        site, created_site = Site.objects.get_or_create(site_url=site_url)
        serializer.save(owner=self.request.user, site=site)
        if created_site:
            schedule, created_schedule = IntervalSchedule.objects.get_or_create(every=30, period=IntervalSchedule.SECONDS)
            PeriodicTask.objects.create(interval=schedule,
                                        task='api.tasks.ping_site',
                                        name=f'id{site.site_id}',
                                        args=json.dumps([site.site_id]))
            ping_site.delay(site.site_id)

    def perform_update(self, serializer):
        site_url = self.request.POST['site']
        site, created = Site.objects.get_or_create(site_url=site_url)
        serializer.save(owner=self.request.user, site=site)

    def perform_destroy(self, instance):
        site = Site.objects.get(site_id=instance.site.site_id)
        list_checks = CheckList.objects.filter(site__site_id=site.site_id)

        if len(list_checks) <= 1:
            site.delete()
            PeriodicTask.objects.get(name=f'id{instance.site.site_id}').delete()

        instance.delete()

    def list(self, request, *args, **kwargs):
        queryset = CheckList.objects.filter(owner=request.user)
        serializer = CheckListSerializer(queryset, many=True)
        return Response({'data': serializer.data})


