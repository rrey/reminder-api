from inventory.models import Group, Host, Inventory
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
