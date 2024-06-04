from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='mainPage'),
    path('home/', views.home, name='homePage'),
    path('contact/', views.contactus, name='contactPage'),
    path('about/', views.about, name='aboutPage'),
    path('services/', views.services, name='servicesPage'),
    path('resource/', views.resources, name='resourcePage'),
    path('signup/', views.signup, name='signupPage'),
    path('login/', views.login, name='loginPage'),
    # path('detect_signature/', views.detect_signature, name='detect_signature'),
    path('detect_signature/', views.detect_signature, name='detect_signature'),


]
