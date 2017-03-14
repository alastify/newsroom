from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Zpravy(models.Model):
    datum = models.DateTimeField(
        verbose_name="Datum zveřejnění",
        auto_now_add=True,
    )

    titulek = models.CharField(
        verbose_name="Titulek",
        max_length=127,
        default="",
    )

    obsah = models.CharField(
        verbose_name="Obsah",
        max_length=999,
        default="",
    )

    obrazek = models.FileField(
        verbose_name="Obrázek",
        upload_to="images",
        max_length=255,
        null=True,
        blank=True
    )

    def url(self):
        url_name = "detail"
        kwargs = { "id": self.id}

        return reverse(url_name, kwargs=kwargs)


    def __str__(self):
        return self.titulek

    class Meta:
        verbose_name = "Zpráva"
        verbose_name_plural = "Zprávy"
