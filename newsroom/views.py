from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Zpravy
import datetime


def index(request, extra_context=None, **kwargs):

    context = {
        "zpravy": Zpravy.objects.filter(datum__gte=datetime.date.today())
    }

    template = loader.get_template('newsroom/index.html')
    context.update(extra_context or {})

    #return TemplateResponse(request, template, context).render()
    return HttpResponse(template.render(context, request))


def detail(request, id, extra_context=None, **kwargs):

    context = {
        "zprava": Zpravy.objects.get(pk=id)
    }

    template = loader.get_template('newsroom/detail.html')
    context.update(extra_context or {})

    return HttpResponse(template.render(context, request))
