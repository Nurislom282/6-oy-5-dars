from django.urls import path
from .views import main,carmodels,cars


urlpatterns = [
    path('',main,name='home'),
    path('carmodels/',carmodels,name='models'),
    path('cars/',cars,name='car' )
]