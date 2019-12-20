from pip._vendor import requests
import json
import os
from bs4 import BeautifulSoup

# html = requests.get("https://www.liberation.fr/")

# print("Statut :", html.status_code)
# print("Headers :", html.headers)
# print("Text :", html.text)

# html = requests.get("http://localhost:8080/formext/avions/avions")

# print("Statut :", html.status_code)
# print("Headers :", html.headers)
# print("Text :", html.text)

dataset = []

"""

soup.find("meta", property="og:title")
soup.find("meta", property="og:description")
soup.find("meta", property="og:image")
soup.find("meta", property="og:url")

"""


def printseparator():
    """ Fonction qui affiche une ligne de séparation """
    print("-" * 50)


def get(url):
    user_agent_text = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
    headerdict = {"User-Agent": user_agent_text}
    html = requests.get(url, headers=headerdict)
    html.raise_for_status()
    return html


def get_urls(arglist, is_verbose=True):
    """ recuperer tout les urls listés dans listedesurls[ ] """
    for url_en_arg in arglist:
        try:
            html = get(url_en_arg)
        except Exception as e:
            print(f"Erreur de request vers {url_en_arg}")
            print(str(e))
            html = None
        if html:
            displayurl(html, is_verbose)
            writetodict(html, is_verbose)
    # count_dataset(dataset)


def displayurl(html, is_verbose):
    """ Fonction d'affichage du status_code et des headers """
    print(f"--> Il y a {len(html.text)} octets dans {html.url}")
    if is_verbose:
        printseparator()
        print("Statut :", html.status_code)
        printseparator()
        print("Headers :", html.headers)
        printseparator()
        # print("Text :", html.text)
    else:
        print(f"Erreur de request vers {html.url} ---- avec code : {html.status_code}")
        for key, value in html.headers.items():
            print(f"{key} : {value}")


F_URL = "url"
F_STATUS = "status_code"
F_HTML = "content"
F_TITLE = "title"
F_IMAGE = "image"
F_DESC = "description"
F_COUNTER = "nbobjet"
F_DATASET = "dataset"


def writetodict(html, is_verbose=False):
    """ création d'un dictionnaire et ecriture de données dans un fichier 'checkurl.json' """
    # title = search_title(html.text)
    # dict_hmtl = {
    # F_URL: html.url,
    # F_STATUS: html.status_code,
    # F_HTML: html.text[:6000],
    # F_TITLE: title,
    # }
    dict_meta = search_meta(html.text)
    dict_hmtl = {F_STATUS: html.status_code}
    dict_hmtl.update(dict_meta)

    # ATTENTION : dataset est défini en global comme une liste
    global dataset
    dataset.append(dict_hmtl)

    # affiche le nom du fichier .py
    print(__file__)
    # affiche le repertoire absolue pour le système d'exploitation
    print(os.path.abspath(__file__))
    # affiche le repertoire contenant le fichier .py
    print(os.path.dirname(__file__))
    # recupere le nom du fichier dans la configuration du ssysteme d'exploitation
    basedir = os.path.dirname(os.path.abspath(__file__))
    print(basedir)

    dataset_api = {F_COUNTER: len(dataset), F_DATASET: dataset}
    # creation du fichier chekurl.json dans le répertoire scrap
    filename = basedir + "/" + "checkurl.json"
    with open(filename, "w", encoding="utf8") as f:
        json.dump(dataset_api, f)
        print(f"file {filename} created !")


# def count_dataset(data):
#     """ Fornction qui permet de savoir combien d'objet il y a dans le dict """
#     counter = len(data)
#     print(50 * "***")
#     print(counter)
#     data_input = {F_COUNTER: counter}
#     return data_input


def search_title_by_bs4(text):
    """ Recherche d'un titre avec beautifulsoup """
    soup = BeautifulSoup(text, "lxml")

    # ATTENTION CODE TEST FIN DE JOURNEE
    d = soup.find_all("h1")
    if d:
        for h1 in d:
            print(f"--> h1 : {h1}")
    d = soup.find_all("h2")
    if d:
        for h2 in d:
            print(f"--> h2 : {h2}")
    # FIN DE CODE DE FIN DE JOURNEE

    return soup.title.string


def search_meta(text):
    soup = BeautifulSoup(text, "lxml")
    # Recherche des données
    # Verification qu'il y a bien un meta title sinon on recupere title sans passer par la fonction meta -> property
    title = soup.find("meta", property="og:title")
    if not title:
        title_content = soup.title.string
    else:
        title_content = title["content"]
    # Verification qu'il y a bien un meta description sinon on recupere description sans passer par la fonction meta -> property
    desc = soup.find("meta", property="og:description")
    desc_content = desc["content"] if desc else ""

    # Verification qu'il y a bien un meta image sinon on recupere image sans passer par la fonction meta -> property
    img = soup.find("meta", property="og:image")
    img_content = img["content"] if img else ""

    # Verification qu'il y a bien un meta url sinon on recupere url sans passer par la fonction meta -> property
    url = soup.find("meta", property="og:url")
    url_content = url["content"] if url else ""

    # print(f"*****************title = {title}")
    # print(f"*****************desc = {desc}")
    # print(f"*****************img = {img}")
    # print(f"*****************url = {url}")

    # Création du dict
    dict_with_img = {
        F_TITLE: title_content,
        F_DESC: desc_content,
        F_IMAGE: img_content,
        F_URL: url_content,
    }
    print(dict_with_img)
    return dict_with_img


def search_title(text):
    """ Fonction qui cherche le titre d'une page HTML """
    search_meta(text)
    return search_title_by_bs4(text)

    # DEPRECATED USE BEATIFULL SOUP INSTEAD
    retbuffer = begin = 0
    end = None
    begin = text.find("<title>")
    if begin != -1:
        begin += len("<title>")
        end = text[begin:].find("</title>")
        if end != -1:
            end += begin
            retbuffer = text[begin:end]
    print(f"Test search_title : {begin}, {end}, {retbuffer}")
    return retbuffer


if __name__ == "__main__":
    letempsquipasse = ["matin", "midi", "soir", "minuit", "aube"]
    for item in letempsquipasse:
        print(item)

    listedesurls = [
        # "http://localhost:8080/formext/avions/avions",
        "https://openclassrooms.com/",
        "https://www.dealabs.com",
        "https://www.ouest-france.fr/",
        "chrome-extension://aejoelaoggembcahagimdiliamlcdmfm/index.html#requests",
        "https://www.youtube.com/",
        "https://twitter.com/home",
    ]
    get_urls(listedesurls)

print(len(dataset))
