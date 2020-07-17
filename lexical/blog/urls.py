from django.urls import path
from . import views

# 127.0.0.1:8000/accueil
urlpatterns = [
    path('base/', views.home), # pour une nouvelle app
    path('blog/neuro/', views.neuro), # pour une nouvelle app
    path('blog/psycho/', views.psycho), # pour une nouvelle app
    path('blog/date/', views.date_actuelle),
    path('blog/addition/<int:nombre1>/<int:nombre2>/', views.addition)
]
