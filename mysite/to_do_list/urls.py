from django.urls import path
from .views import BookViewSet


urlpatterns = [
    path('', BookViewSet.as_view({'get':'list','post':'create'}), name='book_list'),
    path('<int:pk>/', BookViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}), name='book_detail'),
]