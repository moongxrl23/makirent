#!/usr/bin/env python
"""Punto de entrada para comandos de Django (runserver, migrate, etc.)."""
import os, sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arriendos.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
