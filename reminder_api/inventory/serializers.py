from inventory.models import Project, Group, Host, Inventory
from rest_framework import serializers


class HostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Host
        fields = ('name', )


class GroupSerializer(serializers.ModelSerializer):

    hosts = HostSerializer(many=True)

    class Meta:
        model = Group
        fields = ('name', 'hosts')


class InventorySerializer(serializers.ModelSerializer):

    groups = GroupSerializer(many=True)

    class Meta:
        model = Inventory
        fields = ('name', 'groups')


class ProjectSerializer(serializers.ModelSerializer):

    inventory = InventorySerializer(many=True)

    class Meta:
        model = Project
        fields = ('name', 'inventory')

    def create(self, validated_data):
        inventory = validated_data.pop('inventory')
        project = Project.objects.create(**validated_data)
        project.save()
        if inventory:
            for item in inventory:
                project.inventory.create(**item)
        return project
