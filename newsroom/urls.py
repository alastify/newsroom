"""ttd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from news.views import news, detail, pridat
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url("^$", view=news, name="index"),
    # url("^archiv/$", name="detail", view=detail),
    # url("^archiv/(?P<id>[0-9-]+)/$", name="detail", view=detail),
    url("^zprava/pridat/$", name="pridat", view=pridat),
    url("^zprava/(?P<id>[0-9-]+)/$", name="detail", view=detail),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
