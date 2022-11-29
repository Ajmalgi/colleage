from django.urls import path
from .import views
app_name = 'colleage'
urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('courses',views.courses,name='courses'),
    
]
