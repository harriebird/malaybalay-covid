#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def local_config_exists():
    for p in sys.path:
        local_config = os.path.join(p, "local_settings.py")
        if os.path.exists(local_config):
            print("Found local_settings.py at {}".format(local_config))
            return True
    return False

def main():
    if os.path.exists('local_settings.py'):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'local_settings')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mccovid.settings.prod')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
