from django.urls import path
from . import views


app_name = 'shows'
urlpatterns = [
    path('shows/', views.shows_all, name="shows_all"),
    path('shows/<int:id>/', views.shows_detail, name="shows_detail"),
    path('add-show/', views.add_show, name="add_show")
]