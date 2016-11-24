from django.contrib import admin

# Register your models here.
from .models import Apply, Attachment, Term

class ApplyModelAdmin(admin.ModelAdmin):
    class meta:
        model = Apply
        field = (
        "first_name",
        "second_name",
        "email",
        "attachments"
        )

admin.site.register(Apply, ApplyModelAdmin)
admin.site.register(Attachment)
admin.site.register(Term)
