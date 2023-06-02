from django.db import models
from datetime import datetime

class Link(models.Model):
    target_url = models.URLField(blank=False)
    short_url = models.SlugField(blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url + " --> " + self.target_url + "( " + self.created.strftime("%c") + " )"

class Click(models.Model):
    link_clicked = models.ForeignKey(Link, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    ip_routable = models.BooleanField()

    def __str__(self):
        return self.ip + " --> /" + self.link_clicked.short_url + "/ --> " + self.link_clicked.target_url