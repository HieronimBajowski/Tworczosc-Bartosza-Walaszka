from django.urls import path
from .views import bartosz_walaszek_view

urlpatterns = [
    path('', bartosz_walaszek_view, name='bartosz_walaszek'),
]

