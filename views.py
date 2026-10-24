from django.http import HttpResponseRedirect
from short_url.models import Click, Link
from django.core.exceptions import ObjectDoesNotExist
from ipware import get_client_ip
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_not_required
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

class CreateLink(CreateView):
    model = Link
    fields = ['short_url', 'target_url']
    success_url = '/links/'



class LinkList(ListView):
    queryset = Link.objects.all().order_by("-created")

def try_short_url(request, short_url):
    try:
        link = Link.objects.get(short_url=short_url)
        client_ip, is_routable = get_client_ip(request)
        click = Click.objects.create(link_clicked=link, ip=client_ip, ip_routable=is_routable)
        return HttpResponseRedirect(link.target_url)

    except ObjectDoesNotExist:
        return HttpResponseRedirect("https://wabarr.com")

#apply directly to the function based login view
@login_not_required
def login_view(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      urlForRedirect = request.GET.get('next')
      return redirect(urlForRedirect)
  else:
    form = AuthenticationForm()

  return render(request, "short_url/login.html", {"form": form})