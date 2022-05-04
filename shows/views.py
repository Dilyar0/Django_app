from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.shortcuts import redirect, reverse
from datetime import datetime, timedelta
from django.views import generic

start_date = datetime.today() - timedelta(days=1)
one_year_date = datetime.today() - timedelta(days=365)


class ShowsListView(generic.ListView):
    template_name = "shows_list.html"
    queryset = models.TVShow.objects.order_by("-id")

    def get_queryset(self):
        return self.queryset


#
# def shows_all(request):
#     shows = models.TVShow.objects.order_by("-id")
#     return render(request, "shows_list.html", {"shows": shows})
#
#
# def shows_latest(request):
#     shows = models.TVShow.objects.filter(created_date__gt=start_date).order_by("-id")
#     return render(request, "shows_list.html", {"shows": shows})
#
#
# def shows_in_one_year(request):
#     shows = models.TVShow.objects.filter(created_date__gt=one_year_date).order_by("-id")
#     return render(request, "shows_list.html", {"shows": shows})
#
#
# def shows_genre_anime(request):
#     shows = models.TVShow.objects.filter(genre="Anime").order_by("-id")
#     return render(request, "shows_list.html", {"shows": shows})
#
#
# def shows_genre_action(request):
#     shows = models.TVShow.objects.filter(genre="Action").order_by("-id")
#     return render(request, "shows_list.html", {"shows": shows})
#
#
# def shows_genre_romantic(request):
#     shows = models.TVShow.objects.filter(genre="Romantic").order_by("-id")
#     return render(request, "shows_list.html", {"shows": shows})
#
#
# def shows_genre_horror(request):
#     shows = models.TVShow.objects.filter(genre="Horror").order_by("-id")
#     return render(request, "shows_list.html", {"shows": shows})
#
#
# def shows_genre_fantastic(request):
#     shows = models.TVShow.objects.filter(genre="Fantastic").order_by("-id")
#     return render(request, "shows_list.html", {"shows": shows})


class ShowsDetailView(generic.DetailView):
    template_name = "shows_detail.html"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.TVShow, id=shows_id)


# def shows_detail(request, id):
#     show = get_object_or_404(models.TVShow, id=id)
#     return render(request, "shows_detail.html", {"show": show})


class ShowsCreateView(generic.CreateView):
    template_name = "add_shows.html"
    form_class = forms.TVShowForm
    queryset = models.TVShow.objects.all()
    success_url = "/shows/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ShowsCreateView, self).form_valid(form=form)


# def add_show(request):
#     method = request.method
#     if method == "POST":
#         form = forms.TVShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # return HttpResponse("Show created successfully")
#             return redirect(reverse("shows:shows_all"))
#     else:
#         form = forms.TVShowForm()
#     return render(request, "add_shows.html", {"form": form})


class ShowsUpdateView(generic.UpdateView):
    template_name = "shows_update.html"
    form_class = forms.TVShowForm
    success_url = "/shows/"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.TVShow, id=shows_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ShowsUpdateView, self).form_valid(form=form)


# def put_update_shows(request, id):
#     show_id = get_object_or_404(models.TVShow, id=id)
#     if request.method == "POST":
#         form = forms.TVShowForm(instance=show_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("shows:shows_all"))
#     else:
#         form = forms.TVShowForm(instance=show_id)
#     return render(request, "shows_update.html", {"form": form, "show": show_id})


class ShowsDeleteView(generic.DeleteView):
    success_url = "/shows/"
    template_name = "confirm_delete_show.html"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.TVShow, id=shows_id)


# def shows_delete(request, id):
#     show_id = get_object_or_404(models.TVShow, id=id)
#     show_id.delete()
#     return redirect(reverse("shows:shows_all"))
