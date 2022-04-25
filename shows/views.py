from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.shortcuts import redirect, reverse


def shows_all(request):
    shows = models.TVShow.objects.all()
    return render(request, "shows_list.html", {"shows": shows})


def shows_detail(request, id):
    show = get_object_or_404(models.TVShow, id=id)
    return render(request, "shows_detail.html", {"show": show})


def add_show(request):
    method = request.method
    if method == "POST":
        form = forms.TVShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse("Show created successfully")
            return redirect(reverse("shows:shows_all"))
    else:
        form = forms.TVShowForm()
    return render(request, "add_shows.html", {'form': form})