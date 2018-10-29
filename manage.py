#!/usr/bin/env python
import os
import subprocess
import sys

if __name__ == "__main__":
    argv = sys.argv
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
    if argv[1] == 'build':
        p = subprocess.Popen('yarn build', cwd=os.path.join(os.path.dirname(__file__), 'frontend'), shell=True)
        p.wait()
        argv[1] = 'collectstatic'
        print("\033[1;35m " + "Please input 'yes'!" + "\033[0m")
    else:
        if os.environ.get('IS_VUE_RUN') != '1' and (argv[1] == 'runserver' or argv[1] == 'serve'):
            subprocess.Popen('yarn serve', cwd=os.path.join(os.path.dirname(__file__), 'frontend'), shell=True)
            os.environ.setdefault("IS_VUE_RUN", '1')
        if argv[1] == 'serve':
            argv[1] = 'runserver'
            argv.append('8000')
            print(" ".join(argv))
    execute_from_command_line(argv)
