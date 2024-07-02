# convert_filters.py

from django import template

register = template.Library()

@register.filter
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    return round(celsius, 2)
