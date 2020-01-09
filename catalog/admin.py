from django.contrib import admin
from .models import Author, Dewey, Publication


class PublicationAdmin(admin.ModelAdmin):
    """Choix des champs a afficher"""

    list_display = (
        "dewey_number",
        "type_publication",
        "reference",
        "name",
        "author",
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
        ("Reference", {"fields": fields_reference}),
        (
            "Publication",
            {"classes": ("wide", "extrapretty"), "fields": fields_publication},
        ),
        ("Details", {"classes": ("collapse",), "fields": fields_details}),
    )

    radio_fields = {"type_publication": admin.HORIZONTAL}
    readonly_fields = ("reference",)
    # autocomplete_fields = ("dewey_name", "")


class AuthorAdmin(admin.ModelAdmin):
    """Choix des champs a afficher"""

    list_display = (
        "last_name",
        "first_name",
        "date_birth",
        "century_birth",
    )
    list_identity = [("last_name", "first_name",)]
    list_birth = [("date_birth", "place_birth", "century_birth")]
    list_death = [("date_died", "place_died",)]
    list_details = [("content", "image_url", "image_file",)]
    fieldsets = (
        ("Identité", {"fields": list_identity}),
        ("Naissance", {"fields": list_birth}),
        ("Décès", {"classes": ("collapse",), "fields": list_death}),
        ("Details", {"classes": ("collapse",), "fields": list_details}),
    )

    readonly_fields = ("century_birth",)


class DeweyAdmin(admin.ModelAdmin):
    """Choix des champs a afficher"""

    list_display = (
        "number",
        "name",
        "color",
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Dewey, DeweyAdmin)
