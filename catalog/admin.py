from django.contrib import admin
from .models import Author, Dewey, Publication


class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "author",
        "reference",
        "type_publication",
        "genre",
        "dewey_number",
        "date_publication",
        "label_editor",
    )

    # fieldsets = ((None, {"fields": (),}),)


admin.site.register(Author)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Dewey)
