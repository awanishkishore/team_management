from djchoices import DjangoChoices, C


class RoleChoices(DjangoChoices):
    ADMIN = C('Admin')
    REGULAR = C("Regular")