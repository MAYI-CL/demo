from django import template
register = template.Library()

@register.filter
def myupper(val):
	return val.upper()

@register.simple_tag
def jian(a,b):
	res = int(a) - int(b)
	return res