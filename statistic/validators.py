import datetime

from rest_framework import validators

from .models import Statistic


def validate_date_string(date, date_template, date_repr, param_name):
    """
    Validate given date for date_repr
    :param date:
    :param date_template:
    :param date_repr:
    :param param_name:
    :return:
    """
    if not date:
        raise validators.ValidationError(f"Please provide valid {param_name}")
    try:
        return datetime.datetime.strptime(date, date_template)
    except ValueError:
        raise validators.ValidationError(f"Unsupported date format, use {date_repr}")


def validate_sort_field(field_name: str) -> str:
    """
    check `field_name` is exist or not in Statistic model
    :param field_name:
    :return:
    """
    if field_name in [field.name for field in Statistic._meta.get_fields()]:
        return field_name
    raise validators.ValidationError(f'You can not sort with {field_name} field')
