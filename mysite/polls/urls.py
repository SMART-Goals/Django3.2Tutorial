# third party imports
from django.urls import path

# package imports
from polls import views

urlpatterns = [
    path('', views.index, name='index'),
]
