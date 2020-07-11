from django import template
register = template.Library()

# @register.filter(name='cut') You can also use
def cut(value,arg):
    return value.replace(arg,'')


register.filter('cut',cut)
