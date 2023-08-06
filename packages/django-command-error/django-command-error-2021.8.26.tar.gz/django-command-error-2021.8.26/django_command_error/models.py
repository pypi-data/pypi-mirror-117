__all__ = ['Error']

from django.db import models


class Error(models.Model):
    app = models.TextField()
    name = models.TextField()
    sys_argv = models.TextField(null=True,verbose_name='sys.argv')
    args = models.TextField(null=True)
    options = models.TextField(null=True)

    exc_type = models.TextField(verbose_name='type')
    exc_value = models.TextField(verbose_name='value')
    exc_traceback = models.TextField(verbose_name='traceback')

    created_at = models.DateTimeField(auto_now_add=True,verbose_name='created')

    class Meta:
        db_table = 'django_command_error'
        indexes = [
           models.Index(fields=['app',]),
           models.Index(fields=['name',]),
           models.Index(fields=['exc_type',]),
           models.Index(fields=['-created_at',]),
        ]
        ordering = ('-created_at',)
