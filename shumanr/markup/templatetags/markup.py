from django import template
from django.conf import settings
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
def markdown2(value):
    try:
        import markdown2
    except ImportError:
        if settings.DEBUG:
            raise template.TemplateSyntaxError("Error in 'markdonw' filter: The Python markdown2 library isn't install.")
        return force_text(value)
    else:
        return mark_safe(markdown2.markdown(value,safe_mode=True,enable_attributes=False))
