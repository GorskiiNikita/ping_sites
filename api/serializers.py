from rest_framework import serializers

from api.models import CheckList


class CheckListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CheckList
        fields = ['site', 'notification', 'owner', 'id']
