from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('charts/', views.charts, name='charts'),

    # API Paths
    path('api/barangays/', views.BarangayAPIView.as_view(), name='barangay-api'),
    path('api/bulletin/', views.CaseBulletinAPIView.as_view(), name='bulletin-api'),
    path('api/bulletin/latest', views.LatestBulletinAPIView.as_view(), name='latest-bulletin-api'),
    path('api/bulletin/daily', views.DailyCaseBulletinAPIView.as_view(), name='daily-bulletin-api'),
    path('api/cases/', views.CaseAPIView.as_view(), name='cases-api'),
]
