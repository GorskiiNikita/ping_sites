from django.db import models


class Site(models.Model):
    site_id = models.AutoField(primary_key=True)
    site_url = models.CharField(max_length=384)
    is_active = models.BooleanField(default=False)


class CheckList(models.Model):
    name = models.CharField(max_length=120, default=None)
    owner = models.ForeignKey('auth.User', related_name='check_list_owner', on_delete=models.CASCADE)
    site = models.ForeignKey(Site, related_name='check_list_site', on_delete=models.CASCADE)
    notification = models.BooleanField(default=True)
