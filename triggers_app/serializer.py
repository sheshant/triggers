from rest_framework import serializers

from triggers_app.models import Trigger


class TriggerDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trigger
        fields = ('id', 'identifier', 'description', 'state', 'is_active', 'environment', "meta_data")


