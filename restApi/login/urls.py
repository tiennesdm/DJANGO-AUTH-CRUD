from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Login
urlpatterns = [
path('', Login.as_view()),
# path('header', TokenAuthentication)
# path('<int:pk>/', DetailView.as_view()),
# path('rawSQL',  SQLRAWQUERY.raw_SQL),
#     # path('hello/', HelloView.as_view(), name='hello'),

]