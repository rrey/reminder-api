from reminder.models import Reminder, Stack, StackSection, Host, Url
from rest_framework import serializers


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = ('name', )


class HostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Host
        fields = ('name', )


class StackSectionSerializer(serializers.ModelSerializer):
    hosts = HostSerializer()
    urls = UrlSerializer()

    class Meta:
        model = StackSection
        fields = ('name', 'hosts', 'urls')


class StackSerializer(serializers.ModelSerializer):
    #logo = serializers.ImageField(allow_empty_file=True)
    sections = StackSectionSerializer()

    class Meta:
        model = Stack
        fields = ('name', 'logo', 'sections')


class ReminderSerializer(serializers.ModelSerializer):

    stacks = StackSerializer()

    class Meta:
        model = Reminder
        fields = ('name', 'stacks',)
