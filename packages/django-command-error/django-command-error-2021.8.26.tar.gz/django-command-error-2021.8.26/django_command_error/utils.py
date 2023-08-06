import traceback

from django.core.management import get_commands
from django.core.management.base import CommandError

def getapp(name):
    try:
        return get_commands()[name]
    except KeyError:
        raise CommandError("Unknown command: %r" % name)

def getinstance(command):
    if isinstance(command,str):
        app, name = getapp(command), command
        return load_command_class(app,name)
    return command
