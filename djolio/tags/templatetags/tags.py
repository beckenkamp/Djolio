from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def navactive(request, urls):
    if request.path in urls: #( reverse(url) for url in urls.split() ):
        return "active"
    return ""
