from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='replacer')
@stringfilter #indicates it takes only string
def cut(value,unwantedValue):
    return value.replace(unwantedValue,'');

# register.filter('cutter', cut)
