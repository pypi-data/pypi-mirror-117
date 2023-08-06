from datetime import date
from django.contrib import admin
from django.template.defaultfilters import linebreaksbr
from django.utils.safestring import mark_safe
from django.utils.timesince import timesince

from .models import Error

class ErrorAdmin(admin.ModelAdmin):
    list_display = ['id','app','name','sys_argv','args','options_html','exc','traceback','strftime','timesince']
    list_filter = ('app', 'name', 'exc_type')
    search_fields = ('app', 'name', 'exc_type', 'exc_value', 'exc_traceback')

    def options_html(self,e):
        return mark_safe(linebreaksbr(e.options)) if e.options else None
    options_html.short_description = 'options'

    def exc(self,e):
        return ': '.join(filter(None,[e.exc_type,e.exc_value])) if e.exc_type else None
    exc.short_description = 'exc'

    def traceback(self,e):
        return mark_safe(linebreaksbr(e.exc_traceback)) if e.exc_traceback else None
    traceback.short_description = 'traceback'

    def strftime(self, obj):
        datetime_format = '%H:%M:%S' if obj.created_at.date()==date.today() else '%Y-%m-%d'
        return obj.created_at.strftime(datetime_format)
    strftime.short_description = 'time'

    def timesince(self, error):
        return timesince(error.created_at).split(',')[0]+' ago' if error.created_at else None
    timesince.short_description = ''

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Error, ErrorAdmin)
