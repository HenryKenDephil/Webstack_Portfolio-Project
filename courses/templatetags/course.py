from django import template

'''creating template filter to allow
retrieving attributes/variables using underscore
that is prevented by django template'''

register = template.Library.register()

@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None