from django import template
from django.core.files.storage import default_storage

register = template.Library()

@register.filter(name='image_exists')
def image_exists(fp):
    try:
        print default_storage.exists("leif.jpeg")
        print default_storage.exists(fp)
    except:
        pass
    return False
    #return default_storage.exists(fp)