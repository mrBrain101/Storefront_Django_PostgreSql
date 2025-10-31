"Run this to generate a secret key with Django built-in utility"
from django.core.management.utils import get_random_secret_key


DJANGO_SECRET_KEY = get_random_secret_key()

if __name__ == '__main__':
    with open('.env', 'w') as f:
        f.write(f'DJANGO_SECRET_KEY={DJANGO_SECRET_KEY}')