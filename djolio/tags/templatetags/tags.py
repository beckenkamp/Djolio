from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def navactive(request, urls):
    if request.path in urls: #( reverse(url) for url in urls.split() ):
        return "active"
    return ""

#from django.conf import settings # import the settings file
#allows settings constant to be used on template
#@register.tag
#def value_from_settings(parser, token):
#    try:
#        # split_contents() knows not to split quoted strings.
#        tag_name, var = token.split_contents()
#    except ValueError:
#        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]
#    return ValueFromSettings(var)
#
#class ValueFromSettings(template.Node):
#    def __init__(self, var):
#        self.arg = template.Variable(var)
#    def render(self, context):        
#        return settings.__getattr__(str(self.arg))
