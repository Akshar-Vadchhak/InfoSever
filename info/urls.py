from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.info, name='info'),
    path("addinfo", views.addInfo, name="addinfo"),
    path("<int:info_Id>/", views.infoDetails, name="InfoDetails") 
] 