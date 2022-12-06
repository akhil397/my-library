from django.urls import path
from fillform import views

urlpatterns = [
    path('', views.formview, name='formview'),
    path('despach/',views.despach, name='despach')
]