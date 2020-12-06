from rest_framework import serializers
from logging import getLogger

from members.models import TeamMember


logger = getLogger(__name__)


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ('uuid', 'first_name', 'last_name', 'phone_no', 'email', 'role', 'is_active')
        extra_kwargs = {
            'uuid': {
                'read_only': True,
            },
            'first_name': {
                'required': True,
            },
            'last_name': {
                'required': False,
            },
            'phone_no': {
                'required': True,
            },
            'email': {
                'required': True,
            },
            'role': {
                'required': True,
            },
            'is_active': {
                'write_only': True,
            },
        }

    def to_internal_value(self, data):
        if isinstance(data.get('role'), str):
            data['role'] = data['role'].title()
        return super().to_internal_value(data)

    def validate_phone_no(self, data: str):
        if not(data.isdigit()) or len(data) != 10:
            raise serializers.ValidationError('phone_no is invalid.')
        return data

    def validate_email(self, data):
        try:
            TeamMember.objects.get(email=data)
            logger.info(f'Member with Email ID {data} already exists.')
            raise serializers.ValidationError(f'Member with Email ID {data} already exists.')
        except TeamMember.DoesNotExist:
            return data