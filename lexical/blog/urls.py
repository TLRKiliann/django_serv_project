from django.urls import path
from . import views

# 127.0.0.1:8000/accueil
urlpatterns = [
    path('accueil/', views.home),
    path('neuro/', views.neuro),
    path('psycho/', views.psycho),
    path('date/', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
]
