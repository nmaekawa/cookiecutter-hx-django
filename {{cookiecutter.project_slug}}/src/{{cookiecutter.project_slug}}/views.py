import glob
import os

from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# get available vue templates
vue_pathname = "{}/*.html".format(os.path.join(settings.VUE_ROOTDIR, "dist"))
template_list = glob.glob(vue_pathname)
VUE_PAGES = [os.path.basename(x).split(".")[0] for x in template_list]

# workaround for vue integration
def vue_page(request, page):
    if not request.user.is_authenticated:
        if settings.USE_HKEY:
            next_url = request.build_absolute_uri("/{}/".format(page))
            redirect_url = "{}?{}".format(
                reverse("cas_ng_login"),
                urlencode({"next": next_url}),
            )
            return HttpResponseRedirect(redirect_url)
        elif settings.DEBUG and settings.HXYDRA_BYPASS_AUTH:
            pass
        else:
            return HttpResponse(
                "<p>Welcome, stranger.</p><p>You are not logged in.</p>"
            )

    if page in VUE_PAGES:
        return render(request, template_name="{}.html".format(page))
    else:
        raise Http404("page not found: {}".format(page))
