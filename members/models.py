from django.db import models
from model_utils.models import TimeStampedModel
import uuid

from members.choices import RoleChoices


class TeamMember(TimeStampedModel):

    uuid = models.UUIDField("UUID", default=uuid.uuid4, unique=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone_no = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    role = models.CharField(choices=RoleChoices.choices, max_length=20, null=True)


    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name