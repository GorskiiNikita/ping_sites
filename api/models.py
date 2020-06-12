from django.db import models


# class Site(models.Model):
#     site_id = models.AutoField(primary_key=True)
#     site_url = models.CharField(max_length=384)


class CheckList(models.Model):
    name = models.CharField(max_length=120, default=None)
    owner = models.ForeignKey('auth.User', related_name='check_list', on_delete=models.CASCADE)
    site = models.CharField(max_length=384)
    notification = models.BooleanField(default=True)
