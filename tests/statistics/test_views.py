import os
from typing import (
    Dict,
    Optional,
)
from requests import Response

import pytest
from rest_framework.test import APIClient

from tests.conftest import get_json

current_dir = os.path.dirname(__file__)


@pytest.mark.parametrize(
    'from_, to_, sort_field, expected',
    (
            ('2020-12-31', '2021-12-31', 'id', {'status_code': 200}),
    )
)
@pytest.mark.django_db
def test_statistic_list(
        from_: str,
        to_: str,
        sort_field: Optional[str],
        expected: Dict[str, int],
        client: APIClient,
):
    path = f'/statistics/list/?from={from_}&to={to_}'
    if sort_field:
        path += f'&sort_field={sort_field}'
    response: Response = client.get(path, follow=True)
    assert response.status_code == expected['status_code']


@pytest.mark.parametrize(
    'file_name, status_code',
    (
            ('2021-01-01', 201),
    )
)
@pytest.mark.django_db
def test_create_statistic(
        file_name: str,
        status_code: int,
        client: APIClient
):
    inp = get_json(f'{current_dir}/fixture/{file_name}_in')
    response: Response = client.post('/statistics/', data=inp, content_type='application/json', follow=True)
    assert response.status_code == status_code
    otp = get_json(f'{current_dir}/fixture/{file_name}_out')
    assert response.json() == otp


@pytest.mark.parametrize(
    'date, status_code',
    (
            ('2020-12-31', 204),
            ('2020-12-40', 400),
    )
)
@pytest.mark.django_db
def test_clean_statistics(
        date: str,
        status_code: int,
        client: APIClient,
):
    path = '/statistics/clean/'
    if date:
        path += f'?date={date}'
    response: Response = client.delete(path, follow=True)
    assert response.status_code == status_code
