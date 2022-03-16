from . import views
from .views import (
    PostListview,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView

)

urlpatterns = [
    path('', PostListview.as_view(), name='home'),
    path('post/new/', PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('about/', views.about, name='about')
]