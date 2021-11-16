from django.urls import path

from .views import (
    StatisticCreateView,
    StatisticsListView,
    CleanStatisticsView,
)


urlpatterns = [
    path('list/', StatisticsListView.as_view({'get': 'list'})),
    path('clean/', CleanStatisticsView.as_view({'delete': 'destroy'})),
    path('', StatisticCreateView.as_view({'post': 'create'}))
]
