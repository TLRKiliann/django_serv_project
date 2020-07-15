from django.urls import path
from blog import views

# 127.0.0.1:8000/accueil
urlpatterns = [
    path('accueil/', views.home),
    path('neuro/', views.neuro),
    path('psycho/', views.psycho),
]