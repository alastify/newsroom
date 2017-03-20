from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Zpravy
from .forms import ZpravyForm
import datetime


def news(request, extra_context=None, **kwargs):

    context = {
#        "zpravy": Zpravy.objects.filter(datum__gte=datetime.date.today()),
        "zpravy": Zpravy.objects.all(),
        "form": ZpravyForm(),
    }

    template = loader.get_template('news/index.html')
    context.update(extra_context or {})

    #return TemplateResponse(request, template, context).render()
    return HttpResponse(template.render(context, request))


def detail(request, id, extra_context=None, **kwargs):

    context = {
        "zprava": Zpravy.objects.get(pk=id)
    }

    template = loader.get_template('news/detail.html')
    context.update(extra_context or {})

    return HttpResponse(template.render(context, request))


def pridat(request, extra_context=None, **kwargs):

    if request.POST:
        form = ZpravyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ZpravyForm()

    context = {
        "form": form,
    }

    template = loader.get_template('news/pridat.html')
    context.update(extra_context or {})

    return HttpResponse(template.render(context, request))
