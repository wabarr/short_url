from django.contrib import admin
from short_url.models import *

class ShortURLAdminSite(admin.AdminSite):
    site_header = "Short URL Admin"

shortURLAdminSite = ShortURLAdminSite(name='Short URL Admin')


class ClickAdmin(admin.ModelAdmin):

    fields = ["link_clicked", "ip", "ip_routable"]

class LinkAdmin(admin.ModelAdmin):

    fields = ["target_url", "short_url", "created"]
    readonly_fields = ["created"]


shortURLAdminSite.register(Link, LinkAdmin)
shortURLAdminSite.register(Click, ClickAdmin)

