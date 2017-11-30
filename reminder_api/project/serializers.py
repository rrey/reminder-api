from project.models import Project, Environment
from rest_framework import serializers

from reminder.serializers import ReminderSerializer
from inventory.serializers import InventorySerializer


class EnvironmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Environment
        fields = ('project', 'id', 'name', )


class EnvironmentDetailSerializer(serializers.ModelSerializer):

    reminder = ReminderSerializer()
    inventory = InventorySerializer()

    class Meta:
        model = Environment
        fields = ('id', 'name', 'reminder', 'inventory', )


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', )

class ProjectDetailSerializer(serializers.ModelSerializer):

    environments = EnvironmentSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'environments', )
