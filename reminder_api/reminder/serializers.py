from reminder.models import Reminder, Stack, Host, Url
from rest_framework import serializers


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = ('url', )


class HostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Host
        fields = ('hostname', )


class StackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stack
        fields = ('reminder', 'id', 'name', )

class StackDetailSerializer(serializers.ModelSerializer):
    #logo = serializers.ImageField(allow_empty_file=True)
    hosts = HostSerializer(many=True)
    urls = UrlSerializer(many=True)

    class Meta:
        model = Stack
        fields = ('id', 'name', 'urls', 'hosts', )


class ReminderSerializer(serializers.ModelSerializer):

    stacks = StackDetailSerializer(many=True)

    class Meta:
        model = Reminder
        fields = ('id', 'stacks', )
