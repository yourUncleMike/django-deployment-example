from django import template

register = template.Library()

@register.filter(name="censor")
def my_censor_fn(value, arg):
    """
    This replaces all occurrences of "arg" in value with "*".
    """
    return value.replace(arg, '*')

# register.filter('censor', my_censor_fn)
