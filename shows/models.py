from django.db import models


class TVShow(models.Model):
    GENRE_CHOICE = (
        ("Comedy", "COMEDY"),
        ("Action", "ACTION"),
        ("Romantic", "ROMANTIC"),
        ("Horror", "HORROR"),
        ("Anime", "ANIME"),
        ("Fantastic", "FANTASTIC"),
    )
    title = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(upload_to="")
    quantity = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE)
    duration = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class ShowComment(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    shows = models.ForeignKey(
        TVShow, on_delete=models.CASCADE, related_name="shows_comment"
    )

    def __str__(self):
        return self.shows.title
