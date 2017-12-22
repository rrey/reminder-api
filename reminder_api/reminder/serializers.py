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


class StackDetailSerializer(serializers.ModelSerializer):
    #logo = serializers.ImageField(allow_empty_file=True)
    hosts = HostSerializer(many=True)
    urls = UrlSerializer(many=True)

    class Meta:
        model = Stack
        fields = ('id', 'name', 'urls', 'hosts', 'logo', 'category')

    def create(self, validated_data):
        hosts_data = validated_data.pop('hosts')
        urls_data = validated_data.pop('urls')
        stack = Stack.objects.create(**validated_data)
        for host in [item['hostname'] for item in hosts_data]:
            stack.hosts.create(hostname=host)
        for url in [item['url'] for item in urls_data]:
            stack.urls.create(url=url)
        return stack

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.category = validated_data.get('category', instance.category)
        # {{{ delete existing hosts and urls
        for url in instance.urls.all():
            url.delete()
        for host in instance.hosts.all():
            host.delete()
        # }}}
        hosts_data = validated_data.pop('hosts')
        urls_data = validated_data.pop('urls')
        for host in [item['hostname'] for item in hosts_data]:
            instance.hosts.create(hostname=host)
        for url in [item['url'] for item in urls_data]:
            instance.urls.create(url=url)
        return instance


class ReminderSerializer(serializers.ModelSerializer):

    stacks = StackDetailSerializer(many=True)

    class Meta:
        model = Reminder
        fields = ('id', 'stacks', )
