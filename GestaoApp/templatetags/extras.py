from django import template

register = template.Library()


@register.filter
def sub( value, arg ):
  res = 0
  if arg:
    res = arg
  if value:
    res -= value
  return res

@register.filter
def get_index(list, object):
  return list.index(object)

@register.filter
def htmlattributes(value, arg):
    attrs = value.field.widget.attrs

    data = arg.replace(' ', '')   

    kvs = data.split(',') 

    for string in kvs:
        kv = string.split(':')
        attrs[kv[0]] = kv[1]

    rendered = str(value)

    return rendered