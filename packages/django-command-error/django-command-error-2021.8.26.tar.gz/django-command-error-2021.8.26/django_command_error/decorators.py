import logging
import sys
import traceback

from .models import Error
from .utils import getinstance

def command_error(f):
    def wrapper(command,*args,**options):
        instance = getinstance(command)
        module_name = type(instance).__module__
        app, name = module_name.split('.')[-4], module_name.split('.')[-1]
        try:
            return instance.handle(*args, **options)
        except Exception as e:
            Error(
                app=module_name.split('.')[-4],
                name=module_name.split('.')[-1],
                sys_argv = ' '.join(sys.argv),
                args = ' '.join(args) if args else None,
                options = "\n".join(sorted(
                    map(lambda kv:'%s=%s' % (kv[0],kv[1]),filter(lambda kv:kv[1]!=None,options.items()))
                )),
                exc_type='.'.join(filter(None,[type(e).__module__,type(e).__name__])),
                exc_value=str(e),
                exc_traceback='\n'.join(traceback.format_tb(e.__traceback__))
            ).save()
            logging.error(e)
            raise e
    return wrapper if f else None
