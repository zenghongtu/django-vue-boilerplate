#!/usr/bin/env python
import os
import subprocess
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings.dev")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is reall:y that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    if os.environ.get('IS_VUE_RUN') != '1' and sys.argv[1] == 'runserver':
        subprocess.Popen('yarn serve', cwd=os.path.join(os.path.dirname(__file__), 'frontend'), shell=True)
        os.environ.setdefault("IS_VUE_RUN", '1')
    execute_from_command_line(sys.argv)