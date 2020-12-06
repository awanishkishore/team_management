from rest_framework import serializers
from rest_framework.exceptions import APIException
from logging import getLogger
from django.http import Http404


class TeamMemberSerializer(serializers.ModelSerializer):
    pass