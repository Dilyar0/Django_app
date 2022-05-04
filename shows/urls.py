from django.urls import path
from . import views, models
from datetime import datetime, timedelta

start_date = datetime.today() - timedelta(days=1)
one_year_date = datetime.today() - timedelta(days=365)

app_name = "shows"
urlpatterns = [
    path("shows/", views.ShowsListView.as_view(), name="shows_all"),
    path(
        "shows/latest",
        views.ShowsListView.as_view(
            queryset=models.TVShow.objects.filter(created_date__gt=start_date).order_by(
                "-id"
            )
        ),
        name="shows_latest",
    ),
    path(
        "shows/year",
        views.ShowsListView.as_view(
            queryset=models.TVShow.objects.filter(created_date__gt=one_year_date)
        ),
        name="shows_year",
    ),
    path(
        "shows/anime",
        views.ShowsListView.as_view(
            queryset=models.TVShow.objects.filter(genre="Anime")
        ),
        name="shows_anime",
    ),
    path(
        "shows/action",
        views.ShowsListView.as_view(
            queryset=models.TVShow.objects.filter(genre="Action")
        ),
        name="shows_action",
    ),
    path(
        "shows/romantic",
        views.ShowsListView.as_view(
            queryset=models.TVShow.objects.filter(genre="Romantic")
        ),
        name="shows_romantic",
    ),
    path(
        "shows/horror/",
        views.ShowsListView.as_view(
            queryset=models.TVShow.objects.filter(genre="Horror")
        ),
        name="shows_horror",
    ),
    path(
        "shows/fantastic/",
        views.ShowsListView.as_view(
            queryset=models.TVShow.objects.filter(genre="Romantic")
        ),
        name="shows_fantastic",
    ),
    path("shows/<int:id>/", views.ShowsDetailView.as_view(), name="shows_detail"),
    path(
        "shows/<int:id>/update/", views.ShowsUpdateView.as_view(), name="shows_update"
    ),
    path(
        "shows/<int:id>/delete/", views.ShowsDeleteView.as_view(), name="shows_delete"
    ),
    path("add-show/", views.ShowsCreateView.as_view(), name="add_show"),
]
