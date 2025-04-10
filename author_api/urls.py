from rest_framework.routers import DefaultRouter

from author_api import views


router = DefaultRouter()

router.register(r'authors', views.AuthorViewSet, basename='author')

urlpatterns = []

urlpatterns += router.urls
