from django.urls import path
from .views import IndexView, csv_upload

urlpatterns = [
    path('', IndexView.as_view(), name=''),
    path('csv_upload', csv_upload, name=''),
]
