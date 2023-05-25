from django.contrib import admin
from short_url.models import *

class ClickAdmin(admin.ModelAdmin):

    fields = ["link_clicked", "ip", "ip_routable"]

class LinkAdmin(admin.ModelAdmin):

    fields = ["target_url", "short_url", "created"]
    readonly_fields = ["created"]


admin.site.register(Link, LinkAdmin)
admin.site.register(Click, ClickAdmin)

