from project.models import Project, Environment
from rest_framework import serializers


class EnvironmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Environment
        fields = ('name', )


class EnvironmentDetailSerializer(serializers.ModelSerializer):

#    inventory = InventorySerializer()
#    reminder = ReminderSerializer()

    class Meta:
        model = Environment
        fields = ('name', )


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('name', )

class ProjectDetailSerializer(serializers.ModelSerializer):

    environments = EnvironmentSerializer(many=True)

    class Meta:
        model = Project
        fields = ('name', 'environments', )
