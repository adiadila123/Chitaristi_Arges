# myapp/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='truncate_chars')
def truncate_chars(value, arg):
    try:
        length = int(arg)
    except ValueError:
        return value
    if len(value) > length:
        return value[:length] + '...'
    return value
