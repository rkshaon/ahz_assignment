from author_api.urls import urlpatterns as author_api_urls
from book_api.urls import urlpatterns as book_api_urls


urlpatterns = []
urlpatterns += author_api_urls
urlpatterns += book_api_urls
