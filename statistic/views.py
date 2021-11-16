from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Statistic
from .serializers import StatisticCreateSerializer, StatisticListSerializer
from .validators import (
    validate_date_string,
    validate_sort_field,
)


class StatisticCreateView(ModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticCreateSerializer
    http_method_names = ['post']


class StatisticsListView(ModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticListSerializer
    http_method_names = ['get']

    def get_queryset(self):
        query_params = self.request.query_params
        from_ = validate_date_string(query_params.get('from'), "%Y-%m-%d", "YYYY-MM-DD", 'from').date()
        to_ = validate_date_string(query_params.get('to'), "%Y-%m-%d", "YYYY-MM-DD", 'to').date()
        sort_field = validate_sort_field(query_params.get('sort_field', 'date'))

        return super().get_queryset().filter(
            Q(date__gte=from_) & Q(date__lte=to_)
        ).order_by(sort_field)

    @swagger_auto_schema(
        operation_id='statistics_list',
        manual_parameters=[
            openapi.Parameter(
                'from', in_=openapi.IN_QUERY, description='from date YYYY-MM-DD', type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'to', in_=openapi.IN_QUERY, description='to date YYYY-MM-DD', type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'sort_field', in_=openapi.IN_QUERY,
                description='sort parameter', type=openapi.TYPE_STRING, default='date'
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CleanStatisticsView(ModelViewSet):
    queryset = Statistic.objects.all()
    http_method_names = ['delete']

    @swagger_auto_schema(
        operation_id='clean_statistics',
        manual_parameters=[
            openapi.Parameter(
                'date', in_=openapi.IN_QUERY, description='date YYYY-MM-DD', type=openapi.TYPE_STRING
            ),
        ]
    )
    def destroy(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        date_str: str = self.request.query_params.get('date', '')
        if date_str:
            queryset = queryset.filter(
                date=validate_date_string(date_str, "%Y-%m-%d", "YYYY-MM-DD", 'date').date()
            )
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
