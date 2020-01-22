from django.contrib import admin
from .models import Author, Dewey, Publication
from django.utils.translation import gettext as _
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author


class DeweyResource(resources.ModelResource):
    class Meta:
        model = Dewey


class PublicationResource(resources.ModelResource):
    class Meta:
        model = Publication


class PublicationAdmin(ImportExportModelAdmin):
    """Choix des champs a afficher"""

    list_display = (
        "name",
        "reference",
        "author",
        "type_publication",
        "dewey_number",
        "label_editor",
        "nb_tracks_pages",
        "date_publication",
    )
    # fields = (
    #     ("dewey_number", "type_publication", "reference"),
    #     ("name", "author", "label_editor"),
    #     ("nb_tracks_pages", "date_publication", "isbn"),
    #     ("content", "image_url"),
    # )
    fields_reference = ("type_publication", "dewey_number", "reference")
    fields_publication = ("name", "author", "label_editor")
    fields_details = (
        ("date_publication", "nb_tracks_pages", "isbn"),
        ("content", "image_url", "image_file"),
    )

    fieldsets = (
        (_("Référence"), {"fields": fields_reference}),
        (
            _("Publication"),
            {"classes": ("wide", "extrapretty"), "fields": fields_publication},
        ),
        (_("Détails"), {"classes": ("collapse",), "fields": fields_details}),
    )

    radio_fields = {"type_publication": admin.HORIZONTAL}
    readonly_fields = ("reference",)
    search_fields = ["name", "reference", "dewey_number__number"]
    autocomplete_fields = ["author", "dewey_number"]
    list_filter = (
        "dewey_number__number",
        "author__last_name",
    )
    resource_class = PublicationResource


class AuthorAdmin(ImportExportModelAdmin):
    """Choix des champs a afficher"""

    list_display = (
        "last_name",
        "first_name",
        "name",
        "date_birth",
        "century_birth",
    )
    list_identity = [("last_name", "first_name",)]
    list_birth = [("date_birth", "place_birth", "century_birth")]
    list_death = [("date_died", "place_died",)]
    list_details = [("content", "image_url", "image_file",)]
    fieldsets = (
        (_("Identité"), {"fields": list_identity}),
        (_("Naissance"), {"fields": list_birth}),
        (_("Contemporain ?"), {"classes": ("collapse",), "fields": list_death}),
        (_("Details"), {"classes": ("collapse",), "fields": list_details}),
    )
    readonly_fields = ("century_birth",)
    search_fields = ["first_name", "last_name", "name"]
    list_filter = ("century_birth",)
    resource_class = AuthorResource


class DeweyAdmin(ImportExportModelAdmin):
    """Choix des champs a afficher"""

    list_display = (
        "number",
        "name",
        # "color",
        "colored_number",
        # "set_dewey_color_publication",
    )
    search_fields = ["number", "name"]
    list_filter = ("number",)
    # actions = ["add_xls"]
    resource_class = DeweyResource


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Dewey, DeweyAdmin)
