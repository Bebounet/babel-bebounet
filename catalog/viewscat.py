from django.views.generic import TemplateView, ListView, DetailView
from django.utils.translation import gettext as _
from .models import Publication, Dewey
from .views import CONTEXT_GLOBAL


class MixinContextPage:
    title = _("Mon titre")
    description = _("Ma description")

    def get_mycontext(self):
        context_local = {
            "title": self.title,
            "description": self.description,
        }

        context_page = {
            "global": CONTEXT_GLOBAL,
            "local": context_local,
        }
        return context_page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_page = self.get_mycontext()
        return {**context, **context_page}


class PublicationByDewey(MixinContextPage, ListView):
    """
    Vue permettant de voir les publications filtrées par classement Dewey
    """

    template_name = "catalog/publication.html"
    context_object_name = "publication_object_list"
    # ajout du MixinContextPage pour hériter d'un context global et local
    # ajout du support de la traduction avec _()
    # rendre title dynamique et traduisible
    title = _("Liste des Publications n° {}")
    description = _("Vous trouverez les publications classées par Dewey")

    def get_queryset(self):
        # argument dewey_number provenant de la structure de l'url
        deweynumber = self.kwargs["deweynumber"]

        # requête sur les publications avec le classement dewey spécifié dans l'url
        queryset = Publication.objects.filter(dewey_number__number=deweynumber)

        # et requête avec l'objet dewey
        self.currentdewey = Dewey.objects.get(number=deweynumber)
        self.publication_count = queryset.count()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # requête pour avoir la liste du classement Dewey
        context["dewey_object_list"] = Dewey.objects.all()

        # ajout de l'élément dewey actif
        context["dewey_active"] = self.currentdewey

        # diverses variables
        context["jumbotron_class"] = "dewey" + self.currentdewey.number
        context["publication_count"] = self.publication_count

        # traduction avec le deweynumber de l'url
        # ou avec le display name de l'objet currentdewey récupéré dans get_querryyset()
        self.title = self.title.format(self.currentdewey)

        # appel de la fonction get_mycontext de MixinContextPage
        context_page = self.get_mycontext()

        # retour de deux dictionnaires : context et context_page
        return {**context, **context_page}


class PublicationDetail(MixinContextPage, DetailView):
    template_name = "catalog/publication-detail.html"
    model = Publication
    title = _("Ma publication en détails")


# class publicationByDewey(TemplateView):
#     template_name = "catalog/publication.html"


# class publicationDetail(TemplateView):
#     template_name = "catalog/publication.html"
