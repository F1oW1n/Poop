from django.urls import path
from . import views
from .views import (
    PostListview,


)

urlpatterns = [
    path('', PostListview.as_view(), name='home'),
]