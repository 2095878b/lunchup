from django import template
from django.core.files.storage import default_storage

register = template.Library()

@register.filter(name='image_exists')
def image_exists(fp):
    try:
        return default_storage.exists(fp)
    except:
        return False
    #return default_storage.exists(fp)