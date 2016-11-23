from django.contrib import admin

# Register your models here.
from .models import Apply

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
