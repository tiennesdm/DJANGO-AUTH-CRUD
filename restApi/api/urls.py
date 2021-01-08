from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BookAPIView, DetailView,SQLRAWQUERY,MatPlotLib


urlpatterns = [
path('', BookAPIView.as_view()),
path('<int:pk>/', DetailView.as_view()),
path('rawSQL',  SQLRAWQUERY.raw_SQL),
path('plot',MatPlotLib.pandaView)
    # path('hello/', HelloView.as_view(), name='hello'),

]
