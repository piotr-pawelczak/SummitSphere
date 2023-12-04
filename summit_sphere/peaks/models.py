from django.db import models
from django.utils.translation import gettext_lazy as _


class Peak(models.Model):
    name = models.CharField(_("Name of the peak"), max_length=200, db_index=True)
    alternative_names = models.TextField(blank=True, default="")
    unicode_name = models.CharField(_("Unicode name of the peak"), max_length=200)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    elevation = models.DecimalField(
        _("Elevation of the peak"), max_digits=5, decimal_places=1
    )
    country_code = models.CharField(max_length=2)

    def __str__(self) -> str:
        """Return string representation of the object."""
        return f"{self.name} ({self.elevation})"
