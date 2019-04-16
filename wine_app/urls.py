from django.urls import path

from wine_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('wines/', views.WineListView.as_view(), name='wines'),
    path('wine/<int:pk>', views.WineDetailView.as_view(), name='wine-detail'),
    path('api/wine/<int:pk>', views.get_wine, name='wine-api'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('restapi/', views.restapi, name='restapi'),

]