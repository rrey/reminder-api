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

    class Meta:
        model = StackSection
        fields = ('id', 'name', )


class StackSectionDetailSerializer(serializers.ModelSerializer):
    hosts = HostSerializer(many=True)
    urls = UrlSerializer(many=True)

    class Meta:
        model = StackSection
        fields = ('id', 'name', 'hosts', 'urls')


class StackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stack
        fields = ('reminder', 'id', 'name', )

class StackDetailSerializer(serializers.ModelSerializer):
    #logo = serializers.ImageField(allow_empty_file=True)
    sections = StackSectionDetailSerializer(many=True)

    class Meta:
        model = Stack
        fields = ('id', 'name', 'sections')


class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = ('environment', 'id', )


class ReminderSerializer(serializers.ModelSerializer):

    stacks = StackDetailSerializer(many=True)

    class Meta:
        model = Reminder
        fields = ('id', 'stacks', )
