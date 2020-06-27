from rest_framework import serializers

from api.models import CheckList


class CheckListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    site = serializers.ReadOnlyField(source='site.site_url')

    class Meta:
        model = CheckList
        fields = ['name', 'site', 'notification', 'owner', 'id']
