from django.urls import path
from rest_framework import routers
from . import views





# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.GainExperience.as_view(), name='gain_experience'),
    path('retrieve_profile/', views.GetProfile.as_view(), name='retrieve_profile'),
   
]