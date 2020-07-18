from django.urls import path
from . import views

# 127.0.0.1:8000/base
urlpatterns = [
    path('base/', views.home), # lexical/templates/base.html
    path('blog/neuro/', views.neuro), # lexical/blog/templates/blog/neuro.html
    path('blog/psycho/', views.psycho), # ""
    path('blog/date/', views.date_actuelle), # ""
    path('blog/detail/', views.product_detail_view), # ""
    path('blog/addition/<int:nombre1>/<int:nombre2>/', views.addition) # ""
]
