from django.db import models
from django.utils.translation import gettext_lazy as _


class Statistic(models.Model):
    date = models.DateField(_('Дата события'))
    views = models.BigIntegerField(_('Количество просмотров'), blank=True, default=0)
    clicks = models.BigIntegerField(_('Количество кликов'), blank=True, default=0)
    cost = models.DecimalField(_('Стоимость кликов'), max_digits=11, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = _('Статистика')
        verbose_name_plural = _('Статистики')

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')
