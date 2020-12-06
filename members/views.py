from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from logging import getLogger

from members.models import TeamMember
from members.serializers import TeamMemberSerializer


logger = getLogger(__name__)


class TeamMemberViewSet(viewsets.ModelViewSet):
    serializer_class = TeamMemberSerializer
    queryset = TeamMember.objects.all()
    lookup_field = "uuid"

