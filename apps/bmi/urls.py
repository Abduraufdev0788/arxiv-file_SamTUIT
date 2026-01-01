from django.urls import path
from apps.bmi.views import TalabaViewSet, BitiruMalakaviyIshViewSet, FaylViewSet, BaholashViewSet

app_name = "bmi"

urlpatterns = [
    path('talabalar/', TalabaViewSet.as_view({'get': 'list', 'post': 'create'}), name='talaba-list'),
    path('talabalar/<int:pk>/', TalabaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='talaba-detail'),
    path('bitiruv_ishlari/', BitiruMalakaviyIshViewSet.as_view({'get': 'list', 'post': 'create'}), name='bitiruv_ishi-list'),
    path('bitiruv_ishlari/<int:pk>/', BitiruMalakaviyIshViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='bitiruv_ishi-detail'),
    path('fayllar/', FaylViewSet.as_view({'get': 'list', 'post': 'create'}), name='fayl-list'),
    path('fayllar/<int:pk>/', FaylViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='fayl-detail'),
    path('baholashlar/', BaholashViewSet.as_view({'get': 'list', 'post': 'create'}), name='baholash-list'),
    path('baholashlar/<int:pk>/', BaholashViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='baholash-detail'),
]
