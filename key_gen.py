import subprocess
from django.core.management.utils import get_random_secret_key


def set_key() -> None:
    key = get_random_secret_key()
    subprocess.run(f"export DJANGO_KEY='{key}'", shell=True)


if __name__ == "__main__":
    set_key()
