from decimal import Decimal

from rest_framework import serializers

from .models import Statistic


class StatisticCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'


class StatisticListSerializer(serializers.ModelSerializer):
    cpc = serializers.SerializerMethodField(method_name='get_cpc')
    cpm = serializers.SerializerMethodField(method_name='get_cpm')

    class Meta:
        model = Statistic
        fields = '__all__'

    @staticmethod
    def get_cpc(obj: Statistic) -> Decimal:
        """
        :param obj:
        :return:
        """
        try:
            return Decimal("%.2f" % (obj.cost / Decimal(obj.clicks)))
        except ZeroDivisionError:
            return Decimal("0.00")

    @staticmethod
    def get_cpm(obj: Statistic) -> Decimal:
        """
        :param obj:
        :return:
        """
        try:
            return Decimal("%.2f" % ((obj.cost / Decimal(obj.clicks)) * 1000))
        except ZeroDivisionError:
            return Decimal("0.00")
