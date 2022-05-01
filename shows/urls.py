from django.urls import path
from . import views

app_name = 'shows'
urlpatterns = [
    path('shows/', views.shows_all, name="shows_all"),
    path('shows/latest', views.shows_latest, name="shows_latest"),
    path('shows/year', views.shows_in_one_year, name="shows_year"),
    path('shows/anime', views.shows_genre_anime, name="shows_anime"),
    path('shows/action', views.shows_genre_action, name="shows_action"),
    path('shows/romantic', views.shows_genre_romantic, name="shows_romantic"),
    path('shows/horror/', views.shows_genre_horror, name="shows_horror"),
    path('shows/fantastic/', views.shows_genre_fantastic, name="shows_fantastic"),

    path('shows/<int:id>/', views.shows_detail, name="shows_detail"),
    path('shows/<int:id>/update/', views.put_update_shows, name="shows_update"),
    path('shows/<int:id>/delete/', views.shows_delete, name="shows_delete"),
    path('add-show/', views.add_show, name="add_show")
]
