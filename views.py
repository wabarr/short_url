from django.http import HttpResponseRedirect
from short_url.models import Click, Link
from django.core.exceptions import ObjectDoesNotExist
from ipware import get_client_ip

def try_short_url(request, short_url):
    try:
        link = Link.objects.get(short_url=short_url)
        client_ip, is_routable = get_client_ip(request)
        click = Click.objects.create(link_clicked=link, ip=client_ip, ip_routable=is_routable)
        return HttpResponseRedirect(link.target_url)

    except ObjectDoesNotExist:
        return HttpResponseRedirect("https://wabarr.com")
