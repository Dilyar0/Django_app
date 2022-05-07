from django.urls import path
from . import views, models


app_name = "parser_urls"
urlpatterns = [
    path("parser/", views.ParserFormView.as_view(), name="parser_view"),
    path("plants/", views.PlantsListView.as_view(
        queryset=models.Plant.objects.order_by("-id")
    ), name="plants_list"),
]