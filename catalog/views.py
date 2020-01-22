import json
from django.shortcuts import render
from django.conf import settings
from .models import Dewey, Publication

# Create your views here.

CONTEXT_GLOBAL = {
    "mediatheque_name": "Bibliothèque de Bebounet",
    "mediatheque_adr": "Aramon",
    "dev_name": "Nicolas Sagnier",
    "dev_github": "https://github.com/Bebounet/babel-bebounet",
    "dev_cadre": "Formation Django/Python FORMEXT",
}


def publication(request):
    try:
        record_list = Dewey.objects.all()

        publication_list = Publication.objects.all()
    except:
        record_list = publication_list = None

    context_local = {
        "title": "Liste des publications du catalogue",
        "description": "Vous trouverez tous les ouvrages et leurs classifications",
    }
    context_page = {
        "global": CONTEXT_GLOBAL,
        "local": context_local,
        "dewey_object_list": record_list,
        "publication_object_list": publication_list,
    }
    return render(request, "catalog/publication.html", context=context_page)


def home(request):
    context_local = {
        "title": "Page d'accueil de Babel",
        "description": "Bienvenue sur cette page en cours de réalisation",
    }
    context_page = {"global": CONTEXT_GLOBAL, "local": context_local}
    return render(request, "catalog/index.html", context=context_page)


def about(request):
    context_local = {
        "title": "A propos de Babel",
        "description": "Vous trouverez tout les détails de spécification ici.",
    }
    context_page = {"global": CONTEXT_GLOBAL, "local": context_local}
    return render(request, "catalog/about.html", context=context_page)


def newsroom(request):
    """ The home page for babel"""

    basedir = settings.BASE_DIR
    filename = basedir + "/scrap/checkurl.json"
    try:
        with open(filename, "r") as f:
            dict_checkurl = json.load(f)
    except Exception as e:
        dict_checkurl = {"error", str(e)}
    context_local = {
        "title": "Salle de presse",
        "description": "Decouvrez des sites !",
    }

    context_page = {
        "global": CONTEXT_GLOBAL,
        "checkurl": dict_checkurl,
        "local": context_local,
    }
    #  Pour ajouter un dictionnaire a un dictionnaire, j'utilise
    #  bigdict = { **onedict, **anotherdict }
    return render(request, "catalog/newsroom.html", context=context_page)
