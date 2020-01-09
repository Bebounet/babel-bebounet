from django.db import models
from django.utils.html import format_html
from .utils import get_century


# Create your models here.


class Author(models.Model):
    """Création de la table Author"""

    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=61, editable=False)
    century_birth = models.IntegerField(null=True, blank=True, editable=False)
    date_birth = models.DateField(null=True, blank=True)
    place_birth = models.CharField(max_length=50, null=True, blank=True)
    date_died = models.DateField(null=True, blank=True)
    place_died = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    image_file = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        if self.first_name:
            return f"{self.last_name} {self.first_name}"
        else:
            return self.last_name

    def clean(self):
        if self.date_birth:
            self.century_birth = get_century(self.date_birth.year)
            return self.century_birth


class Dewey(models.Model):
    """Création de la table Dewey qui permet de classer les oeuvres grace au classement dewey"""

    BG_COLOR_CHOICES = [
        ("#000000", "black"),  # Black 000
        ("#8B4513", "maroon"),  # Maroon 100
        ("#FF0000", "red"),  # Red 200
        ("#FF6347", "orange"),  # Orange 300
        ("#FFFF00", "yellow"),  # Yellow 400
        ("#32CD32", "green"),  # Green 500
        ("#1E90FF", "blue"),  # Blue 600
        ("#8B008B", "purple"),  # Purple 700
        ("#A9A9A9", "grey"),  # Grey 800
        ("#FFFFFF", "white"),  # White 900
    ]

    TEXT_COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black"),
    ]

    name = models.CharField(max_length=90)
    number = models.CharField(max_length=3)
    bg_color = models.CharField(
        choices=BG_COLOR_CHOICES, max_length=10, null=True, blank=True, editable=False
    )
    text_color = models.CharField(
        choices=TEXT_COLOR_CHOICES, max_length=7, null=True, blank=True, editable=False
    )

    class Meta:
        ordering = ["number"]

    def __str__(self):
        if self.name:
            return f"{self.number} - {self.name}"
        else:
            return self.number

    def color(self):
        if self.number[:1] == "0":
            return format_html(
                '<span style="background-color: #000000; color: #FFFFFF;">{}</span>',
                self.name,
            )
        elif self.number[:1] == "1":
            return format_html(
                '<span style="background-color: #8B4513; color: #FFFFFF;">{}</span>',
                self.name,
            )
        elif self.number[:1] == "2":
            return format_html(
                '<span style="background-color: #FF0000; color: #FFFFFF;">{}</span>',
                self.name,
            )
        elif self.number[:1] == "3":
            return format_html(
                '<span style="background-color: #FF6347; color: #FFFFFF;">{}</span>',
                self.name,
            )
        elif self.number[:1] == "4":
            return format_html(
                '<span style="background-color: #FFFF00; color: #000000;">{}</span>',
                self.name,
            )
        elif self.number[:1] == "5":
            return format_html(
                '<span style="background-color: #32CD32; color: #FFFFFF;">{}</span>',
                self.name,
            )
        elif self.number[:1] == "6":
            return format_html(
                '<span style="background-color: #1E90FF; color: #FFFFFF;">{}</span>',
                self.name,
            )
        elif self.number[:1] == "7":
            return format_html(
                '<span style="background-color: #8B008B; color: #FFFFFF;">{}</span>',
                self.name,
            )
        elif self.number[:1] == "8":
            return format_html(
                '<span style="background-color: #A9A9A9; color: #FFFFFF;">{}</span>',
                self.name,
            )
        elif self.number[:1] == "9":
            return format_html(
                '<span style="background-color: #FFFFFF; color: #000000;">{}</span>',
                self.name,
            )

    def colored_number(self):
        return format_html(
            '<span style="background-color: "#FFFFFF"; color: "#FFFFFF";">{}</span>',
            self.bg_color,
            self.text_color,
            self.name,
        )


class Publication(models.Model):
    """ Création de la table Publication"""

    TYPE_PUBLICATION_CHOICES = [
        ("B", "Books"),
        ("M", "Music"),
        ("F", "Films"),
        ("_", "Autre"),
    ]

    name = models.CharField(max_length=30)
    type_publication = models.CharField(
        max_length=1, choices=TYPE_PUBLICATION_CHOICES, default="B"
    )
    genre = models.CharField(max_length=30,)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    reference = models.CharField(max_length=30, editable=False)
    dewey_number = models.ForeignKey(Dewey, on_delete=models.PROTECT)
    date_publication = models.DateField(null=True, blank=True)
    nb_tracks_pages = models.IntegerField(null=True, blank=True)
    label_editor = models.CharField(max_length=30, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    image_file = models.ImageField(null=True, blank=True)
    isbn = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        ordering = ["reference"]

    def __str__(self):
        return f"{self.reference} {self.name}"

    def clean(self):
        if self.dewey_number and self.author:
            self.reference = f"{self.dewey_number.number}.{self.author.last_name[:3].upper()}.{self.pk}"
        else:
            self.reference = ""
