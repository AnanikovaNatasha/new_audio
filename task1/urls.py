from django.urls import path
from .views import test_view

app_name = 'task1'

urlpatterns = [
    path('', test_view, name='test_view'),
]
