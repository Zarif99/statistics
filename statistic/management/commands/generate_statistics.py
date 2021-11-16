from decimal import Decimal
from random import randint
from datetime import date
from django.core.management.base import BaseCommand
from statistic.models import Statistic
from statistic.utils import get_random_date


class Command(BaseCommand):
    help = 'Generates random statistics'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            nargs='?',
            help='Generate count statistic'
        )

    def handle(self, *args, **options):
        count = options['count']
        i = 0
        while i < count:
            step = min(count - i, 1000)
            Statistic.objects.bulk_create([
                Statistic(
                    date=get_random_date(date(1500, 1, 1), date(2500, 1, 1)),
                    views=randint(0, 10 ** 10),
                    clicks=randint(0, 10 ** 10),
                    cost=Decimal(
                        "%.2f" % Decimal(f'{str(randint(0, 10 ** 9))}.{str(randint(0, 99))}')
                    )
                )
                for _ in range(step)
            ])

            i += step
        self.stdout.write(self.style.SUCCESS(f"Successfully generated {count} statistics"))
