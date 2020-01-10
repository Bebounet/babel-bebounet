from django.db import models
from django.utils.html import format_html
from .utils import get_century, xls_reader
from django.utils.translation import gettext as _


# Create your models here.


class Author(models.Model):
    """Création de la table Author"""

    first_name = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("Prénom")
    )
    last_name = models.CharField(max_length=30, verbose_name=_("Nom"))
    name = models.CharField(
        max_length=61, editable=False, verbose_name=_("Nom complet")
    )
    century_birth = models.IntegerField(
        null=True, blank=True, editable=False, verbose_name=_("Siècle de naissance")
    )
    date_birth = models.DateField(
        null=True, blank=True, verbose_name=_("Date de naissance")
    )
    place_birth = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Lieu de naissance")
    )
    date_died = models.DateField(null=True, blank=True, verbose_name=_("Date de décès"))
    place_died = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Lieu de décès")
    )
    content = models.TextField(null=True, blank=True, verbose_name=_("Contenu"))
    image_url = models.URLField(null=True, blank=True, verbose_name=_("Url de l'image"))
    image_file = models.ImageField(
        null=True, blank=True, verbose_name=_("Fichier de l'image")
    )

    class Meta:
        ordering = ["last_name"]
        verbose_name = _("Auteur")

    def __str__(self):
        if self.first_name:
            return f"{self.last_name} {self.first_name}"
        else:
            return self.last_name

    def clean(self):
        """ 
            update of century from date_birth using catalog.utils.get_century
            update name in <first_name space last_name> or <last_name>
        """
        if self.date_birth:
            self.century_birth = get_century(self.date_birth.year)
            return self.century_birth
        if self.first_name:
            self.name = f"{self.last_name} {self.first_name}"
            return self.name
        else:
            self.name = self.last_name
            return self.name


class Dewey(models.Model):
    """Création de la table Dewey qui permet de classer les oeuvres grace au classement dewey"""

    BG_COLOR_CHOICES = [
        ("#000000", "#FFFFFF", "black"),  # Black 000
        ("#8B4513", "#FFFFFF", "maroon"),  # Maroon 100
        ("#FF0000", "#FFFFFF", "red"),  # Red 200
        ("#FF6347", "#FFFFFF", "orange"),  # Orange 300
        ("#FFFF00", "#000000", "yellow"),  # Yellow 400
        ("#32CD32", "#FFFFFF", "green"),  # Green 500
        ("#1E90FF", "#FFFFFF", "blue"),  # Blue 600
        ("#8B008B", "#FFFFFF", "purple"),  # Purple 700
        ("#A9A9A9", "#FFFFFF", "grey"),  # Grey 800
        ("#FFFFFF", "#000000", "white"),  # White 900
    ]

    TEXT_COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black"),
    ]

    name = models.CharField(max_length=120, verbose_name=_("Nom"))
    number = models.CharField(max_length=12, verbose_name=_("Numéro"))
    bg_color = models.CharField(max_length=10, null=True, blank=True, editable=False)
    text_color = models.CharField(
        choices=TEXT_COLOR_CHOICES, max_length=7, null=True, blank=True, editable=False
    )

    class Meta:
        ordering = ["number"]
        verbose_name = _("Classement dewey")

    def __str__(self):
        if self.name:
            return f"{self.number} - {self.name}"
        else:
            return self.number

    def clean(self):
        # liste_dewey = xls_reader()
        # print(f"*****{liste_dewey[0]}   *****   {liste_dewey[1]}")
        # self.number = liste_dewey[0]
        # self.name = liste_dewey[1]
        if self.number:
            self.number_validator()

    def colored_number(self):
        """Choisir la couleur classement dewey en fonction du dewey_number"""
        if self.number:
            try:
                i = int(self.number[:1])
                return format_html(
                    '<span style="background-color: {}; color: {}; min-width: 50px;">{}</span>',
                    self.BG_COLOR_CHOICES[i][0],  # bg color
                    self.BG_COLOR_CHOICES[i][1],  # text color
                    self.number,
                )
            except:
                return "Wrong Format"

    def number_validator(self):
        """ Verification taille de number, si = 2 on rajoute 0 devant, si = 1 on rajoute 00 devant"""
        if len(self.number) == 3:
            return self.number
        elif len(self.number) == 2:
            self.number = "0" + self.number
            return self.number
        elif len(self.number) == 1:
            self.number = "00" + self.number
            return self.number


class Publication(models.Model):
    """ Création de la table Publication"""

    TYPE_PUBLICATION_CHOICES = [
        ("B", "Books"),
        ("M", "Music"),
        ("F", "Films"),
        ("_", "Autre"),
    ]

    name = models.CharField(max_length=120, verbose_name=_("Nom"))
    type_publication = models.CharField(
        max_length=1,
        choices=TYPE_PUBLICATION_CHOICES,
        default="B",
        verbose_name=_("Type de publication"),
    )
    genre = models.CharField(max_length=30, verbose_name=_("Genre"))
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT, verbose_name=_("Auteur")
    )
    reference = models.CharField(
        max_length=30, editable=False, verbose_name=_("Référence")
    )
    dewey_number = models.ForeignKey(
        Dewey, on_delete=models.PROTECT, verbose_name=_("Numéro dewey")
    )
    date_publication = models.DateField(
        null=True, blank=True, verbose_name=_("Date de publication")
    )
    nb_tracks_pages = models.IntegerField(
        null=True, blank=True, verbose_name=_("Nombre de Titres/Pages")
    )
    label_editor = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("Label/Editeur")
    )
    content = models.TextField(null=True, blank=True, verbose_name=_("Contenu"))
    image_url = models.URLField(null=True, blank=True, verbose_name=_("Url de l'image"))
    image_file = models.ImageField(
        null=True, blank=True, verbose_name=_("Fichier de l'image")
    )
    isbn = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("ISBN")
    )

    class Meta:
        ordering = ["reference"]
        verbose_name = _("Publication")

    def __str__(self):
        return f"{self.reference} {self.name}"

    def clean(self):
        if self.dewey_number and self.author:
            self.reference = f"{self.dewey_number.number}.{self.author.last_name[:3].upper()}.{self.pk}"
        else:
            self.reference = ""
