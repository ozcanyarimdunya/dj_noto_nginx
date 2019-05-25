from django.urls import path

from .views import IndexView, UploadView

app_name = 'sample'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('upload/', UploadView.as_view(), name='upload'),
]
