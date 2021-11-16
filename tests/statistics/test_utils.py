from datetime import date as dt
import pytest

from statistic.utils import get_random_date


@pytest.mark.parametrize(
    'start_date, end_date',
    (
            (dt(2020, 1, 1), dt(2021, 10, 1)),
            (dt(2019, 1, 12), dt(2021, 10, 13)),
            (dt(1600, 1, 1), dt(1600, 1, 1)),
    )
)
def test_get_random_date(
        start_date: dt,
        end_date: dt,
        client
):
    result = get_random_date(start_date, end_date)
    assert isinstance(result, dt)
    assert start_date <= result <= end_date
