from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('follow_stock/', views.follow_stock, name='follow_stock'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:profile_id>/edit/',
         views.profile_edit, name='profile_edit'),
    path('registration', views.registration, name='registration')

]
