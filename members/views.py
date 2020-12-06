from rest_framework import viewsets
from logging import getLogger

from members.models import TeamMember
from members.serializers import TeamMemberSerializer


class TeamMemberViewSet(viewsets.ModelViewSet):
    serializer_class = TeamMemberSerializer
    queryset = TeamMember.objects.filter(is_active=True)
    lookup_field = "uuid"