from datetime import date as dt
import pytest

from statistic.validators import validate_date_string, validate_sort_field


@pytest.mark.parametrize(
    'date, date_template, date_repr, param_name, expected',
    (
            ('2021-01-01', '%Y-%m-%d', 'YYYY-MM-DD', 'from', dt(2021, 1, 1)),
            ('2021-12-31', '%Y-%m-%d', 'YYYY-MM-DD', 'to', dt(2021, 12, 31)),
    )
)
def test_validate_date_string(
        date: str,
        date_template: str,
        date_repr: str,
        param_name: str,
        expected: dt,
        client
):
    assert validate_date_string(date, date_template, date_repr, param_name).date() == expected


@pytest.mark.parametrize(
    'field_name,expected',
    (
            ('id', 'id'),
            ('clicks', 'clicks'),
            ('views', 'views'),
            ('cost', 'cost')
    )
)
def test_validate_sort_field(
        field_name: str,
        expected: bool,
        client
):
    assert validate_sort_field(field_name) == expected
