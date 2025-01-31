from django.core.management import BaseCommand
from django.contrib.auth.models import User, Group, Permission

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(pk=6)

        group, _ = Group.objects.get_or_create(
            name='managers'
        )

        permission_profile = Permission.objects.get(
            codename='view_profile'
        )
        permission_log = Permission.objects.get(
            codename='view_logentry'
        )
        # Добавление разрешенияч для группы
        group.permissions.add(permission_profile)
        # Добавления юзера в группу
        user.groups.add(group)
        #  Связать юзера на прямую
        user.user_permissions.add(permission_log)
        
        group.save()
        user.save()