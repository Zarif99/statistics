from datetime import date, timedelta
from random import randint


def get_random_date(start_date: date, end_end: date) -> date:
    days = (end_end - start_date).days
    return start_date + timedelta(randint(0, days))
