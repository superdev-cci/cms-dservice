from django.contrib.auth.models import User, Group

from branch.models import Branch
from rest_framework import serializers
from ..models import UserAccount
import datetime


class UserAuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'email', 'groups',)
        extra_kwargs = {'password': {'write_only': True},
                        'email': {'required': False}
                        }

    def create(self, validated_data):
        user = super(UserAuthenticationSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_internal_value(self, data):
        data['groups'] = data.pop('group')
        return data


class UserSerializer(serializers.ModelSerializer):
    # group = serializers.SerializerMethodField('get_group_name')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'last_login',
                  'is_staff', 'is_active', 'is_superuser', 'groups',)
        extra_kwargs = {'password': {'write_only': True},
                        'email': {'required': False},
                        'first_name': {'required': False},
                        'last_name': {'required': False},
                        'last_login': {'read_only': False},
                        'is_staff': {'required': False},
                        'is_active': {'read_only': False},
                        'is_superuser': {'read_only': False},
                        'groups': {'required': False},
                        }

    def get_group_name(self, obj):
        group_name = 'Member'
        if hasattr(obj, 'groups'):
            groups = obj.groups.all()
            if len(groups) is not 0:
                group_name = groups[0].name
        return group_name

    def get_staff_branch(self, obj):
        if obj.useraccount.staff is not None:
            return obj.useraccount.staff.code
        else:
            return None

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)

        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_internal_value(self, data):
        new_data = {**data}
        groups = Group.objects.get(name=data.get('group', None))
        new_data.pop('branch')
        new_data.pop('group')
        new_data['groups'] = [groups.id, ]
        return new_data

    def update(self, instance, validated_data):
        instance = super(UserSerializer, self).update(instance, validated_data)
        raw_data = self.context['request'].data
        branch = Branch.objects.get(code=raw_data['branch'])
        instance.useraccount.staff = branch
        instance.useraccount.save()
        return instance

    def to_representation(self, instance):
        data = super(UserSerializer, self).to_representation(instance)
        data['group'] = self.get_group_name(instance)
        data.pop('groups', None)
        if instance.last_login:
            data['last_login'] = instance.last_login.strftime('%H:%M:%S %d/%m/%Y')

        if instance.useraccount.member is not None:
            member = instance.useraccount.member
            # if member.mirror:
            #     data['first_name'] = member.person.mirror.name
            #     data['last_name'] = member.person.mirror.surname
        return data


class UserInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # member = MemberInfoSerializer()
    staff = serializers.SerializerMethodField('get_staff_branch')

    class Meta:
        model = UserAccount
        fields = ('id', 'user', 'member', 'staff')

    def get_staff_branch(self, obj):
        if obj.staff is not None:
            return obj.staff.code
        else:
            return None

    def create(self, validated_data):
        instance = super(UserInfoSerializer, self).create(validated_data)
        raw_data = self.context['request'].data
        branch = Branch.objects.get(code=raw_data['branch'])
        instance.staff = branch
        instance.set_password(validated_data['user']['password'])
        return instance
