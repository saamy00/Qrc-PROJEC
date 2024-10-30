from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('facilities/', views.facilities, name='facilities'),
    path('services/', views.services, name='services'),
    path('qrcode/', views.generate_qr_code, name='qrcode'),

    
    

]
