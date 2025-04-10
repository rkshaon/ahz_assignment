from rest_framework.routers import DefaultRouter

from book_api import views


router = DefaultRouter()

router.register(r'genres', views.GenreViewSet, basename='author')
router.register(r'books', views.BookViewSet, basename='book')

urlpatterns = []

urlpatterns += router.urls
