from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """Extend parent models by timestamp fields."""

    created_at = models.DateTimeField(_("Creation date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Last update date"), auto_now=True)

    class Meta:
        abstract = True
