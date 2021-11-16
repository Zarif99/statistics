import pytest
from statistic.models import Statistic


@pytest.mark.django_db
def test_fixture(client):
    assert Statistic.objects.all().count() == 1000
