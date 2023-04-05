from django.contrib import admin
from django.urls import path
from Myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.hello),
    path('hi/', views.hi),
    path('get/', views.get),
    path('create/', views.create),
    path('evenodd/', views.evenodd),
    path('error/', views.error),
    path('index/', views.index),
    path('variables/', views.variables),
    path('employee/', views.employee),
    path('tables/', views.tables),
    path('emptable/', views.emptable),
    path('', views.image),

]


