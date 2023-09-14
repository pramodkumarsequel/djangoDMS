from django import template
from decimal import Decimal
from django.db.models.fields.related import ForeignKey,ManyToOneRel
register = template.Library()

@register.filter
def is_decimal(value):
    try:
        Decimal(value)
        return True
    except (ValueError, TypeError):
        return False
    
@register.filter
def get_attribute(obj, attr):
    value = getattr(obj, attr, None)
    if attr == "isactive":
        return ''
    return value


@register.filter
def break_loop(value):
    raise StopIteration


@register.filter(name='zip')
def zip_lists(a, b):
  return zip(a, b)


# @register.filter(name='get_item_fields')
# def get_item_fields(item):
#     return [(field.verbose_name, getattr(item, field.name)) for field in item._meta.fields]