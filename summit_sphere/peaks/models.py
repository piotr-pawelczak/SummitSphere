from django.db import models
from django.utils.translation import gettext_lazy as _

from summit_sphere.commons.models import TimeStampedModel
from summit_sphere.users.models import User


class Region(models.Model):
    name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=2)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        """Return string representation of the Region."""
        return self.name


class Peak(models.Model):
    name = models.CharField(_("Name of the peak"), max_length=200, db_index=True)
    alternative_names = models.TextField(blank=True, default="")
    unicode_name = models.CharField(
        _("Unicode name of the peak"), max_length=200, db_index=True
    )
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, default="")
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    elevation = models.DecimalField(
        _("Elevation of the peak"), max_digits=5, decimal_places=1
    )
    country_code = models.CharField(max_length=10)

    class Meta:
        ordering = ["unicode_name"]

    def __str__(self) -> str:
        """Return string representation of the Peak."""
        return f"{self.name} ({self.elevation})"

    def get_coordinates(self) -> str:
        return f"{self.latitude}, {self.longitude}"


class Visit(TimeStampedModel):
    peak = models.ForeignKey(Peak, on_delete=models.CASCADE, related_name="visits")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="visits")
    visited_at = models.DateTimeField(_("Visit date"), blank=True, null=True)
    description = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        """Return string representation of the Visit."""
        return f"{self.peak} - {self.user}"
