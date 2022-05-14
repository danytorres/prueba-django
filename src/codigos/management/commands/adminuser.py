import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        django_admin_user = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        django_admin_email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        django_admin_password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
        user = get_user_model()
        admin = user.objects.filter(username=django_admin_user)
        if len(admin) == 0:
            user.objects.create_superuser(django_admin_user, django_admin_email, django_admin_password)
            print("usuario creado")
        else:
            print("usuario ya existe")