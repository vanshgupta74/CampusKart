import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campus_marketplace.settings')
django.setup()

from django.contrib.auth.models import User

username = os.environ.get('SUPERUSER_NAME')
email = os.environ.get('SUPERUSER_EMAIL')
password = os.environ.get('SUPERUSER_PASSWORD')

if username and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created!")
else:
    print("Superuser already exists or name not set.")