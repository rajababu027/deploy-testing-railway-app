from django.urls import path
from .views import ItemList, ItemDetail, LocationDetail, LocationList, VideoDetailsList, VideoDetailsDetail,UserDetailsList, UserDetailsDetail

urlpatterns = [
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
    path('video/', VideoDetailsList.as_view()),
    path('video/<int:pk>/', VideoDetailsDetail.as_view()),
    path('user/', UserDetailsList.as_view()),
    path('user/<int:pk>/', UserDetailsDetail.as_view()),
]

